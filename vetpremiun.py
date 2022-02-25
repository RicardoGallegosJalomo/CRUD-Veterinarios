# Esta aplicación lleva el control de un Hospital Veterinario

import os
import sqlite3
import funciones
import funcionesdoctores

condicion = True

while condicion:

    os.system('cls')

    print("**************************************************************************************************************************")
    print("*                                                                                                                        *")
    print("*                 C O N T R O L      H O S P I T A L A R I O     Y     H O T E L     V E T E R I M A R I O               *")
    print("*                                                                                                                        *")
    print("**************************************************************************************************************************\n")

    key = 0

    print("                                         ********************************")
    print("                                         *                              *")
    print("                                         *  M E N U  P R I N C I P A L  *")
    print("                                         *                              *")
    print("                                         ********************************\n")

    print("                                         -----> 1.- Nuevo Registro  <---- \n")
    print("                                         -----> 2.- Editar Registro <---- \n")
    print("                                         -----> 3.- Borrar Registro <---- \n")
    print("                                         -----> 4.- Consultar Registro <- \n")
    print("                                         -----> 5.- Doctores        <---- \n")
    print("                                         -----> 6.- Ajustes         <---- \n")
    print("                                         -----> 7.- Hotel           <---- \n")
    print("                                         -----> 8.- Salir           <---- \n")

    key = int(input("Elija una opción -------- : "))

    if key == 1:

        os.system('cls')

        respuesta = ""

        nombre = input("Nombre de la Mascota......: ")
        domicilio = input("Domicilio...: ")
        nombre_papas = input("Nombre de los Padres.....: ")
        doctor = input("Dr. que atiende...: ")
        importe = input("Importe......: ")
        cantidad = input("Cantidad....: ")
        total = input("Total a pagar......: ")
        concepto = input("Tratamiento o padecimiento.....: ")
         
        respuesta = input("Sus Datos son Correctos......S/N.: ")

        if respuesta == "S":

            pclase = funciones.Principal()
            pclase.conec()
            pclase.new_record(nombre,domicilio,nombre_papas,doctor,importe,cantidad,total,concepto,id)

        else:
            
            key = input("Oprima cualquier tecla para volver a Capturar.....")

    if key == 2:

        pclase = funciones.Principal()
        pclase.conec()

        conn = sqlite3.connect('Clientes.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM data')

        for row in cur:
            print(row)

        id = input("Esciba el ID que quiere Modificar.....: ")

        respuesta = ""

        nombre = input("Nombre de la Mascota......: ")
        domicilio = input("Domicilio...: ")
        nombre_papas = input("Nombre de los Padres.....: ")
        doctor = input("Dr. que atiende...: ")
        importe = input("Importe......: ")
        cantidad = input("Cantidad....: ")
        total = input("Total a pagar......: ")
        concepto = input("Tratamiento o padecimiento.....: ")
         
        respuesta = input("Sus Datos son Correctos......S/N.: ")

        if respuesta == "S":

            pclase = funciones.Principal()
            pclase.conec()
            pclase.updaterecord(nombre,domicilio,nombre_papas,doctor,importe,cantidad,total,concepto,id)

        else:
            
            key = input("Oprima cualquier tecla para volver a Capturar.....")


        pass

    if key == 3:

        pclase = funciones.Principal()
        pclase.conec()

        conn = sqlite3.connect('Clientes.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM data')

        for row in cur:
            print(row)

        id = input("Esciba el ID que quiere Eliminar.....: ")

        pclase.delete(id)

    if key == 4:

        pclase = funciones.Principal()
        pclase.conec()

        conn = sqlite3.connect('Clientes.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM data')

        for row in cur:
            print(row)

        id = input("Oprima una tecla para continuar.....")

    if key == 5:

        os.system('cls')

        print("**************************************************************************************************************************")
        print("*                                                                                                                        *")
        print("*                 C O N T R O L      H O S P I T A L A R I O     Y     H O T E L     V E T E R I M A R I O               *")
        print("*                                                                                                                        *")
        print("**************************************************************************************************************************\n")

        keydoctores = 0

        print("                                         ********************************")
        print("                                         *                              *")
        print("                                         *  M E N U    D O C T O R E S  *")
        print("                                         *                              *")
        print("                                         ********************************\n")

        print("                                         -----> 1.- Nuevo Registro  <---- \n")
        print("                                         -----> 2.- Editar Registro <---- \n")
        print("                                         -----> 3.- Borrar Registro <---- \n")
        print("                                         -----> 4.- Consultar Registro <- \n")
        print("                                         -----> 5.- Salir           <---- \n")

        keydoctores = int(input("Elija una opción -------- : "))

        if keydoctores == 1:

            drclase = funcionesdoctores.Doctores()
            drclase.db_doctores()

            nombre_dr = input("Nombre del Doctor....: ")
            domicilio_dr = input("Dirección.....: ")
            telefono_dr = input("Telefono.....: ")
            email_dr = input("Email....: ")

            question = input("Sus Datos son correctos.....: ")

            if question == "S":

                drclase.upgrade_doctores(nombre_dr,domicilio_dr,telefono_dr,email_dr,id)

            else:

                continue

        if keydoctores == 2:

            drclase = funcionesdoctores.Doctores() # ABRE BASE DE DATOS DE DOCTORES
            drclase.db_doctores()

            conn = sqlite3.connect('Doctores.db')
            cur = conn.cursor()

            cur.execute('SELECT * FROM data_dres')

            for row in cur:
                print(row)

            id = input("\n Digite el ID que desea modificar...: ")

            nombre_dr = input("Nombre del Doctor....: ")
            domicilio_dr = input("Dirección.....: ")
            telefono_dr = input("Telefono.....: ")
            email_dr = input("Email....: ")

            question = input("Sus Datos son correctos.....: ")

            if question == "S":

                drclase.dres_update(nombre_dr,domicilio_dr,telefono_dr,email_dr,id)

            else:

                continue

        if keydoctores == 3:

            drclase = funcionesdoctores.Doctores()
            drclase.db_doctores()

            conn = sqlite3.connect('Doctores.db')
            cur = conn.cursor()

            cur.execute('SELECT * FROM data_dres')

            for row in cur:
                print(row)

            id = input("\n Digite el ID que desea Eliminar...: ")

            drclase.dres_delete(id)

        if keydoctores == 4:

            drclase = funcionesdoctores.Doctores()
            drclase.db_doctores()

            conn = sqlite3.connect('Doctores.db')
            cur = conn.cursor()

            cur.execute('SELECT * FROM data_dres')

            for row in cur:
                print(row)

            id = input("\n Oprima cualquier tecla para continuar...")

        if keydoctores == 5:

            continue

    if key == 6:

        pass

    if key == 7:

        pass

    if key == 8:

        condicion = False