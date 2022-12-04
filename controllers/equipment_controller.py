from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.equipment_repository as equipment_repository

equipment_blueprint = Blueprint('equipment', __name__)

@equipment_blueprint.route('/equipment')
def all_equipment():
    equipment = equipment_repository.select_all()
    return render_template('equipment/index.html', all_equipment = equipment)

@equipment_blueprint.route('/equipment/<int:id>', methods=['GET'])
def show_equipment(id):
    equipment = equipment_repository.select(id)
    return render_template('equipment/equipment.html', equipment = equipment)