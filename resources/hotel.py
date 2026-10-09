from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
    {"hotel_id": "Pinthon", "nome": "Hotel Pinthon", "estrelas": 4.8, "diaria": 125.75, "cidade": "Genévè"},
    {"hotel_id": "Estrella", "nome": "Hotel Estrella", "estrelas": 4.5, "diaria": 150.00, "cidade": "Zurich"},
    {"hotel_id": "Pinto", "nome": "Hotel Pinto", "estrelas": 5.0, "diaria": 654.00, "cidade": "Bern"}
]

class Hoteis(Resource):
    def get(self):
        return {"hoteis": hoteis}

class Hotel(Resource):
    argumentos = reqparse.RequestParser() # dados é um dicionario
    argumentos.add_argument("nome", type=str, required=True, help="O nome do hotel é obrigatório")
    argumentos.add_argument("Estrelas", type=float, required=True, help="As Estrelas são obrigatórias")
    argumentos.add_argument("diaria", type=float, required=True, help="A Diária é obrigatória")
    argumentos.add_argument("cidade", type=str, required=True, help="O nome da cidade é obrigatório")

    def encontrar_hotel(self,hotel_id):
        for hotel in hoteis:
                if hotel["hotel_id"] == hotel_id:
                    return hotel
        return None

    def get(self, hotel_id):
        hotel = self.encontrar_hotel(hotel_id)
        if hotel is not None:
            return hotel, 200
        return {"message": "Hotel não encontrado."}, 404

    def post(self, hotel_id):
        dados= Hotel.argumentos.parse_args()
        hotel = self.encontrar_hotel(hotel_id)
        if hotel is not None:
            return { "mensagem": f"o hotel com id {hotel_id} já existe na minha lista."}

        novo_hotel= {"hotel_id": hotel_id, **dados}
        hoteis.append(novo_hotel)
        return novo_hotel, 200
    
    #atualizar hotel
    def put(self, hotel_id):
        dados= Hotel.argumentos.parse_args()
        hotel = self.encontrar_hotel(hotel_id)
        if hotel is not None:
            hotel.update(dados)
            return hotel, 200
            
        #se o hotel não existir, cria um novo
        novo_hotel= {"hotel_id": hotel_id, **dados}
        hoteis.append(novo_hotel)
        return novo_hotel, 201
    
    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel["hotel_id"] != hotel_id]
        return {"message": "O Hotel com id {hotel_id} foi deletado."}, 200
