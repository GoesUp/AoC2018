package day2

import (
	"strings"
)

func Star1(test string) int {
	rows := strings.Split(test, "\n")

	countTwo := 0
	countThree := 0

	for _, i := range rows {
		letters := make(map[int32]int)
		for _, char := range i {
			_, valid := letters[char]
			if !valid {
				letters[char] = 1
			} else {
				letters[char] += 1
			}
		}

		alreadyTwo := false
		alreadyThree := false
		for _, val := range letters {
			if val == 2 && !alreadyTwo {
				countTwo++
				alreadyTwo = true
			} else if val == 3 && !alreadyThree {
				countThree++
				alreadyThree = true
			}
		}
	}

	return countTwo * countThree
}

func Star2(test string) string {
	rows := strings.Split(test, "\n")

	for i, rowPrimary := range rows {
		for _, rowCompared := range rows[i+1:] {
			if len(rowPrimary) == len(rowCompared) {
				errors := 0
				solution := ""

				for k, letter := range rowPrimary {
					if uint8(letter) == rowCompared[k] {
						solution += string(letter)
					} else {
						errors++
					}
				}

				if errors == 1 {
					return solution
				}
			}
		}
	}

	return ""
}
