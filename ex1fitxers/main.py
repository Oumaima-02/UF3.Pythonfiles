from functions import add_file
def main():
    text=input("Que vols afegir al fitxer?")
    while len(text)>100:
        print("Text ha de tenir menys de 100 caràcters ")
        text = input("Que vols afegir al fitxer?")
    add_file("files/text.txt", text)
if __name__ == '__main__':
    main()
