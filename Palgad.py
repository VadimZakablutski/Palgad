from module import*
palk=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
def palgad(p,i):
    valik=input("Средняя зарплата - 1,\nМинимальная зарплата - 2,\nМаксимальная зарплата - 3,\nУдалить человека - 4,\nСортировка - 5, \nДобавить человека - 6\n")
    if valik=="1":
        kesk_palk=round(keskmine(palk),2)
        print("Keskmine palk on ",kesk_palk)
        print()
        print()
    elif valik=="2":
        m_palgad,nimi=minimum(palk,inimesed)
        for n in nimi:
            print(m_palgad[0], " будет получено ",n)
            print()
            print()
    elif valik=="3":
        max_palk,kto=maksimum(palk,inimesed)
        print("Максимальная зарплата ", max_palk, " будет получено ",kto)
        print()
        print()
    elif valik=="4":                                       
        p,i=delete(palk,inimesed)
        print(palk,inimesed)
        if len(inimesed)==0:
            print("Tühi list")
        else:
            for i in range(len(inimesed)):
                print(inimesed[i]," saab kätte ", palk[i])
    elif valik=="5":
        p,i=sorteerimine(palk,inimesed)
        for i in range(len(inimesed)):
            print(inimesed[i]," будет получено ", palk[i])
            print()
            print()
    elif valik=="6":                                        
        i=adding(palk,inimesed)
        print("Обновлённые списки: ")
        print(inimesed)
        print(palk)
        print("Добавлен элемент", inimesed[-1])
        print("С зарплатой", str(palk[-1])+'€')

    elif valik == '7':
        bog, bog_p, bed, bed_p = top3(palk,inimesed,n)
        print("3 самых богатых")
        for i in range(3):
            print(b1[i],'получает',str(b2[i])+'€')
        print()
        print("3 самых бедных")
        for i in range(3):
            print(b4[i],'получает',str(b3[i])+'€')
    elif valik=="4":
        p=võrdlus()
        print(result)
while True:
    palgad(palk,inimesed)