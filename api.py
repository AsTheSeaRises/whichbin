from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

bin = {"21Nov": "recycling-black bin", "28Nov" : "rubbish-green", "5Dec" : "recycling-glass"}

class HelloWorld(Resource):
        def get(self, name):
            return bin[name]
api.add_resource(HelloWorld, "/whichbin/<string:name>")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080) #(debug=True)