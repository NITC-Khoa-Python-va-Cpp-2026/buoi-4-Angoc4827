import random
with open('copy.txt', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
selected_lines = random.sample(lines, 5)
with open('output.txt', 'w', encoding = 'utf-8') as f:
    for line in selected_lines:
        f.write(line)
    f.write("Họ và tên")