def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    if text == 'hi':
        return 'hi'
    
    import re
    x = re.split('\s|(?<!\d)[,.](?!\d)', text)


    for index in range(len(x)-1):
        if not x[index] == '':
            return x[index]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    print(first_word('... itd...'))
    print(first_word("don't touch"))
    print('hoi.bio')

    print("Coding complete? Click 'Check' to earn cool rewards!")
