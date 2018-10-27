# to run app directly:
pre-requirements: 
  - python2.7
  - flask
  - flask_restfull
  - requests

1. clone reposetory
2. run:
      python app.py --local_port=<local port> --remote_address=<http://remote-add:remote-port>

# to run app using docker:
pre-requirements: 
  - docker
  
1. clone reposetory
2. build docker image:
    sudo docker build -t <image-name> .
3. run docker image:
    sudo docker run -p <local-post>:<docker-port> <image-name> --local_port=<local-port> --remote_address=<http://remote-address:remote-port>
    
# to run tests:
pre-requirements: 
  - two app.py running instances
  - python 2.7
  - requests
  
1. clone reposetory
2. run:
      test.py --url1=<http://remote-address1:remote-port1> --url2=<http://remote-address2:remote-port2>
