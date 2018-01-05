def checkio(first, second):
    f_list = first.split(',')
    s_list = second.split(',')
    result_list = []
    stringic = ''
    
    for i in f_list:
        if i in s_list:
          result_list.append(i)

    result_list.sort()

    for x in range(len(result_list)):
        if len(result_list) <= 1:
            stringic += result_list[x]
        elif len(result_list) > 1:
            if x < len(result_list)-1:
                stringic += result_list[x] + ','
            else:
                stringic += result_list[x]

    return stringic
        

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
