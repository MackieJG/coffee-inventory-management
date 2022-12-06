from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.equipment_repository as equipment_repository
import repositories.producer_repository as producer_repository
from models.equipment import Equipment

equipment_blueprint = Blueprint('equipment', __name__)

@equipment_blueprint.route('/equipment')
def all_equipment():
    equipment = equipment_repository.select_all()
    return render_template('equipment/index.html', all_equipment = equipment)

@equipment_blueprint.route('/equipment/<int:id>', methods=['GET'])
def show_equipment(id):
    equipment = equipment_repository.select(id)
    return render_template('equipment/equipment.html', equipment = equipment)

@equipment_blueprint.route('/equipment/new', methods=['GET'])
def new_equipment():
    producers = producer_repository.select_all()
    return render_template('equipment/new.html', all_producers = producers)

@equipment_blueprint.route('/equipment/<id>/edit', methods=['GET'])
def edit_equipment(id):
    equipment = equipment_repository.select(id)
    producers = producer_repository.select_all()
    return render_template('equipment/edit.html', equipment = equipment, all_producers = producers)
   
@equipment_blueprint.route('/equipment/<id>', methods=['POST'])
def update_equipment(id):
    name = request.form['name']
    producer = producer_repository.select(request.form['producer_id'])
    stock = request.form['stock']
    buy_price = request.form['buy_price']
    sell_price = request.form['sell_price']
    equipment = Equipment(name, producer, stock, buy_price, sell_price, id)
    equipment_repository.update(equipment)
    return redirect('/equipment')

@equipment_blueprint.route('/equipment/<id>/delete', methods=['POST'])
def delete_equipment(id):
    equipment_repository.delete(id)
    return redirect('/equipment')

@equipment_blueprint.route('/equipment', methods=['POST'])
def create_equipment():
    name = request.form['name']
    producer_id = request.form['producer_id']
    producer = producer_repository.select(producer_id)
    stock = request.form['stock']
    buy_price = request.form['buy_price']
    sell_price = request.form['sell_price']
    equipment = Equipment(name, producer, stock, buy_price, sell_price)
    equipment_repository.save(equipment)
    return redirect('/equipment')




