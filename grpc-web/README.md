https://medium.com/swlh/ditching-rest-with-grpc-web-and-envoy-bfaa89a39b32


### building client 

`npx webpack client.js`



### generate pb go 

`protoc protos/calculator.proto --go_out=plugins=grpc:./server/calculatorpb/`



### generate pb js 

`protoc protos/calculator.proto js_out=import_style=commonjs,binary:./client --grpc-web_out=import_style=commonjs,mode=grpcwebtext:./client`



### Serving the files 

`python3 -m http.server 8081`



### Building custom envoy image 

`docker build -t my-envoy:1.0 .`



### Running custom envoy image 

`docker run  -p 8080:8080 -p 9901:9901 --network=host my-envoy:1.0`