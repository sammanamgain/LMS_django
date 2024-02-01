
# Library Management System (API)

This is  backend for a library management system using Django .The system will include models representing books and library and users.It also have authentication features.To use the API, you need to be logged In.I  have used the mariadB which is similar to mysql
You can see all the API from this link:

https://api.postman.com/collections/25990226-5043580c-3904-451a-8615-fff2e2106cd1?access_key=PMAT-01HNJDD2APE1W2JZP1929KZC7H
## API Reference

#### Sign UP

```http
  POST /api/v1/signup
```
Description:To Sign up a new User(Librarian)
| Body | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Your User Name |
| `password` | `string` | **Required**. Your Password |

#### LogIn

```http
  POST /api/v1/login
```
Description:To get logged In
| Body | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Your User Name |
| `password` | `string` | **Required**. Your Password |

#### Register a student for Library 

```http
  POST /api/v1/user
```
Description:To register a student into library management system .membership date starts from the day of Registerd student
| Body | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Name` | `string` | **Required**. Your User Name |
| `Email` | `string` | **Required**. Email of student |

#### Register a Book

```http
  POST /api/v1/addbook
```
Description:To add the book in system
| Body | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `title` | `string` | **Required**.Title of  Book  |
| `isbn` | `string` | **Required**. ISBN |
| `published_date` | `string` | **Required**. Date  |
| `genre` | `string` | **Required**. GENRE|

#### Borrow a Book

```http
  POST /api/v1/borrow
```
Description:To borrow a book 
| Body | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `book_id` | `Number` | **Required**.Id of book that you want to borrow  |
| `user_id` | `Number` | **Required**. Id of student|

#### Add Book details

```http
  POST /api/v1/addbookdetails
```
Description:To add the book Description
| Body | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `book_id` | `Number` | **Required**.Id of book that you want to borrow  |
| `details_id` | `Number` | **Required**. Id |
| `Number of Pages` | `Number` | **Required**. Page Number |
| `Publisher` | `string` | **Required**. Publisher House |
| `Language` | `string` | **Required**. Book Language |


#### Get ALL BOOK DETAILS

```http
  GET /api/v1/book/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of Book to fetch |



#### Get ALL Borrowed Book 
Description:To get all the Description of who borrowed and corresponding Book details

```http
  GET /api/v1/getallborrow
```


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| ``      | `` | |

#### Get ALL  Book 
Description:To get all the information of Book present in system

```http
  GET /api/v1/allbook
```


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| ``      | `` | |



#### Deleting a borrow information 
Description:to remove the student from borrow table after he returns book

```http
  DELETE /api/v1/removeborrow
```

| Body | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `book_id` | `Number` | **Required**.Id of book that you want to return  |
| `user_id` | `Number` | **Required**. Id  of user|







## Documentation

[Documentation](https://linktodocumentation)


## Installation

Clone this Repository

```bash
  git clone https://github.com/sammanamgain/LMS_django
```
    

Setup the MariaDB server
Install the Database (mariaDB) according to your OS
start the server
setup a username and password 


Change this file according to your username and password
go to settings.py,change this according to your setting
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'LMS',
        'USER': 'your username',
        'PASSWORD': 'your password',
        'HOST': 'localhost',
        'PORT': '3306',  # Default MySQL/MariaDB port
    }
}
```


create a virtual enviornment using the following command


Install virtualenv (if not installed)
```bash
pip install virtualenv
```

```bash
virtualenv myenv
```

Activate the virtual environment
On Windows
```bash
myenv\Scripts\activate
```
On macOS or Linux
```bash
source myenv/bin/activate
```

Install the django
```bash
pip install django
```


## Running project

### Migration command
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```


#### For Home
```bash
python manage.py makemigrations Home
```
```bash
python manage.py migrate
```

### Running server
```bash
python manage.py runserver
```


# PRE-REQUISITES

python should be installed 
You need to sign Up to test the feature 
## FAQ

#### I have faced a issue while running the server

You can mail me with error at amgain02@gmail.com


