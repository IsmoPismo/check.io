def index_power(array, n):

    if n < len(array):
        return array[n]**n
    else:
        return -1

'''
    KRETAK NAČIN
    try: return array[n] ** n
    except IndexError: return -1
'''

if __name__ == '__main__':
    print (index_power([1,2,10,4],3))
    print(index_power([1,3,10,100],3))
