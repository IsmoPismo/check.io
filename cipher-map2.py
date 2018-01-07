def recall_password(cipher_grille, ciphered_password):
    encrypted = ''
    index = 0
    index2 = 0
    for i, row in enumerate(cipher_grille):
        if row.count('X') == 1:
            index = row.index('X')
            encrypted += ciphered_password[i][index]
        if row.count('X') == 2:
            index = row.index('X')
            index2 = row[index:].index('X') + index #Ovdje si stao, treba skontat drugi index
            encrypted += ciphered_password[i][index] + ciphered_password[i][index2]

    return encrypted



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(recall_password((
         'X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')))

    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
