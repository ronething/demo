// author: ashing
// time: 2020/3/30 10:22 下午
// mail: https://blog.ronething.cn
// Less is more.

// 终端在 day6 目录使用 go run main.go

package main

import (
	"fmt"
	"html/template"
	"net/http"
	"time"

	"github.com/ronething/gee"
)

type student struct {
	Name string
	Age  int
}

func formatAsDate(t time.Time) string {
	year, month, day := t.Date()
	return fmt.Sprintf("%d-%02d-%02d", year, month, day)
}

func main() {
	g := gee.New()
	g.Use(gee.Logger())
	g.SetFuncMap(template.FuncMap{
		"formatAsDate": formatAsDate,
	})
	g.LoadHTMLGlob("templates/*")
	g.Static("/assets", "./static")

	stu1 := &student{Name: "Panda", Age: 20}
	stu2 := &student{Name: "Onething", Age: 22}
	g.GET("/", func(c *gee.Context) {
		c.HTML(http.StatusOK, "css.tmpl", nil)
	})
	g.GET("/students", func(c *gee.Context) {
		c.HTML(http.StatusOK, "arr.tmpl", gee.H{
			"title":  "gee",
			"stuArr": [2]*student{stu1, stu2},
		})
	})

	g.GET("/date", func(c *gee.Context) {
		c.HTML(http.StatusOK, "custom_func.tmpl", gee.H{
			"title": "gee",
			"now":   time.Date(2020, 3, 28, 2, 10, 0, 0, time.UTC),
		})
	})

	g.Run("127.0.0.1:9998")
}
