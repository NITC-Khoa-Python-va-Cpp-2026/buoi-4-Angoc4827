with open('copy.txt', 'w') as f:
    copy = open('input.txt', 'r')
    content = copy.readlines()
    for line in content:
        f.write(f"{line}")
    copy.code()
