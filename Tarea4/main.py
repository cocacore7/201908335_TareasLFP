import webbrowser

lista = ["Nombre: Oscar", "Edad: 20", "Activo: True", "Saldo: 100", "Nombre: Mario", "Edad: 20", "Activo: False",
         "Saldo: 300", "Nombre: Tito", "Edad: 25", "Activo: True", "Saldo: 1200", "Nombre: Beto", "Edad: 27",
         "Activo: False", "Saldo: 800"]


def reporte(Datos):
    entrada = input("Escriba reportar: ")
    comando = entrada.lower()
    if comando == "reportar":
        with open('reporte.html', 'w') as miarchivo:
            miarchivo.write('<!DOCTYPE html>' + "\n")
            miarchivo.write('<html lang="en">' + "\n")
            miarchivo.write('<head>' + "\n")
            miarchivo.write('   <meta charset="UTF-8">' + "\n")
            miarchivo.write('   <title>Document</title>' + "\n")
            miarchivo.write('   <style type="text/css">' + "\n")
            miarchivo.write('       body{background: url(fondo4.jpg);background-size: 100%;}' + "\n")
            miarchivo.write('h4{width: 400px;height: 40px;line-height: 60px;text-align: center;background: yellow;}'
                            + "\n")
            miarchivo.write('h3{width: 400px;height: 40px;line-height: 60px;text-align: center;background: SkyBlue;}'
                            + "\n")
            miarchivo.write('   </style>' + "\n")
            miarchivo.write('</head>' + "\n")
            miarchivo.write('<body>' + "\n")
            miarchivo.write('<center>' + "\n")

            for archivo in Datos:
                miarchivo.write("<h3>" + archivo + "</h3>" + "\n")
            miarchivo.write('</center>' + "\n")
            miarchivo.write('</body>' + "\n")
            miarchivo.write('</html>')
            miarchivo.close()
            print("Reporte Creado")
            webbrowser.open("reporte.html")

    else:
        print("Comando Invalido")
        reporte(Datos)


reporte(lista)
