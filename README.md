## Go Rest

Pytest project to automate REST API calls on Go Rest page. Only some test cases are implemented.

1. One can use pytest for automation
Pytest allows the usage of fixtures to setup and teardown specific conditions necessary for the test case/suite. One can run tests with or without token (reduced scope). Fixtures for skiping tests that require authentication can be implemented in case token is missing (check code).

2. Aplication supports the following actions:
* Get a list with all users information
* Get, update and delete a user (info)
* Get a list of all posts or comments of an user
* User create a post or todo
* Get a list of posts of all users
* Get, update and delete a post
* Create a comment on a post
* Get a list of comments from all posts
* Get, update, and delete a comment on a post
* Get a list of todos for all the users
* Get, update, and delete an user's todo

3.
3.1. Check code
3.2. Not all todos are completed (check report)
3.3. The "due_on" value represents the date at which the todo must be completed. It is in a year-month-dayThour:minute:second format. +05:30 represents the time zone of the server (hosted in India, therefore +05:30 relatively to GMT)

4.
4.1. The API is a public facing API. Moreover, get requests can be submited without authentication. Both factors can expose the interface to extensive usage at certain times. It is threfore relevant to ensure that the system remains responsive and can execute the tasks even during those periods. Jmeter is a tool that allows to setup multiple threads and subimt requests in parallel as if multiplle users were using the API. One can incrementally increase the number of threads, assess the time the server takes to fulfil the requests and determine if it is properly dimentioned for the expected load (by checking the occurence of errors).
4.2. The continuous testing can be divided into functional and LSP testing. Both types of automated tests could run through a Jenkins job (either daily - cronjob - or whenever there are changes on the code - polling a repository). For the functional tests, a customized docker image could be created where python modules are installed as dependencies and where the contents of the repo (incluiding tests, lib, environment file and conftest) are copied into the container filesystem. The commands to run pytest can the specified alongside the docker run in jenkins shell.
For LSP testing, 2 containers can be created: one for the jmeter, focusing on stimulation of the API and another for pytest, that will validate the results from jmeter (again containting test scripts and remaining files necessary for test execution). The automation can be set via jenkins job.
