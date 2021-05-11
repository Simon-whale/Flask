import json

from Services.DataGenerator import DataGenerator

from flask import Flask
from flask_restx import Api, Resource


# TODO: add functionality so that the API namespaces are automatically expanded

app = Flask(__name__)
api = Api(app, version="1.0", title="Playing with Flask API", description="Playing with Flask API")


experiment_api = api.namespace('Experiments', description='Experiment operations')
second_namespace = api.namespace('Part Two', description='Second Part')


@experiment_api.route('/hello')
@experiment_api.response(200, 'Success')
class HelloWorld(Resource):
    def get(self):
        return {'Hello': 'World'}


@experiment_api.route('/Results')
class Results(Resource):
    def get(self):
        values = DataGenerator.create(0, 100)

        return json.dumps(values)


@second_namespace.route('/MoreResults/<int:start>/<int:end>')
@second_namespace.param('start', 'Starting value for the loop')
@second_namespace.param('end', 'Ending value for the loop (end value is not shown')
class MoreResults(Resource):
    def get(self, start: int, end: int):
        if start == 0 and end == 0:
            return "Start and End values must both be greater than 0", 400

        if start == end:
            return "Start and End values can not be the same value", 400

        values = DataGenerator.create(start, end)
        return json.dumps(values)


if __name__ == '__main__':
    app.run(debug=True)
