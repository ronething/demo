// author: ashing
// time: 2020/4/12 12:19 下午
// mail: axingfly@gmail.com
// Less is more.

package main

import (
	"flag"
	"fmt"
	"math"
	"os"
	"strconv"
)

func str2float(s string) float64 {
	f, _ := strconv.ParseFloat(s, 64)
	return f
}

func calcSample(a, b float64) {
	c := (a * math.Pow10(6)) / (14.3 * 1000 * math.Pow(b, 2))
	c = str2float(fmt.Sprintf("%.3f", c))
	fmt.Printf("(a * 10^6) / (14.3 * 1000 * b^2) = %.3f\n", c)
	d := 1 - math.Sqrt(1-2*c)
	d = str2float(fmt.Sprintf("%.3f", d))
	fmt.Printf("1 - sqrt(1 - 2 * c) = %.3f\n", d)
	e := 1 - 0.5*d
	e = str2float(fmt.Sprintf("%.3f", e))
	fmt.Printf("1 - 0.5 * d = %.3f\n", e)
	f := (a * math.Pow10(6)) / (360 * e * b)
	fmt.Printf("(a * 10^6) / (360 * e * b) = %.0f\n", f)
}

var (
	h bool
	a float64
	b float64
)

func init() {
	flag.BoolVar(&h, "h", false, "usage help")

	flag.Float64Var(&a, "a", 0, "value a")
	flag.Float64Var(&b, "b", 0, "value b")

	flag.Usage = usage
}

func usage() {
	fmt.Fprintf(os.Stderr, `calc sample: version 0.1
Usage: calc -a 2.5 -b 60 
`)
	flag.PrintDefaults()
}

func main() {
	flag.Parse()

	if h || (a == 0 && b == 0) {
		flag.Usage()
	} else {
		calcSample(a, b)
	}

}
