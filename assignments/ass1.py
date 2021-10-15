name = input('What is your name? ')
age = input('How old are you? ')


def print_my_data():
  print('Hello ' + name + '! You are ' + age + ' years old.')


def print_any_data(data_one, data_two):
  print(str(data_one) + ' is the first argument, and ' + str(data_two) + ' is the second argument.')


def get_decades_lived(some_age):
  return int(some_age) // 10

print_my_data()
print_any_data(name, age)
print('You have already lived ' + str(get_decades_lived(age)) + ' decades.')