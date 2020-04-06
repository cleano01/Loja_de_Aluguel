from flask import Flask, request
from flask_restful import Api
from Modelos.Modelos import Modelos
import rotas


app = Flask(__name__)
api = Api(app)


api.add_resource(rotas.Cliente, '/cliente')
api.add_resource(rotas.TipoItem, '/tipo_item')
api.add_resource(rotas.Item, '/item')
api.add_resource(rotas.Aluga, '/alugar')
api.add_resource(rotas.Reserva, '/reservar')
api.add_resource(rotas.Cancela_Reserva, '/cancelar_reserva')
api.add_resource(rotas.Devolucao_Aluguel, '/devolucao_aluguel')
api.add_resource(rotas.Devolucao_Reserva, '/devolucao_reserva')

bd =  Modelos()
bd.create_table()

if __name__ == '__main__':
       
    app.run(debug=True)