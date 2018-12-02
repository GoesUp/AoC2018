package main

import (
	"bufio"
	"fmt"
	"github.com/GoesUp/AoC2018/day1"
	"github.com/GoesUp/AoC2018/day2"
	"io/ioutil"
	"log"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter day: ")
	day, _ := reader.ReadString('\n')
	fmt.Print("Enter star: ")
	star, _ := reader.ReadString('\n')

	test, err := ioutil.ReadFile("./input/day" + day[:len(day)-1] + ".txt")
	if err != nil {
		log.Panicln(err)
	}
	properTest := string(test)

	switch day[:len(day)-1]+","+star[:len(day)-1] {
	case "1,1":
		fmt.Println(day1.Star1(properTest))
	case "1,2":
		fmt.Println(day1.Star2(properTest))
	case "2,1":
		fmt.Println(day2.Star1(properTest))
	case "2,2":
		fmt.Println(day2.Star2(properTest))

	}
}
