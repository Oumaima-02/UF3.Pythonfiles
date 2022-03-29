def add_file(fname, text):
    file = open(fname, 'a+')
    file.write(text)
    print(file.read())
    file.close()
