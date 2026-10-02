from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

hoteis = [
    {"hotel_id": "Pinthon", "nome": "Hotel Pinthon", "estrelas": 4.8, "diaria": 125.75, "cidade": "Genebra"},
    {"hotel_id": "Estrella", "nome": "Hotel Estrella", "estrelas": 4.5, "diaria": 150.00, "cidade": "Zurique"},
    {"hotel_id": "Pinto", "nome": "Hotel Pinto", "estrelas": 5.0, "diaria": 654.00, "cidade": "Berna"}
]

class Hoteis(Resource):
    def get(self):
        return {"hoteis": hoteis}

class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel["hotel_id"] == hotel_id:
                return hotel, 200
        return {"message": "Hotel não encontrado."}, 404

api.add_resource(Hoteis, "/hoteis")
api.add_resource(Hotel, "/hoteis/<string:hotel_id>")

if __name__ == "__main__":
    app.run(debug=True)