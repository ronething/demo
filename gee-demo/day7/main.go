// author: ashing
// time: 2020/3/31 1:35 下午
// mail: https://blog.ronething.cn
// Less is more.

package main

import (
	"net/http"

	"github.com/ronething/gee"
)

func main() {
	g := gee.Default()
	g.GET("/", func(c *gee.Context) {
		c.String(http.StatusOK, "Hello Panda\n")
	})
	// index out of range for testing Recovery()
	g.GET("/panic", func(c *gee.Context) {
		names := []string{"panda"}
		c.String(http.StatusOK, names[100])
	})

	g.Run("127.0.0.1:9998")
}
