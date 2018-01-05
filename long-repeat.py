def long_repeat(line):
    try:
        a = line[0]
    except IndexError:
        pass
    max_sub_str = 0
    try:
        for i in range(len(line)):
            if line[i] == line[i+1]:
                    a += line[i+1]
                    if len(a) > max_sub_str:
                        max_sub_str = len(a)
                    
            else:
                if len(a) > max_sub_str:
                    max_sub_str = len(a)
                a = line[i]
    except IndexError:
        pass

    return max_sub_str
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
