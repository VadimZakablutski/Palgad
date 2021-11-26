def adding(palk,inimesed):
    add=input("Имя человека:  ")
    inimesed.append(add)
    add_palk=int(input("Зарплата человека:  " ))
    palk.append(add_palk)
    return palk,inimesed
    print()
    print()
def kustuta(palk,inimesed):
    uus_palk = []; uus_inimesed = []
    kesk = keskmine(palk)
    for p in palk:
        if p > kesk:
            nr = palk.index(p)
            uus_palk.append(p)
            uus_inimesed.append(inimesed[nr])
    palk.clear();inimesed.clear()
    for i in range(len(uus_palk)):
        palk.append(uus_palk[i])
        inimesed.append(uus_inimesed[i])
    return uus_palk, uus_inimesed
def maksimum(palk,inimesed):
    m_palgad=[]
    nimed=[]
    max_palk=palk[0]
    kellel=inimesed[0]
    for p in palk:
        if p>max_palk:
            max_palk=p
            i=palk.index(max_palk)
            kellel=inimesed[i]
            print()
            print()
    n=palk.count(max_palk)
    palk_copy=palk.copy()
    inimesed_copy=inimesed.copy()
    for i in range(n):
        j=palk_copy.index(max_palk)
        m_palgad.append(palk_copy.pop(j))
        nimed.append(inimesed_copy.pop(j))
    return m_palgad, nimed
    print()
    print()
def minimum(palk,inimesed):
    m_palgad=[]
    nimed=[]
    min_palk=palk[0]
    kellel=inimesed[0]
    for p in palk:
        if p<min_palk:
            min_palk=p
            i=palk.index(min_palk)
            kellel=inimesed[i]
    n=palk.count(min_palk)
    palk_copy=palk.copy()
    inimesed_copy=inimesed.copy()
    for i in range(n):
        j=palk_copy.index(min_palk)
        m_palgad.append(palk_copy.pop(j))
        nimed.append(inimesed_copy.pop(j))
    return m_palgad, nimed
    print()
    print()
def keskmine(palk):
    summa=0
    n=len(palk)
    for p in palk:
        summa+=p
    k=summa/n
    return k
    print()
    print()
def kalk():
    print("Это калькулятор) Поможет со сложными вычислениями")
    while True:
        print("Выберите действие которое хотите сделать:\n"
              "Сложить: +\n"
              "Вычесть: -\n"
              "Умножить: *\n"
              "Поделить: /\n"
              "Выйти: q\n")
        action = input("Действие: ")
        if action == "q":
            print("Выход из программы")
            break
        if action in ('+', '-', '*', '/'):
            x = float(input("x = "))
            y = float(input("y = "))
            if action == '+':
                print('%.2f + %.2f = %.2f' % (x, y, x+y))
            elif action == '-':
                print('%.2f - %.2f = %.2f' % (x, y, x-y))
            elif action == '*':
                print('%.2f * %.2f = %.2f' % (x, y, x*y))
            elif action == '/':
                if y != 0:
                    print('%.2f / %.2f = %.2f' % (x, y, x/y))
                else:
                    print("Нельзя на 0 делить")