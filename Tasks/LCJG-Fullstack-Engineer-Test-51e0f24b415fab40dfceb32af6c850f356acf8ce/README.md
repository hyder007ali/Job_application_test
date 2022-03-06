# LCJG-Fullstack-Engineer-Test

Fullstack engineer interview test for LCJG BetaLabs, expected time needed: < 24 hours

## Setup
Follow the steps to setup a mysql database in local
- Install docker desktop and docker-compose (https://www.docker.com/products/docker-desktop)
- Download the [database.zip](https://raw.githubusercontent.com/ayking/LCJG-Backend-Engineer-Test/master/database.zip)
- Run the following command inside the folder to start the database: `docker-compose  up --build --force-recreate --renew-anon-volumes db`

## Tasks

### Task 1
Please use any python web framework (e.g. flask, fast-api, etc) to create an API with following endpoints (using the database in task 1)

- Endpoint 1 - list customer basic details and able to search by first name, last name and order by credit limit
- Endpoint 2 - get full customers details by customerNumber
- Endpoint 3 - update a first name, last name, and credit by customerNumber


### Task 2
Create a single page app by using **Reactjs**, **Angular** or **Vue** with requirements below: 

- Create a table view showing 20 records per page to present the result (customerNumber, customerName, addressLine1 + addressLine2, country, creditLimit) from Endpoint 1

![Row](https://github.com/LCJG-BetaLabs/LCJG-Fullstack-Engineer-Test/blob/main/demo%20row.png?raw=true)
- Show the details view when click on name field in the record, the detail view should show all the data from Endpoint 2
- Allow user to edit the first name and last name in the details view and update it by Endpoint 3

