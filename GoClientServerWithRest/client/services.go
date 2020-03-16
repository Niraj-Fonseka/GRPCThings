package main

import (
	"GRPCThings/GoClientServerWithRest/api"
	"context"
)

func PingService(greeting string) (*api.PingMessage, error) {
	return Client.SayHello(context.Background(), &api.PingMessage{Greeting: greeting})
}
