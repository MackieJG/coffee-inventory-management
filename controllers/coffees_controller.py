import unittest
from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.coffee_repository as coffee_repository
import repositories.producer_repository as producer_repository
import repositories.equipment_repository as equipment_repository

from models.coffee import Coffee
from models.equipment import Equipment

coffees_blueprint = Blueprint('coffees', __name__)

@coffees_blueprint.route('/coffees')
def all_coffees():
    coffees = coffee_repository.select_all()
    return render_template('coffees/index.html', all_coffees = coffees)

@coffees_blueprint.route('/coffees/<int:id>', methods=['GET'])
def show_coffee(id):
    coffee = coffee_repository.select(id)
    return render_template('coffees/coffee.html', coffee = coffee)

@coffees_blueprint.route('/coffees/newcoffee', methods=['GET'])
def new_coffee():
    producers = producer_repository.select_all()
    return render_template('coffees/newcoffee.html', all_producers = producers)

@coffees_blueprint.route('/coffees', methods=['POST'])
def create_coffee():
    name = request.form['name']
    origin = request.form['origin']
    description = request.form['description']
    producer_id = request.form['producer_id']
    producer = producer_repository.select(producer_id)
    stock = request.form['stock']
    buy_price = request.form['buy_price']
    sell_price = request.form['sell_price']
    coffee = Coffee(name, origin, description, producer, stock, buy_price, sell_price)
    coffee_repository.save(coffee)
    return redirect('/coffees')

@coffees_blueprint.route('/coffees/<id>/edit', methods=['GET'])
def edit_coffee(id):
    coffee = coffee_repository.select(id)
    producers = producer_repository.select_all()
    return render_template('coffees/edit.html', coffee = coffee, all_producers = producers)

@coffees_blueprint.route('/coffees/<id>', methods=['POST'])
def update_coffee(id):
    name = request.form['name']
    origin = request.form['origin']
    description = request.form['description']
    producer = producer_repository.select(request.form['producer_id'])
    stock = request.form['stock']
    buy_price = request.form['buy_price']
    sell_price = request.form['sell_price']
    coffee = Coffee(name, origin, description, producer, stock, buy_price, sell_price, id)
    coffee_repository.update(coffee)
    return redirect('/coffees')

@coffees_blueprint.route('/coffees/<id>/delete', methods=['POST'])
def delete_coffee(id):
    coffee_repository.delete(id)
    return redirect('/coffees')

@coffees_blueprint.route('/inventory')
def show_all_stock():
    coffees = coffee_repository.select_all()
    equipment = equipment_repository.select_all()
    return render_template('/inventory.html', all_coffees = coffees, all_equipment = equipment)