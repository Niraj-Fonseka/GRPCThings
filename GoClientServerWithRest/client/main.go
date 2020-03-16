package main

import (
	"GRPCThings/GoClientServerWithRest/api"
	"log"
	"net/http"

	"google.golang.org/grpc"
)

var ClientConn *grpc.ClientConn
var Client api.PingClient

func main() {
	log.Println("Starting Server")
	ClientConn = EstablishGRPCServerConnection()

	Client = api.NewPingClient(ClientConn)

	defer ClientConn.Close()
	RegisterHandlers()

	log.Println("Listening....")
	http.ListenAndServe(":8080", nil)
}
