package day12

func (day *Day12) SolvePart1() error {
	data, err := ParseJSON(day.Input[0])
	if err != nil {
		return err
	}

	day.Answer = FindTotal(data, nil)

	return nil
}

func (day *Day12) SolvePart2() error {
	data, err := ParseJSON(day.Input[0])
	if err != nil {
		return err
	}

	ignoreValue := "red"
	day.Answer = FindTotal(data, &ignoreValue)

	return nil
}
