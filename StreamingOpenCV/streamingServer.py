from concurrent import futures
import time
import datetime
import numpy as np 
import cv2 

import logging

import grpc

import api_pb2
import api_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)


class Pinger(api_pb2_grpc.PingServicer):

    def SayHello(self, request_iterator, context):
        print("In SayHello here")
        message = 'Hello !' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # while True:
        #     print("Iteration")
        #     time.sleep(3)
        #     yield api_pb2.PingMessage(greeting=message)
        #     message = 'Hello !' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #     print("Message : " , message)
        while(True):
            ret , frame = cap.read()

            gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray , scaleFactor=1.5 , minNeighbors=5)

            for ( x , y , w , h) in faces:
                print(x , y , w , h)
                message = "x : " + str(x) + ", y : " + str(y) + ", w : " + str(w) + ", h : " + str(h)
                # roi_gray = gray[y:y+h , x:x+w]
                # roi_color = frame[y:y+h , x:x+w]
                # img_item = "my-image.png"
                # cv2.imwrite(img_item,roi_gray)

                # color = (255, 0 , 0) #BGR
                # stroke = 2 
                # end_cord_x = x + w
                # end_cord_y = y + h 
                # cv2.rectangle(frame,(x,y) , (end_cord_x , end_cord_y) , color,stroke)
                yield api_pb2.PingMessage(greeting=message)



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    api_pb2_grpc.add_PingServicer_to_server(Pinger(), server)
    server.add_insecure_port('[::]:7777')
    print("Server Listening")
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()

    serve()