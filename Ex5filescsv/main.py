import functions as f
MSG2="1.Llegir CSV"
MSG3="2.Afegir CSV"
MSG4="Indica que vols fer:"

def main():
    print(MSG2)
    print(MSG3)
    num=int(input(MSG4))
    match num:
        case 1:
            file=f.fileval()
            f.llegircsv(file)
        case 2:
            file = f.fileval()
            f.afegircsv(file)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
