# - Prizegenerator(Practical Project)

## Contents

### 1. [Brief](#Brief)
### 2. [Application Outline](#Application Outline)
##### * Tools Used
### 3. [Architect](#Architect)
#####  * Entity Diagram
##### * CI Pipeline
##### * Project Tracking
### 4. [Implementation](#Implementation)
##### * Swarm
##### * Ansible
##### * Jenkins
##### * HTML Update Page
#### * Nginx
### 5. [Risk Assessment](#Risk-Assessment)
### 6. [Testing](#Testing)
### 7. [Future Improvements](#Future-Improvements)





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



## Application Outline
For this project, I created a prize generatator app. A random code is generated and to win prizes you have to have a specific code, to win a car the code has to start with the letter C and the second number has to be a one.To win Chocolates, the fifth number has to be a nine. To achieve all this, i needed to create four micro services, and they all depend on each other in order for the app to work.
- Service One: This is the core service, it will render the Jinja2 templates needed to interact with the application, it will also be responsible for communicating with the other three services.
- Service Two & Three: These two services are responsible for creating random outputs for the users.
- Service Four: This service takes the output from service one & two and process it. It will then create a random output.

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













