# - Prizegenerator(Practical Project)

## Contents


### 1. [Brief](#Brief)
##### * App Functionality
##### * Tools Used
### 2. [Architect](#Architect)
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

(Images)

##### Tools Used
- Trello Board
- Version Control: Git
- CI Server: Jenkins
- Configuration Managment: Ansible
- Cloud Server: GCP virtual machine
- Containerisation: Docker
- Orchestration Tools: Docker Swarm
- Reverse Proxy: NGINX


## Architect

(short text)

##### Entity Diagram

(image)

The Entity diagram shows the table for the App. This is a brief breakdown of how the database stores the codes when they are randomly generated. The Prize table has the prize id, the random code and the prize that comes with it.


##### CI Pipeline

(images)

The CI (Continuous Integration) piplines shoews the technologies used, and how they are all linked to each other. The diagram gives a visual representation on how the whole project has been implemented. 


##### Project Planning 

(images)

To track the progression of the project, a trello board was used. This allowed me to outline the tasks and set gooals for the projecct completion. There were 3 different sprints, as the project progressed different changes where made and the board was updated.

* First Sprint
* Second Sprint
* Final Sprint

## Implementation

To get to the final stage of this project, there were differnet ideas implemented using a variety of tools.

* Swarm
* Ansible
* Jenkins
* HTML Page
* NGINX

## Risk-Assessment
## Testing
## Future Improvements

## Author 
* Jadesola Kanimodo














