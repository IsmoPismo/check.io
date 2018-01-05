def Descending_Order(num):
    lista = []
    brojevi = str(num)
    rezultat = ''
    for i in brojevi:
        lista.append(i)

    lista = sorted(lista, reverse=True)
    for i in lista:
        rezultat+=i

    return int(rezultat)

print(Descending_Order(123))
