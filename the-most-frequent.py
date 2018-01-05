def most_frequent(data):
    from collections import defaultdict

    words = ' '.join(data)

    d = defaultdict(int)
    for word in words.split():
        d[word] += 1

    max_value = (max(d.values()))
    for k in d:
        if d[k]==max_value:
            return k

    #GENIUS:
        '''
        return sorted(data, key=data.count)[-1]
        
    #Another GREAD WAY
    
        occurances = {}
            for s in data:
            occurance = occurances.get(s, 0)
            occurances[s] = occurance + 1
        return max(occurances, key=occurances.get)
        '''

if __name__ == '__main__':
    most_frequent(['a','b','a'])


    print('Done')
