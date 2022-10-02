package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main() {
	var r *gin.Engine
	r = gin.Default()
	r.Static("/asserts", "./asserts")
	r.StaticFS("/static", http.Dir("static"))
	r.StaticFile("/favicon.ico", "./favicon.ico")
	r.Run()
}
