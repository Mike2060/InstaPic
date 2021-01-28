# InstaPic - Photo sharing web application
## Introduction
This project is about a image-sharing web app, InstaPic, which is mainly built by flask in Python with mysql database. There would several part explained in the following content

- Documentation of app execution
- Documentation of InstaPic API
- Documentation of automated testing

## Documentation of app execution
### Local testing
#### 1. Environment setting
For local testing, please use venv (pip module) to install the virtual environment on the project.
```
python3 -m venv <virtual_env_folder_name>
```
Then click activate the environment.
```
source <virtual_env_folder_name>/bin/activate
```
Install the required pip plugin
```
pip3 install flask
pip3 install requests
pip3 install pymysql
```
#### 2. config setting
Some of the config variable would need to be changed due to the environment difference between deployment enivornment and local environment.
In ``` db.py ```, ```initDB()``` database would need to change your own database setting

Original
```
def initDB():
    connection = pymysql.connect(
    host = os.environ.get('CLEARDB_DATABASE_HOST'),
    user = os.environ.get('CLEARDB_DATABASE_USER'),
    password = os.environ.get('CLEARDB_DATABASE_PASSWORD'),
    db = os.environ.get('CLEARDB_DATABASE_DB')
    )
    return connection
```
After
```
def initDB():
    connection = pymysql.connect(
    host = <host_name>,
    user = <user name>,
    password = <password>,
    db = <database used>
    )
    return connection
```
Also in at the ```___init___.py```, the ```UPLOAD_FOLDER``` variable need to change to the absolute path to the ```InstaPic/static/img/UserImage```
```
UPLOAD_FOLDER = <absolute path>
```
After that, you could start to run the server by running the ```wsgi.py```
```
python3 wsgi.py
```
### Heroku deployment
#### *** Notice: for real deployment , it's better use other services to deploy the app (E.g. Azure, Amazon,...) in order to have some persistent storage to store the image folder. For this testing, due to the lack of credit card , the account is not available for me to register. If use heroku for the production deployment, please connect to the AWS S3 service ,which is the persistent storage system. Otherwise, the image folder would be clear with certain time period and the uploaded image would be not able to show after a cycle (heroku would redeploy it)***

In this project, ```heroku``` is used to deploy the web application.

#### 1. Heroku registration and app creation
First you will need to register a heroku account and open an app on heroku.
#### 2. Download the heroku CLI
Follow the following tutor to install the herokuCLI
https://devcenter.heroku.com/articles/heroku-cli
#### 3. Login the heroku and add remote to git (The git of the git project of InstaPic)
Under the same git init directory, add the heroku master with the following command:
```
heroku git:remote -a <app name in heroku>
```
#### 4. ClearDB (Mysql) setting
Go to the heroku app portal, install the ClearDB as the add-ons of your app. After the installation of the ClearDB, on the terminal, use the following command to check the db configuration
```
heroku config
```
you would see the config of CLEARDB_DATABASE_URL, the information of the DB could be gained from the URL
```
mysql://<user name>:<password>@<host>/<database name>?.....
```
Go to the setting page of the app in heroku, add the configuration variable
```
CLEARDB_DATABASE_DB: <database name>
CLEARDB_DATABASE_HOST:  <host>
CLEARDB_DATABASE_PASSWORD: <password>
CLEARDB_DATABASE_USER: <username>
```
#### 5. Push and deploy
Use the following command to push the content to heroku master and deploy it
```
git push heroku master
```
## Documentation of InstaPic API
### 1. login()
#### Method: GET or POST
It is the basic login api that user would be redirected to if the user haven't login yet. When user send the username and password as login details to loggin the application,if the login is not successful (etc wrong password), error message would be shown under the login button. Otherwise, After successful login, user would redirect to index()

---
### 2. logout()
#### Method: GET or POST
User can use this to loggout, and the corresponding login session would be deleted

---
### 3. registration()
#### Method: GET or POST
User can use this to register a new account. If the registration is success, the page would redirect to index(). Otherwise if is fail (etc registered username), it would return to the registration page and show the error message.

---
### 4. index()
#### Method: GET
This would be the portal for user to see the uploaded images. If the user is not login yet and direct access this page, login() would be trigger and return the user to the login page.

---
### 5. search()
#### Method: GET or POST
This would allow user to search for the photo of specific users by entering specific username on the search.

---
### 6. upload
#### Method: GET or POST
This would allow user to get in the upload page if it is GET method. For the post method, user can upload the image and text to the server and the database, and this would return the user to the index()

## Documentation of the automated testing
In this project, ```unittest``` is used for the testing. For the testing content, it is stored under the ```/tests``` file. First please set the flask app environment varible to be main.py i.e.
```
export FLASK_APP=main.py
```
Then execute the following code to execute the testing
```
flask test
```
