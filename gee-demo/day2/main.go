// author: ashing
// time: 2020/3/28 3:45 下午
// mail: https://blog.ronething.cn
// Less is more.

package main

import (
	"net/http"

	"github.com/ronething/gee"
)

func main() {
	g := gee.New()
	g.GET("/", func(c *gee.Context) {
		c.HTML(http.StatusOK, "<h1>Hello World</h1>")
	})

	g.GET("/hello", func(c *gee.Context) {
		// /hello?name=panda
		c.String(http.StatusOK, "hello %s, you're at %s\n", c.Query("name"), c.Path)
	})

	g.POST("/login", func(c *gee.Context) {
		c.JSON(http.StatusOK, gee.H{
			"username": c.PostForm("username"),
			"password": c.PostForm("password"),
		})
	})

	g.Run("127.0.0.1:9998")

}
