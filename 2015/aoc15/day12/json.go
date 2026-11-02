package day12

import (
	"encoding/json"
	"fmt"
)

func ParseJSON(input string) (any, error) {
	var err error
	var blob any

	err = json.Unmarshal([]byte(input), &blob)
	if err != nil {
		return nil, err
	}

	return blob, nil
}

// array, object, number, string
func FindTotal(blob any) int {
	var total int

	switch element := blob.(type) {
	case string:
		// fmt.Println("STRING")
	case int:
		// fmt.Println("INT")
		total += element
	case float64:
		// fmt.Println("FLOAT64")
		total += int(element)
	case map[string]any:
		// fmt.Println("MAP")
		for _, subElement := range element {
			total += FindTotal(subElement)
		}
	case []any:
		// fmt.Println("SLICE")
		for _, subElement := range element {
			total += FindTotal(subElement)
		}
	default:
		msg := fmt.Sprintf("UNKNOWN TYPE: (%T)\n", element)
		panic(msg)
	}

	return total
}
