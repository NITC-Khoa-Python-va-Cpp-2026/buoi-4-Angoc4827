with open ('input.txt', 'r') as f:
    data = f.readlines()
    print(data)
    x = 0

    for line in data:
        x += 1
    print(x)