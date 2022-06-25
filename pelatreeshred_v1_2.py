#pelatreeshred v 1.12

# este programa llena de basura archivos y los renombra con nombres aleatorios
# antes de borrarlos, luego, renombra las carpetas con nombres aleatorios y
# las borra.
#
#    NOTA: este programa afecta a todos el arbol de carpetas desde la direccion
#          de donde se ejecuta

# Descripción del funcionamiento:
#
# 1. presentacion del titulo del programa
# 2. Verificación de que existe el comando shred, el cual se usa para
#    sobreescribir con datos basura los archivos
# 3. pregunta si se está seguro de destruir la información
# 4. Se destruyen y borran los archivos, desde los que se encuentran
#    mas profundos en el arbol de carpetas hasta el directorio
#    en donde se ejecuta este programa ( incluso se destruye
#    el archivo del programa )
# 5. Se destruyen las carpetas hasta el lugar en donde se ejecuta el programa

# Versiones
# v1.1 : Es la primer versión operativa
# v1.2 : Solo cambia algunas decoraciones de los primeros titulos


#presentación del programa

print("\r")
print("                          <>               ")
print("                        <<<>>>               ")
print("                     <<<<<<>>>>>>               ")
print("                <<<<<<<<<<<>>>>>>>>>>               ")
print("          <<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>\r")
print("       <<<<<<<   Pela Tree Shred v1.2   >>>>>>")
print("          <<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>\r")
print("                <<<<<<<<<<<>>>>>>>>>>               ")
print("                     <<<<<<>>>>>>                   ")
print("                        <<<>>>               ")
print("                          <>               ")
print("\r")

#importando librerias necesarias
import subprocess
import os
import sys

#verificacion de que shred existe
print("Verificando que shred esta disponible")
rc = subprocess.call(['which', 'shred'])
if rc == 0:
    print("\r")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("el comando shred se encuentra disponible!")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("\r")
else:
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("el comando shred NO se encuentra disponible")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("\r")
    sys.exit(1)

#pregunta si esta seguro de borrar los archivos y carpetas
seguro_de_borrar = True
while seguro_de_borrar:
    choice = input('ESTA SEGURO DE DESTRUIR LOS ARCHIVOS Y CARPETAS? (s/n) ')
    if choice == 's':
        print("\r")
        print("  ----------------------------------\r")
        print("  comenzar a destruir la informacion\r")
        print("  ----------------------------------")
        print("\r")
        seguro_de_borrar = False
    elif choice == 'n':
        print("\r")
        print("  saliendo del programa")
        print("\r")
        sys.exit(1)
    else:
        seguro_de_borrar = True
        print("\r")
        print("ingrese 's' o 'n' ")
        print("\r")

#comenzar con el trabajo de archivos y directorios
print("\rrecorriendo archivos y carpetas")

#recorrer el arbol de directorios con os.walk y aplicar los cambios por cada resultado
for root, dirs, files in os.walk(".", topdown=False):

######################################################################
#bucle para trabajar con los archivos
    for name in files:

#bucle para generar los nombres random para los archivos
        from string import ascii_letters, punctuation, digits
        from random import choice, randint
        min = 6
        max = 15
        string_format = ascii_letters + digits
        generated_string = "".join(choice(string_format) for x in range(randint(min, max)))
#        print("Your String is: {0}".format(generated_string))

#introducir los comandos dentro de variables para que subprocess.call los pueda interpretar
        command1 = "shred"
        command1_argument1 = "-v"
        command1_argument2 = "-u"
        command2 = "mv"
        command3 = "rm"
        command3_argument1 = "-f"

#introducir el nombre del archivo dentro de una variable para que subprocess.call lo pueda interpretar
        fn = (os.path.join(root, name))

#ejecutar los cambios a los archivos
        print("destrozando el archivo {0}".format(fn))
        subprocess.call([command1, command1_argument1, fn])
        print("Renombrando el archivo {0} por {1}".format(fn, generated_string))
        subprocess.call([command2, fn, generated_string])
        print("borrando el archivo {0}".format(generated_string))
        subprocess.call([command3, command3_argument1, generated_string])

######################################################################
#bucle for para trabajar con las carpetas
    for name in dirs:

#bucle para generar los nombres random para las carpetas
        from string import ascii_letters, punctuation, digits
        from random import choice, randint
        min = 6
        max = 15
        string_format = ascii_letters + digits
        generated_string = "".join(choice(string_format) for x in range(randint(min, max)))
#        print("Your String is: {0}".format(generated_string))

#introducir los comandos dentro de variables para que subprocess.call los pueda interpretar
        command2 = "mv"
        command4 = "rmdir"
        dn = (os.path.join(root, name))

#ejecutar los cambios en las carpetas
        print("Renombrando la carpeta {0} por {1}".format(dn, generated_string))
        subprocess.call([command2, dn, generated_string])
        print("borrando la carpeta {0}".format(generated_string))
        subprocess.call([command4, generated_string])

