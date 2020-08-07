# Project SFIA 1 - La Fiesta de Piscina

## The Brief
*-Taken directly from the Fundamental Project specification on Community-*

Your overall objective with this project is the following:

To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

### Proposed Solution
For this project, I decided to create a CRUD application based around a music festival, where a user could view the headliners, buy tickets to the event and amend the orders that they have made. It would meet the requirements set out by the specification, by utilising all the modules taught, and within the constraints specified, such as having at least 2 tables that share a relationship.
_________________________________________________________________________________________________________________________________________________________________

## [Architecture](https://docs.google.com/presentation/d/1_xDR19iRin1x-JbXEpeXnpWctO_i5_fxQrBvRhd9zi4/edit#slide=id.p)

### Entity Relationship Diagrams
As part of the planning process of the project, an ERD was constructed to set out the relational database and its associating relationships. 

### Risk Assessment
The risk assessment was constructed using the format of a risk register, which was amended throughout the entirety of the project - setting out intial events to be considered, and evaluated at the end to ensure all risk were taken into consideration.

### MoSCoW Prioritisation
This form of documentation is used to set the guidelines for the project as an application. Using the acronym, it is a way of prioritising what tasks need to be completed first. 
_________________________________________________________________________________________________________________________________________________________________

## Testing
The project was built around the concept of TDD (Test Driven Development). Being the core value of the development, it had a major role to play if the project were to be successful. Test coverage at current stage in development is a respectable 82%.

Testing methods such as Unit Testing and Integration Testing were implemented throughout the program, using a number of frameworks such as:
  - Werkzeug (Flask Unit Testing)
  - Flask-testing (Flask Integration Testing
  - Selenium (Flask Integration Testing)
  - Gunicorn (Web Server Gateway Interface - WSGI)
  - Pytest
  
_________________________________________________________________________________________________________________________________________________________________  
## Application Deployment Process

### Technologies Used and Overview of Development
#### (- In a rough chronological order of implementation)

#### A multitude of diverse, intuitive technologies were combined in order to successfully build, develop and deliver this project.

* Agile Fundamentals
  - This is the framework that was used to organise and plan the entire project. Working in an agile way enables the planning of sprints, a product backlog, and     allowing for adaptability. Working in an agile way facilitated the development of the application, testing and documentation simultaneously. Without such fundamentals, the project wouldn't have been completed in the time given, as each change would require backtracking and remapping of the entire plan. 
  
* [Jira](https://jsandhu.atlassian.net/secure/RapidBoard.jspa?rapidView=6&projectKey=FES&view=planning&selectedIssue=FES-76&issueLimit=100) - Project Tracking
  - The Jira Board was essentially the backbone of this project. It defined all tasks, which tasks should be completed when (via the use of sprints) and frequent 
    checks ensure that tasks weren't forgotten or missed. Along with the use of Planning Poker, tasks were also assigned story points, which allocates priority and levels of difficult.
  
* Python - Visual Studio Code
  -  Python was also heavily implemented throughout the development of the project, using Jinja2 syntax, it was used to perform operations in the HTML files which allowed for querying and integrating forms and user input. 
  
* [Git](https://github.com/JavasMiddi/SFIA-Project1) - VCS
  - The use of Git was imperative in developing the assignment; it was used to not only hold the repository which contains the entire application, but allowed for the push up of changes to the master version of the project. As a Version Control System, it helps DevOps engineers such as myself to manage the source code, and the project simply wouldn't exist without it. 
 
* [GCP](https://console.cloud.google.com/home/dashboard?cloudshell=true&project=practiceproject-283411) - Cloud Service Provider
  - GCP was crucial in the foundation of the project, it was used to configure the virtual environments and all databases associated with the project. The virtual machines were used to manage the source code and provide the first stage of a test environment. GCP also created the link between the source code and the databases, through the use of exported variables, firewalls and ports. 
  
* Databases & SQL - Fundamentals
  - Databases are useless without SQL, the understanding of its principles allowed the databases to be used within the application to the best of their ability. SQL is what performs the CRUD operations on the database at the back end. Again, GCP was the provider for enabling SQL. 

* Linux
  - In summary, utilising Linux and its commands created the application. It created the files, directories and enabled the application to deploy as a service. Linux allows for the creation of sudoers and what permissions they have in terms of what they can do with files. 
  
* Flask 
  - Flask made the application possible. As an extensible micro-framework, it gives the engineer the tools to create the application, while allowing for customisation and flexibility. Ranging from a basic web application to a large-scale assignment, it was used create my SFIA Project. Flask also allowed the deployment of application through Gunicorn.
  
* HTML 
  - HTML created the front end of the application, it ensured the user could easily navigate throughout the application, and could perform the necessary operations through redirects and input forms. HTML was crucial for the project, as the operations couldn't be configured without the layout and format that HTML provides. 
  
* Jenkins - CI Server
  - Jenkins took the basic application and raised it to a higher level of development and implementation. Before the application was integrated with Jenkins, I had to physically start the application through the virtual machine, or through Gunicorn. However, Jenkins truly added automation to the SFIA project. Through the use of jobs and workspaces, automation was configured through Github Webhooks and Build steps. Build steps are essentially the primary linux commands that I would have ran myself physically through the virtual machine. Using Jenkins as the CI Pipeline, it allowed those primary commands to be ran by the click of a button - not only this but the process of the deployment of the application itself ensures that it is deployed correctly.

A separate job is created to run the tests before the application is even built - if all tests are successful and there are no errors within the source code, it triggers a build for the application itself to be built, and deploys it via the specified URL. Without this functionality, Jenkins would continue to build broken versions of the application, which is efficient or practical in any sense.  
  
#### Every technology listed above was undeniably paramount in the creation of the project, and the absence of any one technology would hinder the application. 
_________________________________________________________________________________________________________________________________________________________________

## Future Improvements

Currently, the application has been successfully integrated with Jenkins and has deployed as service. CRUD functionality has successfully been met via the MVP. 

In my next sprint, I would like to develop the application further by making use of the last entity - the timeSlot table. After the input of data, I would like to present it alongside the artists, thus a schedule being made. 

In later sprints, I would also like to utilise the foreign keys in such a way as to allow for the deletion of a customer account, along with all the orders that said account has created. Also, a querying option to select which artists are performing on which day, initialising the relationship between the Artist table and the timeSlot table.

_________________________________________________________________________________________________________________________________________________________________

## Honorable Mentions
* QA's own Luke Benson - Trainer
* The JulyDevOps Cohort
_________________________________________________________________________________________________________________________________________________________________
