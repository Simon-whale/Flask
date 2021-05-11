import json
from Services.DataGenerator import DataGenerator

from flask import Flask
from flask_restplus import Resource, Api

# TODO: add functionality so that the API namespaces are automatically expanded
# TODO: replace flask_restplus as this is now obsolete and not being maintained

app = Flask(__name__)
api = Api(app)


experiment_api = api.namespace('Experiments', description='Experiment operations')
second_namespace = api.namespace('Part Two', description='Second Part')


@experiment_api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'Hello': 'World'}


@experiment_api.route('/Results')
class Results(Resource):
    def get(self):
        values = DataGenerator.create(0, 100)

        return json.dumps(values)


@second_namespace.route('/MoreResults/<int:start>/<int:end>')
class MoreResults(Resource):
    def get(self, start: int, end: int):
        values = DataGenerator.create(start, end)
        return json.dumps(values)


if __name__ == '__main__':
    app.run(debug=True)
