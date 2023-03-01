from classes.banco_dados import BancoDados
from classes.clientes_db import Clientes_DB
from classes.cliente import Cliente
from classes.registro import Registro
from classes.registros_db import Registro_DB
from datetime import datetime
from datetime import date

if __name__ == '__main__':

    password = "Projeto_Final_RT_2195"
    database = "project_rt"
    db = BancoDados(host="localhost", user="root", password=password, database=database)
    db.connect()
    print(db.connection)
    client_db = Clientes_DB(db)
    register_db = Registro_DB(db)

    # teste de adicionar novos clientes
    #new_cliente = Cliente("Marcos Cabrera Neto", "21951799", "2195", "2")
    #client_db.insertClient(new_cliente)

    id_client = client_db.getID_nameCLient("Vinicius Patricio Medeiros da Silva")
    permission_client = client_db.getPermission_nameClient("Vinicius Patricio Medeiros da Silva")
    print(id_client, permission_client)
    #teste - adicionar o novo registro

    date_now = datetime.now()
    #new_register = Registro(id_client, date_now, "Entrada")
    #register_db.insertRegister(new_register)
    print(register_db.lastRegister(id_client))
    #data1 = '2023-03-01 16:22:13'
    #data2 = '2023-03-01 16:38:46'
    #print(register_db.dateClient(data1, data2, id_client))

    #to_day = date.today()
    #print(to_day)
    #days_of_week = to_day.weekday()
    #print(days_of_week)