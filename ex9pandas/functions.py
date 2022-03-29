import pandas as pd
import functions as f
MSG1="Identificador:"
MSG2="Grup/Cantant:"
MSG3="Nom cançó:"
MSG4="Data publicació:"
MSG5="Nombre de visualitzacions: "
MSG7="Torna a introduir-lo."
def dades():
    dicti=dict()
    dicti["Identificador"] = f.val_num(int(input(MSG1)))
    dicti["Grup/cantant"] = f.val_str(input(MSG2))
    dicti["Nom"] = f.val_str(input(MSG3))
    print('data:')
    dia=int(input('dia:'))
    mes = int(input('mes:'))
    any = int(input('any:'))
    dicti["Data pub."] = (f'{dia}/{mes}/{any}')
    dicti["Visualitzacions"] = f.val_num(int(input(MSG5)))
    return dicti

def val_num(var):
    while var < 0:
        print('No es vàlid aquest número! :(')
        var=int(input(MSG7))
    if  var>=0:
        return var
def val_str(var):
    while type(var)!=str:
        print(' No és un string')
        var = input(MSG7)
    if type(var)==str:
        return var
def mostrar(csv):
    df=pd.read_csv(csv)
    print(df)
