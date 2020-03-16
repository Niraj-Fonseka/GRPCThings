package main

import (
	"log"

	"google.golang.org/grpc"
)

func EstablishGRPCServerConnection() *grpc.ClientConn {
	log.Println("Establishing connection with the grpc server..")
	conn, err := grpc.Dial(":7777", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %s", err)
	}
	return conn
}
