package day1

import (
	"strconv"
	"strings"
)

func Star1(test string) int {
	frequency := 0
	changes := strings.Split(test, "\n")

	for _, value := range changes {
		currentChange, _ := strconv.Atoi(value)
		frequency += currentChange
	}

	return frequency
}

func Star2(test string) int {
	frequency := 0
	changes := strings.Split(test, "\n")
	pastFrequencyValues := make(map[int]bool)

	for {
		for _, value := range changes {
			currentChange, _ := strconv.Atoi(value)
			frequency += currentChange
			if pastFrequencyValues[frequency] == true {
				return frequency
			}
			pastFrequencyValues[frequency] = true
		}
	}
}