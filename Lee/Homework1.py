import string
import re
name1 = input('Enter your name: ')
age1 = input('Enter your age: ')
gender1 = input('Enter your gender: ')

alldata1 = '1Hello! My name is ' + name1 + ". I'm " + age1 + " and I'm a " + gender1
print(alldata1)
alldata11 = '%s%s%s%s%s%s' % ('2Hello! My name is ', name1, ". I'm ", age1, " and I'm a ", gender1)
print(alldata11)
alldata12 = "3Hello! My name is {}. I'm {} and I'm a {}".format(name1, age1, gender1)
print(alldata12)

about_me_fstring = print(f"4Hello! My name is {name1}. I'm {age1} and I'm a {gender1}")
print(about_me_fstring)
