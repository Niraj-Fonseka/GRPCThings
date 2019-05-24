package main

import (
	"log"
	"fmt"
	"time"
	"io"

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

	//ping := &api.PingMessage{Greeting: "foo"}

	go func() {
		for {
			in, err := stream.Recv()
			if err == io.EOF {
				fmt.Println("ENDDD")
			}
			log.Printf("Message Recivbed : %s \n", in.Greeting)
			time.Sleep( 5 * time.Second)
			
			}
	}()
	<-waitc
	stream.CloseSend()

	
}



