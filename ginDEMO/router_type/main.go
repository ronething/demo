package main

import "github.com/gin-gonic/gin"

func main() {
	var r *gin.Engine
	r = gin.Default()
	r.GET("/get", func(c *gin.Context) {
		c.String(200, "get")
	})
	r.POST("/post", func(c *gin.Context) {
		c.String(200, "post")
	})
	r.Handle("DELETE", "/delete", func(c *gin.Context) {
		c.String(200, "delete")
	})
	r.Any("/any", func(c *gin.Context) {
		c.String(200, "any")
	})
	r.Run()
}
