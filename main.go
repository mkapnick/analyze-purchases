package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

type Transaction struct {
	Date   time.Time
	Place  string
	Amount float64
}

type Transactions struct {
	Transactions     []Transaction
	Max              float64
	Min              float64
	Average          float64
	Sum              float64
	NumTransactions  int
	Places           []string
	PlacesMap        map[string]int
	Dates            []string
	DatesMap         map[string]int
	Order            string
	OrderedPlaces    []string
	OrderedPurchases []float64
}

const TIME_LAYOUT = "01/01/2017"

func main() {

	// open the file for read purposes
	file, err := os.OpenFile("./transactions.csv", os.O_RDONLY, 0600)
	if err != nil {
		fmt.Println("Error opening file")
		os.Exit(0)
	}

	// Create a scanner over the file
	scanner := bufio.NewScanner(file)

	// declare variables we need
	var transactions []Transaction
	var places []string
	var dates []string
	// var orderedPlaces []string
	var orderedPurchases []float64
	min := 10000.0
	max := -1.0
	sum := 0.0
	placesMap := make(map[string]int)
	datesMap := make(map[string]int)

	// File should be in the form:
	// Date,Place,Amount
	// Ex: 09/25/2017,Market Street,24.30
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Split(line, ",")
		date := parts[0]
		place := parts[1]
		amount, _ := strconv.ParseFloat(parts[2], 64)
		dateObj, _ := time.Parse(date, TIME_LAYOUT)

		if amount != 0 && amount < min {
			min = amount
		}

		if amount > max {
			max = amount
		}

		sum = sum + amount
		places = append(places, place)
		dates = append(dates, date)
		orderedPurchases = append(orderedPurchases, amount)

		// use this to get more accurate count
		// p := place[0:5]

		// maps
		if placesMap[place] == 0 {
			placesMap[place] = 0
		}

		if datesMap[date] == 0 {
			datesMap[date] = 0
		}

		placesMap[place] = placesMap[place] + 1
		datesMap[date] = datesMap[date] + 1

		// sort places
		// sort purchases
		for i, p := range orderedPurchases {
			if i+1 >= len(orderedPurchases) {
				continue // do nothing
			}
			next := orderedPurchases[i+1]
			if next > p {
				orderedPurchases[i] = next
				orderedPurchases[i+1] = p
			}
		}

		transactions = append(transactions, Transaction{
			Date:   dateObj,
			Place:  place,
			Amount: amount,
		})
	}

	avg := float64(sum / float64(len(transactions)-1))
	t := Transactions{
		Transactions:    transactions,
		Min:             min,
		Max:             max,
		Average:         avg,
		Places:          places,
		PlacesMap:       placesMap,
		DatesMap:        datesMap,
		Dates:           dates,
		Sum:             sum,
		NumTransactions: len(transactions) - 1,
	}

	// print quick stats
	fmt.Println("==>Num: ", t.NumTransactions)
	fmt.Println("==>Sum: ", t.Sum)
	fmt.Println("==>Max: ", t.Max)
	fmt.Println("==>Min: ", t.Min)
	fmt.Println("==>Avg: ", t.Average)

	// uncomment to print ordered purchases
	for _, p := range orderedPurchases {
		fmt.Println(p)
	}

	// uncomment to print where money is being spent
	// print other stats
	// fmt.Println("==>Places:<==")
	// for place, count := range t.PlacesMap {
	// fmt.Println(place, ": ", count)
	// }

	file.Close()
}
