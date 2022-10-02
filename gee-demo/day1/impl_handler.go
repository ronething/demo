// author: ashing
// time: 2020/3/28 11:34 上午
// mail: https://blog.ronething.cn
// Less is more.

package main

import (
	"fmt"
	"log"
	"net/http"
)

type Engine struct {
}

func (e *Engine) ServeHTTP(w http.ResponseWriter, req *http.Request) {
	switch req.URL.Path {
	case "/":
		fmt.Fprintf(w, "URL.Path = %q\n", req.URL.Path)
	case "/hello":
		for k, v := range req.Header {
			fmt.Fprintf(w, "Header[%q] = %q\n", k, v)
		}
	default:
		fmt.Fprintf(w, "404 Not Found: %s\n", req.URL)
	}
}

func main() {
	e := new(Engine)
	log.Fatal(http.ListenAndServe("127.0.0.1:9999", e))
}
