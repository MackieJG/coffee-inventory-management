Your Inventoruy Manager App

Build an App that keeps track of your Inventory for Coffee Shop/Roaster

MVP:

* The inventory should track individual products, including a name, description, stock quantity, buying cost, and selling price.
* The inventory should track manufacturers, including a name and any other appropriate details.
* The shop can sell anything you like, but you should be able to create and edit manufacturers and products separately.
  * This might mean that it makes more sense for a car shop to track makes and models of cars. Or a bookstore might sell books by author, or by publisher, and not by manufacturer. You are free to name classes and tables as appropriate to your project.
* Show an inventory page, listing all the details for all the products in stock in a single view.
* As well as showing stock quantity as a number, the app should visually highlight "low stock" and "out of stock" items to the user.

Inspired by:

Monzo, MoneyDashboard, lots of mobile/online banking apps

Possible Extensions:

* The user should be able to mark Merchants and Tags as deactivated. Users will not be able to choose deactivated merchants/tags when creating a transaction. 
* Transactions should have a timestamp, and the user should be able to view transactions sorted by the time they took place.
* The user should be able to supply a budget, and the app should alert the user somehow when when they are nearing this budget or have gone over it.
* The user should be able to filter their view of transactions, for example, to view all transactions in a given month, or view all spending on groceries.

Project Planning:

I used LucidChart to Map out the layout and design criteria for the place. 

Built With:

HTML
CSS
Python
Flask
PostgresSQL


To Test this App:

Psychopg:

pip3 install psycopg2

Flask:

pip3 install Flask

INSTALLATION:

1. Clone the repository

https://github.com/MackieJG/Project_Python_W5

2. Navigate to the folder using the Terminal

3. Create the Database
  -  psql -d stock_manager -f db/stock_manager.sql

4. Populate the database with pre-set data.
  - python3 console.py

5. Run Flask
  - flask run

6. Using preferably Chrome
 - access the app http://127.0.0.1:4999

7. To close the running of the app
 - control c
 



