
const { AddRequest, AddResponse, FibonacciRequest, FibonacciResponse } = require("./calculator_pb")
const { CalculatorClient } = require("./calculator_grpc_web_pb")
var client = new CalculatorClient('http://localhost:8080');

var request = new AddRequest()

request.setNum1(2)
request.setNum2(3)

client.add(request, {}, (err, response) => {
    console.log("Result of Add : ",response.getResult())
})


var fibRequest = new FibonacciRequest()
fibRequest.setCount(5)

var stream = client.fibonacci(fibRequest, {})


stream.on('data', function (response) {
    console.log("Fibonacci No : ",response.getNumber());
})