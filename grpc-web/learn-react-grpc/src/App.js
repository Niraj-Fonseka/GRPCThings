import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';

const { AddRequest, AddResponse, FibonacciRequest, FibonacciResponse } = require("./calculator_pb")
const { CalculatorClient } = require("./calculator_grpc_web_pb")
var client = new CalculatorClient('http://localhost:8080');


function App() {

  const [count,setCount] = useState(0);
  
  const callGrpcService = () => {
    var fibRequest = new FibonacciRequest()
    fibRequest.setCount(5)

    var stream = client.fibonacci(fibRequest, {})
   
    stream.on('data', function (response) {
      //console.log("Fibonacci No : ",response.getNumber());
      setCount(response.getNumber())
    });

  };

  useEffect(()=>{
   callGrpcService()
  })

  return (
    <div className="App">
      {count}
    </div>
  );
}

export default App;
