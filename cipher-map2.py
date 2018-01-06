def recall_password(cipher_grille, ciphered_password):
    s1, s2, s3, s4 = cipher_grille
    print(s1.index('X'))
    print(s2.index('X'))
    print(s3.index('X'))
    print(s4.index('X'))
    return ""


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
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
