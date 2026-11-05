package day13

type Person struct {
	name  string
	rules []*Rule
}

func NewPerson(name string) *Person {
	return &Person{
		name: name,
	}
}

func (person *Person) addRule(rule *Rule) {
	person.rules = append(person.rules, rule)
}
