// author: ashing
// time: 2020/3/30 12:24 下午
// mail: https://blog.ronething.cn
// Less is more.

package gee

import (
	"log"
	"time"
)

func Logger() HandlerFunc {
	return func(c *Context) {
		// Start timer
		t := time.Now()
		// Process request
		c.Next()
		// Calculate resolution time
		log.Printf("[%d] %s in %v", c.StatusCode, c.Request.RequestURI, time.Since(t))
	}
}
