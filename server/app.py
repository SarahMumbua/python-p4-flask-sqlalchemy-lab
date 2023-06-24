#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)
@app.route('/')
def home():
    return '<h1>Zoo app</h1>'
@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get(id)
    if animal:
        # Return the details of the animal, such as its name and species
        return f'''
        <h1>Animal Details</h1>
        <ul>
            <li>Name: {animal.name}</li>
            <li>Species: {animal.species}</li>
        </ul>
        '''
    else:
        return 'Animal not found'

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get(id)
    if zookeeper:
        # Return the details of the zookeeper, such as their name and ID
        return f"Zookeeper ID: {zookeeper.id}, Name: {zookeeper.name}"
    else:
        return 'Zookeeper not found'

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get(id)
    if enclosure:
        # Return the details of the enclosure, such as its ID and environment
        return f"Enclosure ID: {enclosure.id}, Environment: {enclosure.environment}"
    else:
        return 'Enclosure not found'


if __name__ == '__main__':
    app.run(port=5555, debug=True)