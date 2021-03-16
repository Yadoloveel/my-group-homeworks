import string

name = str(input("Введіть своє ім'я: "))
age = str(input("Вкажить свій вік: "))
sex = str(input("Вкажить свою стать: "))

user_var1 = 'Hello! My name is '+name+". I'm "+age+". I'm "+sex+'.'
print(user_var1)
####
user_var2 = "Hello! My name is %s. I'm %s. I'm %s." % (name, age, sex)
print(user_var2)
#####
user_var3 = "Hello! My name is {0}. I'm {1}. I'm {2}.".format(name, age, sex)
print(user_var3)
####
about_me_fstring = f"Hello! My name is {name}. I'm {age}. I'm {sex}."
print(about_me_fstring)
####
txt1 = about_me_fstring[:about_me_fstring.index('I')]
txt2 = about_me_fstring[about_me_fstring.find('I'):about_me_fstring.rindex('I'):]
txt3 = about_me_fstring[about_me_fstring.rindex('I'):]
print(txt1+'\n'+txt2+'\n'+txt3)
####
about_unname = about_me_fstring.replace('Alex', 'Bogdan').replace("38", "28").replace('man', 'strong man')
print(about_unname)
####
list_from_str = about_me_fstring.split('. ')
print(list_from_str)
####
print(type(list_from_str))
####
str_from_list = '. '.join(list_from_str)
print(str_from_list)
####
print(about_me_fstring.swapcase())
####
