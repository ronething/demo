// author: ashing
// time: 2020/3/28 11:49 上午
// mail: https://blog.ronething.cn
// Less is more.

package main

import (
	"fmt"
	"net/http"

	"github.com/ronething/gee"
)

func main() {
	g := gee.New()
	g.GET("/", func(w http.ResponseWriter, r *http.Request) {
		for k, v := range r.Header {
			fmt.Fprintf(w, "Header[%q] = %q\n", k, v)
		}
	})
	g.POST("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "post method\n")
	})

	g.Run("127.0.0.1:9998")
}
