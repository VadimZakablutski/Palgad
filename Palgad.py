from module import*
palk=[1200,2500,750,749,1200]
inimesed=["A","B","C","D","E"]
def palgad(p,i):
    valik=input("Средняя зарплата - 1,\nМинимальная зарплата - 2,\nМаксимальная зарплата - 3,\nДобавить человека - 4\n ")
    if valik=="1":
        keskmine()
    elif valik=="2":
        min()
    elif valik=="3":
        maks()
    elif valik=="4":
        adding()
while True:
    palgad(palk,inimesed)