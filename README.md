# FormBuilder
# FormBuilder Application

A Django app that allows you to create surveys and share it to collect data.

## Setup

Clone the github repository and navigate to the project folder.
```
$ git clone https://github.com/nidhi3110/FormBuilder.git
$ cd FormBuilder
```


Install the dependencies present in the requirements.txt
```
(env)$ pip install -r requirements.txt
```

Create a virtual environment and activate it.
```
$ pipenv shell
```

Once the dependencies are installed, move inside the project folder and run the following commands.
```
$ cd FormBuilder
$ python manage.py makemigrations
$ python manage.py migrate

```

This will intialise the database and start the server. Head over to the below link to start navigating the app.
 > http://127.0.0.1:8000/

## Walkthrough

### Landing Page

As soon as you open the app, in order to create surveys and share them, you will be required to signup on the portal.
An existing user can login through this page

### Home Page

Once logged in, the app takes you to a homepage where you can see your existing surveys and an option to view the statistics associated with that form.
The page also provides a **CREATE** option to create a new survey.
A logout button is also provided.

Please note that the app uses an internal authentication and a request by any unregistered user trying to access the page is put down.  

### Create Survey

On this Page, you can set the title and the description of the survey you want to create.
Press the submit button to create a survey.
A dialogue box pops up with a success message and the link of the survey which can be shared among other people, of whom you want to collect data.

### Survey Page

This is the page where anyone can come and submit their response. The form owner can share the form url among anyone, of whom he wishes to collect data of.

### Statistics

This page is only accessible to the form owner. It gives information to the SurveyOwner about all the responses collected thorugh his survey. 

## Admin

The admin page provides an interface for the superuser to perform CRUD operations over the app. He has the functionality to modify/create/delete any data (be it users or surveys or survey data) from the DB.


Admin can be accessed suing the following link.
 > http://127.0.0.1:8000/admin

