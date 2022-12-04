from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.producer_repository as producer_repository

producers_blueprint = Blueprint('producers', __name__)

@producers_blueprint.route('/producers')
def all_producers():
    producers = producer_repository.select_all()
    return render_template('/producers/index.html', all_producers = producers)

