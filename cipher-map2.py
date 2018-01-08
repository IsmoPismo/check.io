def recall_password(cipher_grille, ciphered_password):
    encrypted = ''
    index = 0
    index2 = 0
    for n in range(4):
        for i, row in enumerate(cipher_grille):
            if row.count('X') == 1:
                index = row.index('X')
                encrypted += ciphered_password[i][index]
            if row.count('X') == 2:
                index = row.index('X')
                help_index = index + 1
                index2 = row[help_index:].index('X') + index + 1
                encrypted += ciphered_password[i][index] + ciphered_password[i][index2]
        cipher_grille = zip(*cipher_grille)

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
