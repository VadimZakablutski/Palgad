def adding():
    #Программа добавляет в списки имя и зарплату
    #esimene arv nimi: str
    #teine arv - palk: int 
    #rtype var:
	nimi=input("Введите имя: ")
	palk=input("Введите зарплату: ")
	with open("login.txt", "a") as inimesed:
		inimesed.write(nimi+"\n")	
	with open("palgad.txt", "a") as palgad:
		palgad.write(palga+"\n")

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
def maks():
	palgad=[]
	with open("palgad.txt", "r") as f1:
		for stro in f1:
			palgad.append(stro.strip())
	f=open("login.txt", "r")
	inimesed=[]
	for stroka in f:
		inimesed.append(stroka.strip())
	f.close
	zp=palgad.copy()
	zp.sort()
	a=zp[0]
	b=palgad.index(a)
	print("Самая большая зарплата у "+inimesed[b])
def smallest_salary():
	palgad=[]
	with open("palgad.txt", "r") as f1:
		for strok in f1:
			palgad.append(strok.strip())
	inimesed=[]
	with open ("login.txt", "r") as inimene:
		for stroka in f:
			inimesed.append(stroka.strip())
	zp=palgad.copy()
	zp.sort()
	zp.reverse()
	a=zp[0]
	b=palgad.index(a)
	print("Самая маленькая зарплата у "+inimesed[b])
def keskmine():
    """
    Программа проверяет списки и выводит среднюю зарплату
    rtype var:
    """
    sum=0
    for palk in p:
        sum+=palk
    keskm=sum/len(p)
    print(keskm)
    v=0
    if 0<p.index(keskm)<len(p)-1:
        kesk=i(p.index(keskm))
        return keskm
    else:
        print("Kesk on puudub")
        return keskm
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