# Task2
This task is implementation of RESTapi. By using of this, user can get status of the droneport. 
This package requires the packages of `flask`, `flask_basicauth`, `requests`. 
## api.py
This script randomly generates Json status string and publish this information over "0.0.0.0" over port number "5000". 
To get the json status string, user needs to send `get` request to api. 
**Username**: droneport <br/>
**Password**: password <br/>  
To run the  script <br> 
`export FLASK_APP=api.py` <br>
`flask run` 
## test.py
This is a test script, basically sends get request to api and print the status on the console. <br> 
To run the  script <br> 
`python ./test.py`