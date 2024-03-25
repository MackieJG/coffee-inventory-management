# Your Inventory Manager App

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about">About</a>
      <ul>
        <li><a href="#design">Design</a></li>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#reflections">Reflections</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>
<!-- ABOUT -->
### Coffee Inventory Management

An app built in Flask which allows roastery employees manage coffee inventory

### MVP:

### Main Web Application
* Users can add, update and delete coffee products to the database
* Be able to filter through different categories only providing the appropriate rows
* Be able to view all products in clean format

Inspired by:
Shopify, Square, iZettle

### Possible Extensions:

* The user should be able to mark Merchants and Tags as deactivated. Users will not be able to choose deactivated merchants/tags when creating a transaction. 
* Transactions should have a timestamp, and the user should be able to view transactions sorted by the time they took place.
* The user should be able to supply a budget, and the app should alert the user somehow when when they are nearing this budget or have gone over it.
* The user should be able to filter their view of transactions, for example, to view all transactions in a given month, or view all spending on groceries.
<!-- DESIGN -->
## Design
I used LucidChart to Map out the layout and design criteria for the app. 

<!-- Built With -->
Built With:

* HTML
* CSS
* Python
* Flask
* PostgresSQL

<!-- GETTING STARTED -->
## Getting Started
###Prerequisites

Psychopg:
```sh
pip3 install psycopg2
```
Flask:
```sh
pip3 install Flask
```
INSTALLATION:

Clone the repository:
https://github.com/MackieJG/coffee-inventory-management

Create the Database:
```sh
psql -d stock_manager -f db/stock_manager.sql
```
Populate the database with pre-set data:
```sh
python3 console.py
```
Run the app:
```sh
 flask run
```
<!-- CONTACT -->
##Contact

* Joshua Mackie - [GitHub](https://github.com/mackiejg)

Project Link [https://github.com/mackiejg/coffee-inventory-management](https://github.com/mackiejg/coffee-inventory-management)




