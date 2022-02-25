import os
import sqlite3


class Doctores:

    """docstring for Doctores"""

    def __init__(self, nombre_dr ="",domicilio_dr="",telefono_dr="",email_dr=""):
        super(Doctores, self).__init__()
        self.nombre_dr = nombre_dr
        self.domicilio_dr = domicilio_dr
        self.telefono_dr = telefono_dr
        self.email_dr = email_dr

    def upgrade_doctores(self,nombre_dr,domicilio_dr,telefono_dr,email_dr,id):

        conn = sqlite3.connect('Doctores.db')
        cur = conn.cursor()

        sql = (""" INSERT INTO data_dres (nombre_dr,domicilio_dr,telefono_dr,email_dr) VALUES(?,?,?,?)""")
        cur.execute(sql,[nombre_dr,domicilio_dr,telefono_dr,email_dr])
        conn.commit()

    def db_doctores(self):

        conn = sqlite3.connect('Doctores.db')
        cur = conn.cursor()

        try:

            sql = (""" CREATE TABLE data_dres (id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
                   nombre_dr TEXT NOT NULL, domicilio_dr TEXT NOT NULL, telefono_dr TEXT NOT NULL,
                   email_dr TEXT NOT NULL)""" )

            conn.execute(sql)
            conn.commit()

            print("La BDD se creo correctamente")
            key = input("Oprima una tecla para continuar")

        except sqlite3.OperationalError:

            print("Abriendo Base de Datos")

    def dres_update(self,nombre_dr,domicilio_dr,telefono_dr,email_dr,id):

        conn = sqlite3.connect('Doctores.db')
        cur = conn.cursor()

        sql = ('''UPDATE data_dres SET nombre_dr = ?, domicilio_dr = ?, telefono_dr = ?, email_dr = ?
            WHERE id = ?''')

        cur.execute(sql,[nombre_dr,domicilio_dr,telefono_dr,email_dr,id])
        conn.commit()

        tecla = input('Registro modificado correctamente.....Presiona una tecla para continuar....')

    def dres_delete(self,id):

        conn = sqlite3.connect('Doctores.db')
        cur = conn.cursor()

        sql = ('''DELETE FROM data_dres WHERE id = ?''')

        cur.execute(sql,[id])
        conn.commit()

        tecla = input('Registro Elimidado correctamente.....Presiona una tecla para continuar....')


            