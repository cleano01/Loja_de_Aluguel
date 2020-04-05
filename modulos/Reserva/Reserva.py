import sqlite3
from flask_restful import Resource
from flask import Flask, request
import datetime
import time


class Reserva (Resource):
    
    def __init__(self):
        self.conn = sqlite3.connect('base.bd')
        self.cursor = self.conn.cursor()
        self.conn.execute('PRAGMA Foreign_keys = ON;')


    def post(self):
        try:
            
            cursor = self.conn.cursor()            
            dados_requisicao = request.json              
            data_reserva =dados_requisicao.get('data_reserva')
            

            data_devolucao = ''
            entrega = False
            cancelamento = False
            cpf = dados_requisicao.get('cpf')
            id_item = dados_requisicao.get('id_item')


            lista = [(data_reserva, data_devolucao, entrega, 
            cancelamento, cpf,  id_item)]


            self.conn.executemany('INSERT INTO ReservaItem \
            (data_reserva, data_devolucao, entrega, \
            cancelamento, cpf, id_item )\
            VALUES (?, ?, ?, ?, ?, ?)',lista)


            self.conn.commit()
            cursor.close()        
            return {'Status':'Dados inseridos'}
        
        except Exception as exception:            
            return {'Error': f"Não foi possivél alugar um item: {exception}"}
            
    
    def put(self):
        try:
            cursor = self.conn.cursor()            
            dados_requisicao = request.json


            cpf = dados_requisicao.get('cpf')
            id_item = dados_requisicao.get('id_item')
            id_reserva = dados_requisicao.get('id_reserva')
            data_atual = str(datetime.datetime.fromtimestamp\
            (int(time.time())).strftime('%Y-%m-%d'))


            cursor.execute(f'UPDATE  ReservaItem  SET entrega={1}\
             WHERE exists (select * from Cliente,\
             Item where ReservaItem.cpf = {cpf} and\
			 Cliente.cpf = {cpf} and\
			 ReservaItem.id = {id_reserva} and\
			 Item.id_tipo =  {id_item} and\
             ReservaItem.data_reserva <= "{data_atual}")')


            self.conn.commit()
            cursor.close()


            if(cursor.rowcount > 0):
                return {'Status':f'Dados atualizados {cursor.rowcount}'}
 
            return {'Status':f'Nenhum dados foi atualizados  {cursor.rowcount}'}


        except Exception as exception:
            return {'Error': f"Não foi possivél Resevar um item: {exception}"}

       
 



