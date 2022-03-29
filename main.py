import functions as f
import csv
MSG="Introdueix el teu nom:"
MSG2="Introdueix el teu cognom:"
MSG3="Introdueix la teva edat:"

def main():
    dict={}
    nom = input(MSG)
    cognom = input(MSG2)
    edat = input(MSG3)
    NOM,COGNOM=f.identificador(nom,cognom)
    ident=NOM+"-"+COGNOM+"-"+edat
    dict["Identificador"]=ident
    dict["Nom"] = nom
    dict["Cognom"] = cognom
    dict["Edat"] = edat
    print(dict)
    infos=list()
    info= input("Intodueix el que vols afegir (per parar introdueix 0): ")
    infos.append(info)
    for x in infos:
        if x == '0':
            print("Has introduit un 0.")

    with open('files/dictio.csv', 'w', encoding='utf-8',newline='') as csvfile:
        fieldnames=['Identificador', 'Nom', 'Cognom', 'Edat']
        writeCSV=csv.DictWriter(csvfile, fieldnames=fieldnames)
        writeCSV.writer(csvfile)
        writeCSV.writer(infos)
        writeCSV.writeheader()
        writeCSV.writerow(fieldnames)
        writeCSV.writerow(dict)
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
