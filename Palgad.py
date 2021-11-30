from module import*
palk=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
def palgad(p,i):
    valik=input("Средняя зарплата - 1,\nМинимальная зарплата - 2,\nМаксимальная зарплата - 3,\nУдалить человека - 4,\nДобавить человека - 5\nСвоя функция - 6.\n ")
    if valik=="1":
        keskmine()
    elif valik=="2":
        min()
    elif valik=="3":
        maks()
    elif valik =="4":
        p,i=kustuta(palk,inimesed)
        print("Удалены данные, где зарплата ниже средней")
        for i in range(len(p)):
            print(inimesed[i],"получает", str(palk[i])+'€')
    elif valik=="5":
        adding()
    elif valik=="6":
        x,y=kalk()
while True:
    palgad(palk,inimesed)