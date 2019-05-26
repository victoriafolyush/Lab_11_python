# init app
import os


from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,
                                                                    'dbsqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
database = SQLAlchemy(app)
# Init ma
marshmallow = Marshmallow(app)


class SkiResortMachinery(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(138), unique=True)
    producer = database.Column(database.String)
    fuel_per_hour = database.Column(database.Float)
    mileage = database.Column(database.Float)

    def __init__(self,
                 name,
                 producer,
                 fuel_per_hour,
                 mileage):
        self.name = name
        self.producer = producer
        self.fuel_per_hour = fuel_per_hour
        self.mileage = mileage


class SkiResortMachinerySchema(marshmallow.Schema):
    class Meta:
        fields = ('name', 'producer', 'fuel_per_hour', 'mileage')


machinery_schema = SkiResortMachinerySchema(strict=True)
machineries_schema = SkiResortMachinerySchema(many=True, strict=True)


@app.route('/ski_resort_machinery', methods=['POST'])
def add_machinery():
    name = request.json['name']
    producer = request.json['producer']
    fuel_per_hour = request.json['fuel_per_hour']
    mileage = request.json['mileage']

    new_machinery = SkiResortMachinery(name, producer, fuel_per_hour, mileage)

    database.session.add(new_machinery)
    database.session.commit()

    return machinery_schema.jsonify(new_machinery)


@app.route('/ski_resort_machinery', methods=['GET'])
def get_all_machineries():
    all_machineries = SkiResortMachinery.query.all()
    result = machineries_schema.dump(all_machineries)
    return jsonify(result.data)


@app.route('/ski_resort_machinery/<id>', methods=['GET'])
def get_machinery(id):
    machinery = SkiResortMachinery.query.get(id)
    return machinery_schema.jsonify(machinery)


@app.route('/ski_resort_machinery/<id>', methods=['PUT'])
def put_machinery(id):
    machinery = SkiResortMachinery.query.get(id)

    name = request.json['name']
    producer = request.json['producer']
    fuel_per_hour = request.json['fuel_per_hour']
    mileage = request.json['mileage']

    machinery.name = name
    machinery.producer = producer
    machinery.fuel_per_hour = fuel_per_hour
    machinery.mileage = mileage

    database.session.commit()
    return machinery_schema.jsonify(machinery)


@app.route('/ski_resort_machinery/<id>', methods=['DELETE'])
def delete_machinery(id):
    machinery = SkiResortMachinery.query.get(id)
    database.session.delete(machinery)
    database.session.commit()
    return machinery_schema.jsonify(machinery)


#database.create_all()

if __name__ == '__main__':
    app.run(debug=True)
