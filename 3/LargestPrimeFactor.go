/*
    Project Euler Question 3:
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?

    Authur: thebeard@engineerbeard.com
*/

package main

import (
	"math"
	"fmt"
	"time"
)

func main() {
	start := time.Now()
	fmt.Println(largestPrimeFactor(90000133))
	elapsed := time.Since(start)
	fmt.Println("Elapsed:", elapsed)
}

func isSquare(n float64) bool {
	x := math.Sqrt(n)
	c := math.Ceil(x)
	f := math.Floor(x)
	if c == f {
		return true
	} else {
		return false
	}
}

func fermatAlgo(n float64) (float64, float64) {
	a := math.Ceil(math.Sqrt(n))
	b2 := a*a - n
	for !isSquare(b2) {
		a = a + 1;
		b2 = a*a - n
	}
	fmt.Println(a - math.Sqrt(b2), a + math.Sqrt(b2))
	return a - math.Sqrt(b2), a + math.Sqrt(b2)
}

func largestPrimeFactor(n float64) float64 {
	var factors []float64
	a, b := fermatAlgo(n)
	factors = append(factors, a)
	factors = append(factors, b)
	for ;; {
		for i, j := range factors {
			a, b = fermatAlgo(j)
			if a != 1 && b != 1 {
				factors[i] = a
				factors = append(factors, b)
			} else if (a == 1 || b == 1) && (len(factors)-1 == int(i)) {
				break
			}
		}
		biggestFactor := 0.0
		for _, j := range factors {
			if j > biggestFactor {
				biggestFactor = j
			}
		}
		fmt.Println("Prime Factors: ", factors)
		return biggestFactor
	}
}