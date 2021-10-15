# import copy

persons = [
    {'name': 'Alex', 'age': 21, 'hobbies': [
        'cooking', 'video games', 'football']},
    {'name': 'Beatrix', 'age': 34, 'hobbies': ['cooking', 'coding']},
    {'name': 'Carol', 'age': 23, 'hobbies': ['yoga', 'sewing']}
]
names = [person['name'] for person in persons]
print('Names', names, sep=': ')
all_older_than_20 = all([person['age'] > 20 for person in persons])
print('All persons are older than 20', all_older_than_20, sep=': ')
print('\n')
persons_copy = [person.copy() for person in persons]
# persons_copy = copy.deepcopy(persons)
persons_copy[0]['name'] = 'Walter'
print('persons: ', persons)
print('persons_copy: ', persons_copy)
print('\n')
a, b, c = persons
print(a, b, c, sep='\n')
