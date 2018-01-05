def best_stock(data):
    a = 0.00
    master_key = ''
    for k, v in data.items():
        if v > a:
            a=v
            master_key = k

    return master_key

if __name__ == '__main__':
    print(best_stock({"CAC":91.1,"TASI":120.9,"ATX":1.01}))
