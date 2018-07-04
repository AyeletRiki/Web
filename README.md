# Web Project

Rivka Fishman - 205589377
Ayelet Ehrman - 315311860

* Project runs on python 2.7

* Install needed packages:

    pip install unittest2

    pip install flask
    
    pip install configparser
    
    pip install requests

* Install curl (Windows): https://skanthak.homepage.t-online.de/download/curl-7.60.0.cab

1. Calculator Function:

	Located in web_calculator.py
	
2. Unit Tests:

	Run - python tests/unit_test.py

3. Git:

	You can find our git repsetory here: https://github.com/AyeletRiki/Web 

4. Web Server:
	
	We built the server using Flask web framwork.
	Run - python server.py

5. Integration Tests:
	
	Run - python tests/integration_test.py

6. Docker:
	
	We are working on Windows so we installed Docker for Windows.
	Next, we wrote a Dockerfile located in the main root directory of the project.
	In order to build the calculator server Docker we run the command: docker build . -t currency-calculator.
	In order to run the server we run the command: docker run -p 3000:3000 currency-calculator.
	Now calculator server Docker is up and we can address him, for that we need to know the ip of our computer.
	We run ipconfig and extract the ip from there and then send our request to <ip>:3000 like that:
	curl http://<ip>:3000/calculate -X POST -H "Content-Type:application/json" -d "{\"calculatorState\":null,\"input\":\"1\"}".
	
7. Docker Compose:

	In order to run all the microservices together run - docker-compose up.

