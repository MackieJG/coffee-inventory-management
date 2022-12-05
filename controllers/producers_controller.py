from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.producer import Producer
import repositories.producer_repository as producer_repository

producers_blueprint = Blueprint('producers', __name__)

@producers_blueprint.route('/producers')
def all_producers():
    producers = producer_repository.select_all()
    return render_template('producers/index.html', all_producers = producers)

@producers_blueprint.route('/producers/<int:id>', methods=['GET'])
def show_producer(id):
    producer = producer_repository.select(id)
    return render_template('producers/producer.html', producer = producer)

@producers_blueprint.route('/producers/newproducer', methods=['GET'])
def new_producer():
    return render_template('producers/newproducer.html')

@producers_blueprint.route('/producers', methods=['POST'])
def create_producer():
    name = request.form['name']
    location = request.form['location']
    description = request.form['description']
    producer = Producer(name, location, description)
    producer_repository.save(producer)
    return redirect('/producers')

@producers_blueprint.route('/producers/<id>/delete', methods=['POST'])
def delete_producer(id):
    producer_repository.delete(id)
    return redirect('/producer')

@producers_blueprint.route('/producers/<id>/edit', methods=['GET'])
def edit_producer(id):
    producer = producer_repository.select(id)
    return render_template('producers/edit.html', producer = producer)

@producers_blueprint.route('/producers/<id>', methods=['POST'])
def update_producer(id):
    name = request.form['name']
    location = request.form['location']
    description = request.form['description']
    producer = Producer(name, location, description, id)
    producer_repository.update(producer)
    return redirect('/producers')