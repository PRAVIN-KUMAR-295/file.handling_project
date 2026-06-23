from pathlib import Path
import os 
def readfileandfolder( ):
    Path_object = Path('')
    items =list(Path_object.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")

def createfile( ):
   try:
        readfileandfolder()
        name  = input("please tell your file name:--")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("what you  want  to write in  this file:--")
                fs.write(data)

            print(f"FILE CREATED SUCCESSFULlY")
        else:
            print("this file is already exists")
            
   except Exception as err:
       print(f"An error ocrred as {err}")

def readfile():
    try:
     readfileandfolder( )
     name = input("which file you  want to read:--")
     p = Path(name)
     if p.exists( ) and p.is_file( ):
         with open(p,"r") as fs:
             data = fs.read( )
             print(data)

         print("Readed successfully")
     else:
         print("the file is doesn't exists")

    except Exception as err:
        print(f"An error occred as{err} " )

def updatefile():
    try:
        readfileandfolder()
        name = input("tell which file want to update:--")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing  the name of your file:-- ")
            print("press  2 for overwriting the your file:-- ")
            print("press 3 for apending  some contect in your life:-- ")

            res = int(input("tell your response :--"))

            if res ==1 :
                name2 =input("tell your new file name :--")
                p2 = Path(name2)
                p2.rename(p2)

            if res ==2:
                with open(p,"w") as fs:
                    data = input("tell what you want  to write is overwriting the data:--")
                    fs.write(data)

            if res ==3:
                with open(p,"a") as fs:
                    data = input("tell what you want  to append :--")
                    fs.write("    "+data)

    except Exception as err:
        print(f"An error accoured as {err}")

def  deletionfile():
    try:
        readfileandfolder()
        name = input("which want to you file delete:--")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(name)

            print("file removes are successfully ")

        else:
            print("No such file exist")

    except Exception as err:
        print(f"An error accoured as {err}")

    


print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deletion a file")

check = int(input("please tell your response:--"))

if check == 1:
    createfile( )

if check == 2:
    readfile( )

if check == 3:
    updatefile( )

if check == 4:
    deletionfile( )