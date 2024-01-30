# Library Management API
## Overview
This Django-based Library Management API allows you to manage books, user. It provides endpoints for CRUD operations on books, user, as well as features like borrowing and returning books.


## Installation

Create a virtual environment

```bash
python -m venv myenv
source myenv/bin/activate 
```

Install required packages 

```bash
pip install -r requirements.txt

```
Create a new Django project

```bash
django-admin startproject library_system
```

Navigate into the project directory

```bash
cd myproject
```
## API Reference
### User
#### Create new user

```http
POST "http://127.0.0.1:8000/api/users/create/"
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | **Required**. User Name |
| `email` | `string` | **Required**. Unique email address |
| `membership_date` | `date` | **Required**. Date when user joined |

#### Get User list

```http
GET "http://127.0.0.1:8000/api/users/list/"
```

#### Get Specific User 

```http
GET "http://127.0.0.1:8000/api/users/<id>"
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `uuid` | **Required**. User ID |

### Books
#### Add new book

```http
POST "http://127.0.0.1:8000/api/books/add/"
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `title` | `string` | **Required**. Book title |
| `isbn` | `string` | **Required**. ISBN of the book |
| `published_date` | `date` | **Required**. Published date |
| `genre` | `string` | **Required**. Genre of the book |

#### Get list of books

```http
GET "http://127.0.0.1:8000/api/books/list"
```
#### Get specific book 


```http
GET "http://127.0.0.1:8000/api/books/<id>"
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `uuid` | **Required**. Book ID |


#### Assign/Update Book Details


```http
POST "http://127.0.0.1:8000/api/books/details/"
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `book` | `uuid` | **Required**. Book ID |
| `number_of_pages` | `integer` | **Required**. Number of pages |
| `publisher` | `string` | **Required**. Publisher of the book |
| `language` | `string` | **Required**. Language of the book |

### BorrowedBook
#### Borrow Book

```http
POST "http://127.0.0.1:8000/api/borrow/"
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `user` | `uuid` | **Required**. User ID |
| `book` | `uuid` | **Required**. Book ID |
| `borrow_date` | `date` | **Required**. Date of borrow |



#### Return Book

```http
PUT "http://127.0.0.1:8000/api/return/<id>/"
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `uuid` | **Required**. Borrow ID |
| `return_date` | `date` | **Required**. Date of return |

#### List of Borrowed Books


```http
GET "http://127.0.0.1:8000/api/borrowed/list"
```
## Notes

Postman collection is also pushed in repository.

