from functions import add_file
CREATE="a.Crear un fitxer."
SHOW="b.Mostrar el contingut d'un fitxer per pantalla."
MODIFY="c.Modificar el contingut d'un fitxer."
EXIT="d.Sortir"
LETRA="Introdueix la lletra de lo que vols fer:"
CR="Has escollit Crear un fitxer"
NAME="Introdueix el nom del fitxer:"
SH="Has escollit Mostrar el contingut d'un fitxer per pantalla"
MO="Has escollit Modificar el contingut d'un fitxer."
EX="Has escollit sortir." \
   "  Adéu! :)"
def main():
    print(CREATE)
    print(SHOW)
    print(MODIFY)
    print(EXIT)
    x=input(LETRA)
    match x:
        case 'a':
            print(CR)
            file_name=input(NAME)
            add_file('files/'+file_name)
        case 'b':
            print(SH)
            file_name= input(NAME)
            show_file('files/'+file_name)
        case 'c':
            print(MO)
            file_name = input(NAME)
            modify_file('files/'+file_name)
        case 'd':
            print(EX)
if __name__ == '__main__':
   main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
