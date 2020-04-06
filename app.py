from flask import Flask, request
from flask_restful import Api
import sqlite3
import banco_de_dados

from modulos.Cliente.Cliente import Cliente
from modulos.Item.TipoItem import TipoItem
from modulos.Item.Item import Item
from modulos.Aluga.Aluga import Aluga
from modulos.Reserva.Reserva import Reserva
from modulos.Cancela_Reserva.Cancela_Reserva import Cancela_Reserva
from modulos.Devolucao_Item.Devolucao_Aluguel import Devolucao_Aluguel
from modulos.Devolucao_Item.Devolucao_Reserva import Devolucao_Reserva

app = Flask(__name__)
api = Api(app)


api.add_resource(Cliente, '/cliente')
api.add_resource(TipoItem, '/tipo_item')
api.add_resource(Item, '/item')
api.add_resource(Aluga, '/alugar')
api.add_resource(Reserva, '/reservar')
api.add_resource(Cancela_Reserva, '/cancelar_reserva')
api.add_resource(Devolucao_Aluguel, '/devolucao_aluguel')
api.add_resource(Devolucao_Reserva, '/devolucao_reserva')

if __name__ == '__main__':
            
    app.run(debug=True)