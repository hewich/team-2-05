# Task Organizer CMPE 131

## Project Description

This task organizer is a website that requires users to sign in with a first name, last name, email and create a user name and password. Once this is done the user is allowed to add task, remove task, organize and view task.

## Instructions in how to run the app using pycharm
To run the app go to myrunapp.py and press on the terminal 
* Running on http://...../  

## Requirements: 

Click==7.0
Flask==1.1.1
Flask-SQLAlchemy==2.4.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
SQLAlchemy==1.3.10
Werkzeug==0.16.0


## Features Description 

Features:

1. Log In: Login is a set of proofs used to authenticate a registered user. Once is clicked you would be sent to the Register page. 
2. Log Out: Logging out informs the computer or website that the current user wishes to end the login session.
3. Register: The register page consist of a couple of credentials such as name, lastname, email, username and password to authenticate a new user. 
4. CSS: The CSS page includes the colors, layout and fonts of this webpage.
5. Add: Let user write and save a task. 
6. Remove: User is allowed to remove saved task.
7. View: Create a copy of the added task. 
8. Organize: Organize the task name alphabically.

## File location of test cases and how to run them

Use case 1 and 2: 
Sign In/Registration
Inside of myapp folder we can find the all the necesary tabs such as  __init__.py, forms.py, models.py, routes.py necesary for the functionality of the database with the Registration and Sign In page. Also, inside of the folder named tamplate we can find a home.html file where the sign in buttom is located and the register.html file where the register page is located. 

Use case 3:
Add Task
Inside of myapp folder we can find the all the necesary tabs such as  __init__.py, forms.py, models.py, routes.py necesary for the functionality of the database with the add task function. Also, inside of the folder named tamplate we can find the file add.html that allowed us to add and save the task in the website.

Use case 4: 
Remove Task
Inside of myapp folder we can find the all the necesary tabs such as  __init__.py, forms.py, models.py, routes.py necesary for the functionality of the database with the Remove Task. Also, inside of the folder named templates we can find the file remove.html that allowed us to remove the previustly saved task in the website.

Use case 5: 
View Task
Inside of myapp folder we can find the all the necesary tabs such as  __init__.py, forms.py, models.py, routes.py necesary for the functionality of the database with the View Task.Also, inside of the folder named templates we can find the file view.html that allowed us to view the previustly added task. 

Use case 6:
Log Out 
Inside of myapp folder we can find the all the necesary tabs such as  __init__.py, forms.py, models.py, routes.py necesary for the functionality of the database with the Log Out. Since login and logout are connected the main necesary file is routes.py.

Use case 7:
Organize Task
Inside of myapp folder we can find the all the necesary tabs such as  __init__.py, forms.py, models.py, routes.py necesary for the functionality of the database with the Organize Task. Also, inside of the folder named templates we can find the file organize.html that allowed us to organize the task by alphabetical name. 






Futhermore, in another folder named static there is a file named style.css used for the esthetic of the webpage. 






