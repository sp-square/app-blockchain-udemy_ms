names = ['Alice', 'Bob', 'Carol', 'Dylan', 'Elizabeth',
         'Frederick', 'Garth', 'Hector', 'Ingrid', 'Jun', 'Kyle', 'Lily', 'Michel', 'Norma']


for name in names:
    print('Name is ' + name)
    if len(name) > 5:
        print('Note that ' + name + ' has more than 5 characters')
    if 'n' in name or 'N' in name:
        print('Note that ' + name + ' has "n" or "N" in it')

while len(names) > 0:
    print(names)
    names.pop()
