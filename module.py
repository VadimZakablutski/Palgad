def adding():
    #Программа добавляет в списки имя и зарплату
    #esimene arv nimi: str
    #teine arv - palk: int 
    #rtype var: str
	nimi=input("Введите имя: ")
	palk=input("Введите зарплату: ")
	with open("login.txt", "a") as inimesed:
		inimesed.write(nimi+"\n")	
	with open("palgad.txt", "a") as palgad:
		palgad.write(palk+"\n")
def maks():
     #Программа проверяет списки и выводит на экран человека с максимальной зарплатой
    #rtype var: int
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
def min():
    #Программа проверяет списки и выводит на экран человека с самой маленькой зарплатой
    #rtype var: int
	palgad=[]
	with open("palgad.txt", "r") as f1:
		for strok in f1:
			palgad.append(strok.strip())
	inimesed=[]
	f=open("login.txt", "r")
	inimesed=[]
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
    Программа проверяет списки и выводит на экран среднюю зарплату
    rtype var:int
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
        print("Нет средней зарплаты")
        return keskm