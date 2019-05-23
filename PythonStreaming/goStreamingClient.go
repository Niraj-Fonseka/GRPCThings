package main

import (
	"log"
	"time"

	"golang.org/x/net/context"
	"google.golang.org/grpc"

	api "GRPCThings/PythonStreaming/api"
)

func main() {
	var conn *grpc.ClientConn

	conn, err := grpc.Dial(":7777", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %s", err)
	}
	defer conn.Close()

	c := api.NewPingClient(conn)
	stream, err := c.SayHello(context.Background())

	waitc := make(chan struct{})

	ping := &api.PingMessage{Greeting: "foo"}

	go func() {
		for {
			log.Println("Sleeping...")
			time.Sleep(2 * time.Second)
			log.Println("Sending msg...")
			stream.Send(ping)
		}
	}()
	<-waitc
	stream.CloseSend()

	
}
