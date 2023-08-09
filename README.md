# Whiplash Test Result Database

## Description:
In this project a web based application is created using Flask framework which is intended for gathering the result data
gained from EuroNCAP Whiplash physical testing for specific car seat model.
It helps engineers to store and study neck injury criteria during the reat impact.
The users may document the details regarding car seat version and record test result set for specified hardware test
conducted.

## Features:
+ user register to access the application. Authentication process is done by email and password.
+ Seat version register
+ Test and result values register
+ Coloring of cells in the overview table based on result values, bottom limit and upper limit

## How to use:
Install required packages by:
+ pip install -r requirements.txt

Set a database type and filename in app.py:
+ edit: app.config['SQLALCHEMY_DATABASE_URI']  

Use bash terminal and proceed with following commands to establish database and load table of available crash pulses
of different severity - Low, Medium, High:
+ python
+ from app import db
+ from app import create_db
+ from app import load_pulses
+ create_db()
+ load_pulses()
+ flask run 


