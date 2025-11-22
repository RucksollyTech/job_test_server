Here I have two apps/packages

simple python package and a django + next js 

SIMPLE PYTHON PACKAGE

Job_test > my_web_socket

This is a simple websocket system with pure python

It includes the server(server.py), the client (client.py), requirements.txt  and test_compute_sum_numbers.py

It has a simple sever side function with two number inputs

It has a client-side async function that calls the server and prints the results

I also demostrated multiple calls

the requirements/dependencies can be seen in the folder job_test > my_web_socket > requirements.txt

to run the server part :
Navigate to my_web_socket directory and run

python3 -m server

Expected output:

WebSocket server is running on ws://localhost:8765

It listens on ws://localhost:8765

the message expect : 

Expected request (JSON):
        {
            "method": "compute_sum_numbers",
            "params": {"a": number, "b": number}
        }

response json
{
  "result": number
}


to run the client part :
Navigate to my_web_socket directory and run:

python3 -m client

the out put would be

compute_sum_numbers(1, 2) = 3
compute_sum_numbers(10, 20) = 30
compute_sum_numbers(-5, 15) = 10
compute_sum_numbers(3.5, 4.5) = 8.0

It contains a test_compute_sum_numbers.py for testing
To run this test simply navigate to my_web_socket directory and run:

pytest
---------------------------------------------------



Django application that runs on channels to provide a websocket behavior and I have modified the settings to use ASGI which is for websockets applications in django.

the routing is handled in the asgi.py.

the asycs > custom_func folder contains the consumer and common.py 

common.py contains common function that can be called.

In there I have compute_sum_numbers which sums up two numbers

requirements can be seen in the requirements.txt in the root folder (job_test > requirements.txt)


this can be started using daphne :
daphne job_test.asgi:application


For this section I also made a next js application to call on this with random values at https://github.com/RucksollyTech/job_test_client.git

The next js app can be started by running (before that make sure to run npm install)

npm run dev

Expected out put for this section can be seen on the client side next js 
