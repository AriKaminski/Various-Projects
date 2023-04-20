"""

with open('quotes.txt') as f:
    for one_line in enumerate(f.readlines()):
        if one_line[0] % 2 == 0:
            print(one_line[1],end=' ')
        else:
            print(' '+ one_line[1])


with open('quotes.txt') as f:
    counter = 1
    one_line = f.readline()
    while one_line:
        if counter % 2 ==0:
            print('    ' + one_line)
        else:
            print(one_line, end='')
        counter += 1
        one_line = f.readline()
"""

new_name = 'Steve Jobs\n'
with open('names.txt','a',encoding='utf-8') as f:
    f.write(new_name)

print('\nDone')
with open('names.txt',encoding='utf-8') as f:
    print(f.read())