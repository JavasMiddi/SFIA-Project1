# Project SFIA 1 - La Fiesta de Piscina

## The Brief
*-Taken directly from the Fundamental Project specification on Community-*

Your overall objective with this project is the following:

To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

### Proposed Solution
For this project, I decided to create a CRUD application based around a music festival, where a user could view the headliners, buy tickets to the event and amend the orders that they have made. It would meet the requirements set out by the specification, by utilising all the modules taught, and within the constraints specified, such as having at least 2 tables that share a relationship.
_________________________________________________________________________________________________________________________________________________________________

## Architecture

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
  - Pytest
  
_________________________________________________________________________________________________________________________________________________________________  
## Application Deployment Process

### Technologies Used and Overview of Development

* Agile Fundamentals
  - This is the framework that was used to organise and plan the entire project. Working in an agile way enables the planning of sprints, a product backlog, and     allowing for adaptability. Working in an agile way facilitated the development of the application, testing and documentation simultaneously. Without such
    fundamentals, the project wouldn't have been completed in the time given, as each change would require backtracking and remapping of the entire plan. 
  
* [Jira](https://jsandhu.atlassian.net/secure/RapidBoard.jspa?rapidView=6&projectKey=FES&view=planning&selectedIssue=FES-76&issueLimit=100) - Project Tracking
  - The Jira Board is essentially the backbone of this project. It defines all tasks, which tasks should be completed when (via the use of sprints) and frequent 
    checks ensure that you don't forget or miss any tasks.
  
* Python - Visual Studio Code
  -  
  
* [Git](https://github.com/JavasMiddi/SFIA-Project1) - VCS
  -
 
* GCP - Cloud Service Provider
  - GCP was crucial in the foundation of the project, it was used to configure the virtual environments and all databases associated with the project.
  
* Databases & SQL - Fundamentals
  -

* Linux
  -
  
* Flask 
  -
  
* Jenkins - CI Server
  - 
_________________________________________________________________________________________________________________________________________________________________

## Future Improvements

Currently, the application has been successfully integrated with Jenkins and has deployed as service. CRUD functionality has been met via the MVP. 

In my next sprint, I would like to develop the application further by making use of the last entity - the timeSlot table. After the input of data, I would like to present it alongside the artists, thus a schedule being made. 

In later sprints, I would also like to utilise the foreign keys in such a way as to allow for the deletion of a customer account, along with all the orders that said account has created. Also, a querying option to select which artists are performing on which day, initialising the relationship between the Artist table and the timeSlot table.

_________________________________________________________________________________________________________________________________________________________________

## Honorable Mentions
* QA's own Luke Benson - Trainer
* The JulyDevOps Cohort
_________________________________________________________________________________________________________________________________________________________________
