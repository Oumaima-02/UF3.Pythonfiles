import csv
MSG="Indica el nom del fitxer:"
MSG02="Nom incorrecte del fitxer. Torna a introduir-lo: "
MSG03="Has fet ja 3 intentsm no pots fer més."
def fileval():
    file = input(MSG)
    i = 0
    while i <= 3:
        if file != 'Registre':
            print(MSG02)
            file = input(MSG)
            i += 1
        elif file == 'Registre':
            return file
    if i == 3:
        print(MSG03)
def llegircsv(file):
    with open (f'files/{file}.csv')as csvfile:
        readCSV=csv.reader(csvfile,delimiter=';')



def afegircsv():
    text=input("Que vols escriure?")
    with open (f'files/{file}.csv','a')as csvfile:
        writeCSV=csv.write(csvfile,delimiter=';', quotechar='"',)
