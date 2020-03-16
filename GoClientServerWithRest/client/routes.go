package main

import "net/http"

func RegisterHandlers() {
	http.HandleFunc("/greeting", PingController)
}
