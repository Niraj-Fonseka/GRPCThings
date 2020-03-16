package main

import (
	"fmt"
	"net/http"
)

func PingController(w http.ResponseWriter, r *http.Request) {
	greeting := "hello"

	response, err := PingService(greeting)

	if err != nil {
		fmt.Fprintf(w, fmt.Sprintf("ERROR : %s", err.Error()))
	}
	fmt.Fprintf(w, fmt.Sprintf("GRPC Server said : %s", response.Greeting))
}
