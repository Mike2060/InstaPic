import pymysql
from flask import Flask, render_template, request, redirect, url_for, session
import re
import os

# def check_duplicated (username)
def loadCardList(username = ""):
    db = initDB()
    try:
        with db.cursor() as cursor:
            # check db connection
            if cursor.connection :
                print ( "connect success" )
            if username == "":
                sql = f"SELECT imageID,extention,content FROM images ORDER BY time DESC"
            else:
                sql = f"SELECT imageID, extention,content FROM images WHERE username = '{username}' ORDER BY time ASC"
            cursor.execute(sql)
            result = cursor.fetchall() #return all records
            return result
    except Exception as e:
        return str(e)
    finally :
        db.close()

def upLoadImage(username, content, extention):
    db = initDB()
    try:
        with db.cursor() as cursor:
            # check db connection
            if cursor.connection :
                print ( "connect success" )
            sql = f"INSERT INTO images (imageID,content,username,extention) VALUES (UNIX_TIMESTAMP(CURRENT_TIMESTAMP),'{content}','{username}','{extention}')"
            cursor.execute(sql)
            db.commit()
            # search for the imageID just generated as the filename
            sql = "SELECT imageID FROM images where id=(SELECT LAST_INSERT_ID())"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
    except Exception as e:
        return str(e)
    finally :
        db.close()


def regNewAccount(username, password):
    db = initDB()
    try :
        with db.cursor() as cursor:
            # check db connection
            if cursor.connection :
                print ( "connect success" )
            # check for existed username
            sql = f"SELECT * FROM accounts WHERE username = '{username}'"
            account = cursor.execute(sql)
            if account:
                return "The username has been registered"
            # check for regular username --> with alphabatic and numerical value only
            elif not username.isalnum():
                return "Username must only contain characters and numbers"
            else:
                sql = f"INSERT INTO `accounts` (`imageID`, `password`, `username`) VALUES (UNIX_TIMESTAMP(CURRENT_TIMESTAMP),'{password}', '{username}')"
                cursor.execute(sql)
                db.commit()
                # setting for the session
                session['loggedin'] = True
                session['username'] = username
                return 'login success'
    except Exception as e:
        return str(e)
    finally :
        db.close()

def login (username, password):
    db = initDB()
    try :
        with db.cursor() as cursor:
            # check db connection
            if cursor.connection :
                print ( "connect success" )
            sql = f"SELECT * FROM accounts WHERE username = '{username}' AND password = '{password}'"
            cursor.execute(sql) # return 1 if success
            account = cursor.fetchone()
            if account:
                session['loggedin'] = True
                session['username'] = username
                return 'login success'
            else:
                return 'Wrong username or password'
    except Exception as e:
        return str(e)
    finally :
        db.close()

# def loggout ()

def initDB():
    connection = pymysql.connect(
    # host = os.environ.get('CLEARDB_DATABASE_HOST'),
    host = 'localhost',
    # user = os.environ.get('CLEARDB_DATABASE_USER'),
    user = 'root',
    # password = os.environ.get('CLEARDB_DATABASE_PASSWORD'),
    password = 'mike2060',
    # db = os.environ.get('CLEARDB_DATABASE_DB')
    db = 'heroku_5a73ef4f1809026'
    )
    return connection
