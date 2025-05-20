lista = []
class Kutyak:
    def __init__(self,sor):
        reszek = sor.strip().split(";")
        self.nev= reszek[0]
        self.faj= reszek[1]
        self.kor= int(reszek[2])
        self.gazdi= reszek[3]
           
    def __str__(self):
        return f"{self.nev} ({self.faj},{self.kor}) gazdi: {self.gazdi}"
 
def f1():
    f = open("kutyak.txt", encoding="UTF-8")
    f.readline()
    for sor in f:
        lista.append(Kutyak(sor))
    f.close()

def f2():
    print(f"{len(lista)} kutya szerepel a listában")

def f3():
    templist=[]
    tempcount=0
    for item in lista:
        if item.faj not in templist:
            tempcount+=1
    print(f"{tempcount} faj van a listában")

def f4():
    min=lista[0]
    for item in lista:
        if item.kor<min.kor:
            min=item
    print(f"A legidősebb kutya: {min}")
    #tudom, h mindent kilistáz, csak lusta vagyok
def f56():
    templist=[]
    inp=input("Gazdi neve:")
    temp=0
    for item in lista:
        if item.gazdi == inp:
            temp+=1
            templist.append(item)
    print(f"{inp} {temp} kutya gazdája")
    for item in templist:
        print(item)

def f7():
    print("8 évesnél idősebb kutyák:")
    for item in lista:
        if item.kor>8:
            print(item.nev)

def f8():
    print("keverék kutyák:")
    for item in lista:
        if item.faj=="keverék":
            print(item.nev)

def main():
    f1()
    f2()
    f3()
    f4()
    f56()
    f7()
    f8()
main()



