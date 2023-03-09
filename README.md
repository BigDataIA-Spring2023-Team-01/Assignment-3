# Assignment-3
#Hosted on AWS EC2

Streamlit - http://ec2-52-45-166-0.compute-1.amazonaws.com:8501/

FastAPI Docs - http://ec2-52-45-166-0.compute-1.amazonaws.com:8080/docs#/

AWS Report - https://greatexpectationsteam01.s3.amazonaws.com/index.html

Refrence:

## api folder /api
This folder contains all the api method functions and their respective functional dependencies. They are named as per the functionality - for example: api/metadata_geos.py - contains the api methods for extracting metadata from the Public aws geos bucket to a database.

## data folder /data
This contains all the database file and csv files.

## sql folder /sql
This folder contains all the sql scripts that are being used in this application.

## streamlit /streamlit
This contains all the streamlit pages and use the api calls from /api folder to do any task.

# How to Run
1. Open terminal
2. Browse the location where you want to clone the repository
3. Write the following command and press enter 
````
  git clone https://github.com/BigDataIA-Spring2023-Team-01/Assignment-2.git
 ````
 4. Create a virtual environment using the following command
 ````
  python -m venv <Virtual_environment_name>
 ````
 5. Activate the virtual environment and download the requirements.txt using
 ````
  pip install -r /path/to/requirements.txt
 ````
6. User docker compose to run both FastAPI and Streamlit containers.
 ````
  docker compose up -d --build
 ````
 link to documentation: https://codelabs-preview.appspot.com/?file_id=1WeY9z0c7sudPQ1AYpLt4cTWWUyIIraKTsfUFj3M1DmY#0
 ## Declaration 
 Contribution 
 
 1. Anandita Deb : 25%
 2. Cheril Yogi :25%
 3. Shamin Chokshi :25%
 4. Thejas Bharadwaj :25%
 
 WE ATTEST THAT WE HAVEN'T USED ANY OTHER STUDENT'S WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK.
