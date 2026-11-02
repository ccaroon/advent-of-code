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
func FindTotal(blob any, ignoreValue *string) int {
	var total int

	// Type Switch
	switch element := blob.(type) {
	case string:
		// No-Op. Don't care about strings
		// But don't want the default case to kick in
		// ACK and move on
		// fmt.Println("STRING")
	// case int:
	// NOTE: I don't this this case ever gets used b/c the JSON parser
	// parses numbers as float64 by default
	// fmt.Println("INT")
	// total += element
	case float64:
		// fmt.Println("FLOAT64")
		total += int(element)
	case map[string]any:
		// fmt.Println("MAP")
		// 	Check for ignored property value
		ignoreElement := false
		if ignoreValue != nil {
			for _, subElement := range element {
				switch seValue := subElement.(type) {
				case string:
					if seValue == *ignoreValue {
						ignoreElement = true
						break
					}
				}
			}
		}

		if !ignoreElement {
			// fmt.Printf("KEEPING: (%v)\n", element)
			for _, subElement := range element {
				total += FindTotal(subElement, ignoreValue)
			}
		} else {
			// fmt.Printf("IGNORING: (%v)\n", element)
		}

	case []any:
		// fmt.Println("SLICE")
		for _, subElement := range element {
			total += FindTotal(subElement, ignoreValue)
		}
	default:
		msg := fmt.Sprintf("UNKNOWN TYPE: (%T)\n", element)
		panic(msg)
	}

	return total
}
