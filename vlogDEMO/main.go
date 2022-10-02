package main

import (
	"crypto/md5"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"path/filepath"
	"strings"
	"time"
)

// output helloworld

func sayHello(w http.ResponseWriter, r *http.Request) {
	fmt.Println("path", r.URL.Path)
	w.Write([]byte("hello world"))

}

func main() {
	// 注册进 servermux 就是将不同 url 的请求交给对应的 handler
	http.HandleFunc("/sayHello", sayHello)

	// 获取 vlog 接口 fileHandler 是一个 handler
	fileHandler := http.FileServer(http.Dir("./video"))

	http.Handle("/video/", http.StripPrefix("/video/", fileHandler))

	// 上传 vlog 接口
	http.HandleFunc("/api/upload", uploadHandler)

	// 获取 vlog 视频列表
	http.HandleFunc("/api/list", getFileListHandler)

	// 启动 web 服务
	err := http.ListenAndServe(":9090", nil)
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}
}

// 1.业务逻辑 uploadHandler 是一个 handler func
func uploadHandler(w http.ResponseWriter, r *http.Request) {

	// 解决跨域访问限制问题
	w.Header().Set("Access-Control-Allow-Origin", "*")

	// 1.限制客户端上传视频文件的大小
	r.Body = http.MaxBytesReader(w, r.Body, 10*1024*1024)
	err := r.ParseMultipartForm(10 * 24 * 24)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// 2.获取上传文件
	file, fileHeader, err := r.FormFile("uploadFile")

	// 3.检查文件类型
	ret := strings.HasSuffix(fileHeader.Filename, ".mp4")
	if ret == false {
		http.Error(w, "not mp4", http.StatusInternalServerError)
		return
	}

	// 4. 获取随机名称
	md5Byte := md5.Sum([]byte(fileHeader.Filename + time.Now().String()))
	md5Str := fmt.Sprintf("%x", md5Byte)
	newFileName := md5Str + ".mp4"

	// 5.写入文件
	dst, err := os.Create("./video/" + newFileName)
	defer dst.Close() // 延迟关闭资源
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer file.Close()
	if _, err := io.Copy(dst, file); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

}

// 获取视频文件列表

func getFileListHandler(w http.ResponseWriter, r *http.Request) {
	files, _ := filepath.Glob("video/*.mp4")
	var ret []string
	for _, file := range files {
		ret = append(ret, "http://"+r.Host+"/video/"+filepath.Base(file))
	}
	retJson, _ := json.Marshal(ret)

	// 解决跨域访问限制问题
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Write(retJson)

	return

}
