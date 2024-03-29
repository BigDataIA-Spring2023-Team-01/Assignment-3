# Assignment-3
#Hosted on AWS EC2

Streamlit - http://ec2-44-211-9-40.compute-1.amazonaws.com:8501/

FastAPI Docs - http://ec2-44-211-9-40.compute-1.amazonaws.com:8070/docs

AWS Report - https://greatexpectationsteam01.s3.amazonaws.com/index.html

Refrence:

## airflow folder /airflow
This folder contains all the airflow related data and logs.

## api folder /api
This folder contains all the api method functions and their respective functional dependencies. They are named as per the functionality - for example: api/metadata_geos.py - contains the api methods for extracting metadata from the Public aws geos bucket to a database.

## data folder /data
This contains all the database file and csv files.

## cli folder /cli
This contains files related to the CLI

## sql folder /sql
This folder contains all the sql scripts that are being used in this application.

## streamlit /streamlit
This contains all the streamlit pages and use the api calls from /api folder to do any task.

## great_expectations folder /great_expectations
This folder contains all the reports for the great expectations and the expectation suite.

## logs folder /logs
This contains the 'app.log' file which contains all the logs of the fastapi.



# How to Run
1. Open terminal
2. Browse the location where you want to clone the repository
3. Write the following command and press enter 
````
  git clone https://github.com/BigDataIA-Spring2023-Team-01/Assignment-3.git
 ````
 4. Create a virtual environment using the following command
 ````
  python -m venv <Virtual_environment_name>
 ````
 5. Activate the virtual environment and download the requirements.txt using
 ````
  pip install -r /path/to/requirements.txt
 ````
6. Create a .env file inside the main directory /Assignment-3 and ppoulate the below fields
 ````
  AIRFLOW_UID= <The UID of the server of airflow>
  AIRFLOW_PROJ_DIR=<Base Directory of Airflow. For example ./airflow>
  AWS_ACCESS_KEY = <Your AWS_ACCESS_KEY>
  AWS_SECRET_KEY = <Your AWS_SECRET_KEY>
  USER_BUCKET_NAME = team01
  URL = <URL of the FASTAPI application>
  SECRET_KEY = <SECRET_KEY used to hash the token>

 ````
7. User docker compose to run both FastAPI and Streamlit containers.
````
docker compose up -d --build
````


# How to Run CLI commands
1. Open terminal
2. Go to the directory of /cli
Note: For now we need to add the JWT token needed to access the endpoints manually. So in the cli/cli/goesNexrad.py file, in line number 10 add the JWT Token that is created when we login to the streamlit application or you can generate the token by accessing the fastapi website linked above. 
  2.1 Go to http://ec2-44-211-9-40.compute-1.amazonaws.com:8070/docs and use the /token endpoint.
  2.2 Pass the username and password as user_free and test respectively
  2.3 Token is generated and returned as response in response header.
  2.4 Copy that token from there and add it to cli/cli/goesNexrad.py file at line number 10.
  2.5 Continue the rest

3. Write the following command and press enter
 ````
python setup.py bdist_wheel
  ````
  
 ````
  pip install .
 ````
4. This will install the CLI package in local and you can now run cli commands using 'goesNexrad'.
5. The following commands are available through this

 create-user                         Create a new user.                                                                                   
 downloadbyfilename                  Download a file by name.                                                                                
 fetchcoordinates                    List all coordinates of the nexrad sattelited locations.                                                
 fetchgoes                           List all files in a bucket with the given prefix.                                                       
 fetchnexrad                         List all files in a bucket with the given prefix.         
 
6. Execute them like following: 
  
 ````
  goesNexrad create-user
 ````

This will prompt the user to enter the required parameters via prompt.

 link to documentation: https://codelabs-preview.appspot.com/?file_id=1WeY9z0c7sudPQ1AYpLt4cTWWUyIIraKTsfUFj3M1DmY#0
 ## Declaration 
 Contribution 
 
 
 1. Anandita Deb : 25%
 2. Cheril Yogi :25%
 3. Shamin Chokshi :25%
 4. Thejas Bharadwaj :25%
 
 WE ATTEST THAT WE HAVEN'T USED ANY OTHER STUDENT'S WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK.
