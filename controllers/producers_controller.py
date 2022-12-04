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

@producers_blueprint.route('/producers/new', methods=['GET'])
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
