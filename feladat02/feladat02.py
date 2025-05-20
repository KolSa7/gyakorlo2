
lista=[]
def beolvasas():
    f=open("kutyusok.txt", encoding="UTF-8")
    for sor in f:
        lista.append(sor.strip())
    f.close
    print(lista)

def f2():
    print(f"{len(lista)} kutya szerepel a listán")

def f3():
    print("i betűre végzőző nevek:")
    for item in lista:
        if item[-1]=="i":
            print(item)

def f4():
    
    for item in lista:
        tempcount=0
        for bitem in lista:
            if item==bitem:
                tempcount+=1
        if tempcount>1:
            print(f"{item} {tempcount}-szor/szer szerepel a listán")

def f5():
    lista.sort()
    print(f"A kutyák abc sorrendben: {lista}")

def f6():
    f=open("kutyusok_nagy.txt","a", encoding="UTF-8")
    for item in lista:
        f.write(f"{item.capitalize()} \n")
    f.close()

def main():
    beolvasas()
    f2()
    f3()
    f4()
    f5()
    f6()

main()