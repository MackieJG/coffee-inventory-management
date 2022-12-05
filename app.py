from flask import Flask, render_template

from controllers.coffees_controller import coffees_blueprint
from controllers.producers_controller import producers_blueprint
from controllers.equipment_controller import equipment_blueprint

app = Flask(__name__)

app.register_blueprint(coffees_blueprint)
app.register_blueprint(producers_blueprint)
app.register_blueprint(equipment_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

