import unittest
from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.coffee_repository as coffee_repository

coffees_blueprint = Blueprint('coffees', __name__)

@coffees_blueprint.route('/coffees')
def all_coffees():
    coffees = coffee_repository.select_all()
    return render_template('coffees/index.html', all_coffees = coffees)

@coffees_blueprint.route('/coffees/<int:id>', methods=['GET'])
def show_coffee(id):
    coffee = coffee_repository.select(id)
    return render_template('coffees/coffee.html', coffee = coffee)
