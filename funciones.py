import os
import sqlite3

class Principal:
    """docstring for principal"""
    def __init__(self,nombre="",domicilio="",nombre_papas="",doctor="",
        importe=0,cantidad=0,total=0,concepto=""):

        super(Principal, self).__init__()
        self.nombre = nombre
        self.domicilio = domicilio
        self.nombre_papas = nombre_papas
        self.doctor = doctor
        self.importe = importe
        self.cantidad = cantidad
        self.total = total
        self.concepto = concepto

    def conec(self):

        conn = sqlite3.connect('Clientes.db')
        cur = conn.cursor()

        try:

            sql = (""" CREATE TABLE data (id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
                nombre TEXT NOT NULL, domicilio TEXT NOT NULL, nombre_papas TEXT NOT NULL,
                doctor TEXT NOT NULL, importe TEXT NOT NULL, cantidad TEXT NOT NULL,
                total TEXT NOT NULL, concepto TEXT NOT NULL)""" )

            conn.execute(sql)
            conn.commit()

            print("La BDD se creo correctamente")

            key = input("Oprima una tecla para continuar")

        except sqlite3.OperationalError:

            print("Abriendo Base de Datos")

    def new_record(self,nombre,domicilio,nombre_papas,doctor,
        importe,cantidad,total,concepto,id):

        self.conn = sqlite3.connect('Clientes.db')
        self.cur = self.conn.cursor()

        sql = ''' INSERT INTO data (nombre, domicilio, nombre_papas,
            doctor, importe, cantidad,total, concepto) VALUES (?,?,?,?,?,?,?,?) '''

        self.cur.execute(sql,[nombre,domicilio,nombre_papas,doctor,importe,cantidad,total,concepto])
        self.conn.commit()

        key = input("Se inserto Registro con Exito....Presiona una tecla para cotinuar")

    def updaterecord(self,nombre,domicilio,nombre_papas,doctor,
        importe,cantidad,total,concepto,id):

        self.conn = sqlite3.connect('Clientes.db')
        self.cur = self.conn.cursor()

        sql = (''' UPDATE data SET nombre = ?,domicilio =?,nombre_papas=?,doctor=?,importe=?,
        cantidad=?,total=?,concepto=? WHERE id =?''')

        self.cur.execute(sql,[nombre,domicilio,nombre_papas,doctor,importe,cantidad,total,concepto,id])

        self.conn.commit()

        tecla = input("Registro Actualizado Correctamente presione una tecla para continuar.....")

    def delete(self,id):

        self.conn = sqlite3.connect('Clientes.db')
        self.cur = self.conn.cursor()

        sql = ('DELETE FROM data WHERE id = ?')

        self.cur.execute(sql,[id])
        self.conn.commit()

        tecla = input("Registro Borrado con Exito.. presiona una tecla para continuar......")

        
