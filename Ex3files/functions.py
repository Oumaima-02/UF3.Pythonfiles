def add_file(fname):
   file = open(fname, 'a+')
   file.write()
   print(file.read())
   file.close()

def show_file(fname):
   file=open(fname,"r")
   print(file.read())
   file.close()

def  modify_file(fname):
   file = open(fname, 'a+')
   file.write()
   print(file.read())
   file.close()
