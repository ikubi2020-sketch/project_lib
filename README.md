
running rules

the container is :::::   docker run --name library_db  -e MYSQL_ROOT_PASSWORD=1313  -e MYSQL_DATABASE=library_db  -p 3306:3306  -v library_db_data:/var/lib/mysql  -d mysql:latest

git clone 
https://github.com/ikubi2020-sketch/project_lib.git

pip install -r requirements.txt 

notice code mysql : 1313 :


description  

the prepuce of this program is to manege a library  with 2 sides . 1 is the books , in there we will manege in all books details such as name, author and more  (in the tables to follow ) to give us the exact state of every book , second part is managing the members and theres state 
all of this will be inn a local database which will be connected to the code where details can be altered .
the code will run an api which allow user to give a request from the internet completing the system  

database details 

database library_db contain 2 tables. 1: books . columns in it as follow 
1:  id = primary key, auto_increment 
2: title = author varchar(50) not null 
3: genre = must be in (fiction | non_fiction | science | history | other) not null
4: is_available = boolean if book is available ,  not null
5 : total_borrow = not null
6: borrowed_by_member_id =  hold who is holding the book

table 2 members 
1 : id =  primary key, auto_increment 
2: name = hold a  member name varchar(50) not null
3: email = hold a  member email , unique
4: is active = boolean , hold if member is active , if not true member cant borrow not null 
5: total_borrows = count how many books member is having , not null

files structure 

library-api is holding all the project 
main is the center where the api is ruining and data exception will be cached 
readme is this file holding all the description 
.gitignore and requirements.txt are for git and all versions in the project

directory database is responsible  to interact with the database
db_connection.py hold the connection to database in a class
book_db.py hold class with function to alter the books table
member_db.py hold class with function to alter the members table  

directory logs hold the logging setting file and the logger itself 

directory routers hold different files holding deferent routers
one for all books one for all members and one to get reports 

file .vscode is an extension that contain miss spelled words (a.k.a. not relevant) 

library-api/ 
│ 
│ 
├── main.py 
├── database/ 
│   ├── db_connection.py 
│   ├── book_db.py 
│   └── member_db.py 
├── routes/ 
│   ├── book_routes.py 
│   ├── member_routes.py 
│   └── report_routes.py 
├── logs/ 
│   └── app.log 
│ 
├── README.md 
├── requirements.txt 
└── .gitignore 

endpoints books

POST /books  ::: create a book and put it in the DB 
GET /books   ::: return all book list 
GET /books/{id} ::: return one book by ID 
PUT /books/{id} ::: update one field 
PUT /books/{id}/return/{member_id} ::: update  is_available and  borrowed_by_member_id
PUT /books/{id}/borrow/{member_id} ::: revers  the earle functions
GET /reports/summary ::: return count of all books in the DB 
GET /reports/summary  ::: count all available books 
GET /reports/summary ::: count all unavailable  books
PUT /books/{id}/borrow/{member_id}  ::: count how many books the member hold in this moment 


endpoints members 

POST /members  ::: add a member 
GET /members :::  return all members
GET /members/{id}  ::: get one member by ID 
PUT /members/{id} ::: update a member details 
PUT /members/{id}/deactivate  ::: turn is_active to false 
PUT /members/{id}/activate :::: turn is_active to True 
PUT /books/{id}/borrow/{member_id}  ::: get count books borrowed by 1
GET /reports/summary ::: count all active members 
GET /reports/top-member :::  return  member with the highest borrowed 

system run processes

database  with all previous details are in existence 
and and API serves is standing whiting to a request 
as soon as a request comes throw the right  place  the request will 
be sent to the right class/function that will go to the database to get 
the required information or or update to right field doing  this process every action will by written in the logs file 
when the request will be done with success or failure  the user and the logs will get respond of result


