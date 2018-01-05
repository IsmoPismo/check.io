def checkio(number):
    
    djeljitelj = 10
    broj = 1
    pomocna_lista=[0,1,2,3,4,5]
    pomocna_var=0
    for pomocna_var in range(len(pomocna_lista)):
        if number % djeljitelj == 0:
            broj *= 1
            number /= 10
        else:
            broj *= (number % djeljitelj)
            number -= (number % djeljitelj)
            number /= 10
    return int(broj)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio(1203))
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
