# - Prizegenerator(Practical Project)

## Contents


### 1. [Brief](#Brief)
##### * App Functionality
##### * Tools Used
### 2. [Architecture](#Architecture)
#####  * Entity Diagram
##### * CI Pipeline
##### * Project Tracking
### 3. [Implementation](#Implementation)
##### * Swarm
##### * Ansible
##### * Jenkins
##### * HTML Update Page
#### * Nginx
### 4. [Risk Assessment](#Risk-Assessment)
### 5. [Testing](#Testing)
### 6. [Future Improvements](#Future-Improvements)



## Helpful Links
Trello: https://trello.com/b/A5FLlJQ7/prize-generator




## Brief

In this project, the brief states to create an application that has four servers, allowing the user to generate an output based on a set of predefined rules. To complete this project a full expansion of tasks and tools were used to meet the project goal. The MVP requirements are below:

Requirments:
- An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
- This could also provide a record of any issues or risks that you faced creating your project.
- An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
- If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
- The project must follow the Service-oriented architecture that has been asked for.
- The project must be deployed using containerisation and an orchestration tool.
- As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
- The project must make use of a reverse proxy to make your application accessible to the user.


##### App Functionality 
For this project, I created a prize generatator app. A random code is generated and to win prizes you have to have a specific code, to win a car the code has to start with the letter C and the second number has to be a one.To win Chocolates, the fifth number has to be a nine. To achieve all this, i needed to create four micro services, and they all depend on each other in order for the app to work.
- Service One: This is the core service, it will render the Jinja2 templates needed to interact with the application, it will also be responsible for communicating with the other three services.
- Service Two & Three: These two services are responsible for creating random outputs for the users.
- Service Four: This service takes the output from service one & two and process it. It will then create a random output.

![imageone](https://github.com/jadecodespy/prizegenerator/blob/test_branch/prizegenerator/Application%20Flow.png)

##### Tools Used
- Trello Board
- Version Control: Git
- CI Server: Jenkins
- Configuration Managment: Ansible
- Cloud Server: GCP virtual machine
- Containerisation: Docker
- Orchestration Tools: Docker Swarm
- Reverse Proxy: NGINX


## Architecture
In this section, the infrastructure of the project is shown:

##### Entity Diagram

![imagetwo](https://github.com/jadecodespy/prizegenerator/blob/test_branch/prizegenerator/prizetable.png)

The Entity diagram shows the table for the App. This is a brief breakdown of how the database stores the codes when they are randomly generated. The Prize table has the prize id, the random code and the prize that comes with it.


##### CI Pipeline

![imagethree](https://github.com/jadecodespy/prizegenerator/blob/test_branch/prizegenerator/CI%20Pipline.png)

The CI (Continuous Integration) piplines shoews the technologies used, and how they are all linked to each other. The diagram gives a visual representation on how the whole project has been implemented.


##### Project Planning 

To track the progression of the project, a trello board was used. This allowed me to outline the tasks and set gooals for the projecct completion. There were 3 different sprints, as the project progressed different changes where made and the board was updated.

* First Sprint: In this sprint, i was planning how i wanted my project to work, collecting all the requirements and creating the application flow
![imagefour](https://github.com/jadecodespy/prizegenerator/blob/test_branch/prizegenerator/trello%201.jpg)
* Second Sprint: The second sprint, i started with the implementation of the tools in creating the application.
![imagefive](https://github.com/jadecodespy/prizegenerator/blob/test_branch/prizegenerator/trello2.jpg)
* Final Sprint
![imagesix](https://github.com/jadecodespy/prizegenerator/blob/test_branch/prizegenerator/trello3.jpg)
## Implementation

To get to the final stage of this project, there were differnet ideas implemented using a variety of tools.

* Swarm: Swarm is a group of virtual machines, i had one Swarm Master and 1 worker. Using Swarm make it easy for me to delpy my app and make it more scalable.
* Ansible: Ansible is a configuration Tool, i used ansible to set up my swarms.I did this by creating a playbook, setup an inventory & roles.
* Jenkins: Jenkins was a very important part of this project, as it made deploying the app very easy.I set up a pipeline from Git to automate any pulling, installed and set up my ansible and also my docker compose.While trying to create my builds, i hit a few issues i was able to fix.The first issue was saying "No TTY-ASK PASS, i had to give my jenkins user permission and allow all passwords.Then another issue that i had was it wasnt connecting to my dockerhub.All i had to do was log in and connect.
When i fixed all the errors, i got my build to be successful.
![Imagesseven](https://github.com/jadecodespy/prizegenerator/blob/test_branch/prizegenerator/jenkins1.jpg)
![imageeight](https://github.com/jadecodespy/prizegenerator/blob/test_branch/prizegenerator/fails1.jpg)



* HTML Page: This is my Main page and the front end of my app. When you click the refresh button, different codes are generated and the prizes are displayed on the screen
![imagenine](https://github.com/jadecodespy/prizegenerator/blob/test_branch/prizegenerator/page1.jpg)

* NGINX: Nginx is a web server, i used it for HTTP caching in my project.

## Risk-Assessment
I documented a few risks, and how i'd go by solving the issues if they arise.

![imageten](https://github.com/jadecodespy/prizegenerator/blob/test_branch/prizegenerator/risky34.png)

## Testing
Testing was done with Pytest, the application were all unit tested, each service were tested to see if they work individually.Service 2,3&4 all passed the unnittest. The service1 had an issue with the Post request from the mock test. I was unable to fix this test.
![imageeleven](https://github.com/jadecodespy/prizegenerator/blob/test_branch/prizegenerator/unit2.jpg)
![imagetweleve](https://github.com/jadecodespy/prizegenerator/blob/test_branch/prizegenerator/unit3.jpg)
![imagethirteen](https://github.com/jadecodespy/prizegenerator/blob/test_branch/prizegenerator/unit1.jpg)
Here i have added the testing for the Service1, two different method of testing where tried but none of them seemed to work.

![imagefourteen](https://github.com/jadecodespy/prizegenerator/blob/test_branch/prizegenerator/testing45.jpg)
![imagefifteen](https://github.com/jadecodespy/prizegenerator/blob/test_branch/prizegenerator/testing2.jpg)

## Future Improvements

In the Future, i'd make sure to automate all the process with Jenkins, at the moment some of the project is still done manually.
I would like to improve my test and make sure they all pass the test and get 100% coverage.
I would like to make the front end page more appealing to the user.

## Author 
* Jadesola Kanimodo














