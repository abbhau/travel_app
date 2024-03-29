Project's Title : Travel_App

Project Description : This project gives all information about the famous travelling places.

How to Install and Run the Project:
1) create a virtual enviornment in your local repository and activate it 
    create : virtuaenv venv
    activate : venv\scripts\activate

2) Clone the project respository to your local repository
    git clone https://github.com/abbhau/travel_app.git

3) change directory by using command : cd travel_app


4) install all the dependencies required to the project
    pip install -r requirements.txt

5) run the migrate command to create an sqlite database
    py manage.py migrate

6) run the server by using command
   py manage.py runserver

To run the unit and Api test run command
    python manage.py test

To check postman Api collection or to Test all api 
   Open postman tool and import travel_app.postman_collection.json file which is present in destination app 

    

  
