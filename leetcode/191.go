package main

import "fmt"

func main(){
	fmt.Println(hammingWeight(11))
}

func hammingWeight(num uint32) int {
	var count int = 1
	for (num > 0){
		if ((num & 1) > 0){
			count ++
		}
		num = num >> 1
	}
	return count
}
