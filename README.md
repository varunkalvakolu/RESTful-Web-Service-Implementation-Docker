# RESTful-web-service using DOCKER container

Created a Python RESTful services using Flask and use docker to run this application.                              
First, docker need to be installed. Link: https://docs.docker.com/toolbox/toolbox_install_mac/                  
once docker installed we can see docker quick terminal on our system

 Steps
1. Get inside the app folder in terminal                          

2. Build the docker image:                                           

      ```bash
      docker build -t Airlines-sample .
      ```
3. once the docker image is created, run the "flask-test-sample" in docker container                                                            
      ```bash
      docker run -d -p 5000:5000 Airlines-sample
      ```
4.Now, app will run locally. i.e, if it is run on normal terminal, address will be localhost else docker ip address.                   
  1)GET request1: Go to http://192.168.99.100:5000/getairlines/  to list all details of passengers.                               
  2)GET request2: Go to http://192.168.99.100:5000/getairlines/1/ for specific customer with id "1" (example: 1)         
  3)GET request3: Go to http://192.168.99.100:5000/getairlines/gate/A2/ to find how many customers are present on specific gate "A2".
               
  

