# Дан словарь такого типа:
sample_dict = {
    "class_a": {
        "student": {
            "name": "Misha",
            "marks": {
                "math": 90,
                "history": 85
            }
        }
    }
}
print(sample_dict)

# 1. Вывести значение ключа "name";
print(sample_dict['class_a']['student']['name'])

# 2. Вывести значение ключа "history";
print(sample_dict['class_a']['student']['marks']['history'])

# 3. Добавить нового студента в "class_a", соответственно его "name" и "marks";
sample_dict["class_a"].setdefault("student2", {'name': 'Alex',
                                               'marks': {
                                                   'math': 95, 'history': 98}})
print(sample_dict["class_a"])

# 4. Добавить новый класс со студентами;
sample_dict.setdefault("class_e", {"student1": {"name": "Dima",
                                                "marks": {
                                                    "math": 30, "history": 55}
                                                }})
sample_dict["class_e"].setdefault("student2", {'name': 'Liza',
                                               'marks': {
                                                   'math': 80, 'history': 70}})
print(sample_dict)

# 5. Добавить каждому студенту в "marks" предмет "physics" с оценкой;
sample_dict["class_a"]["student"]['marks'].setdefault("physics", 45)
sample_dict["class_a"]["student2"]['marks'].setdefault("physics", 67)
sample_dict["class_e"]["student1"]['marks'].setdefault("physics", 89)
sample_dict["class_e"]["student2"]['marks'].setdefault("physics", 87)
print(sample_dict["class_a"])
print(sample_dict["class_e"])

# 6. Подсчитать средний бал по каждому студенту (результат округлить до 2
# знаков после запятой);
st1 = sample_dict['class_a']['student']['name']
st2 = sample_dict['class_a']['student2']['name']
st3 = sample_dict['class_e']['student1']['name']
st4 = sample_dict['class_e']['student2']['name']
bal1 = str(round(sum(sample_dict["class_a"]["student"]['marks'].values())/\
        len(sample_dict["class_a"]["student"]['marks']), 2))
bal2 = str(round(sum(sample_dict["class_a"]["student2"]['marks'].values())/\
        len(sample_dict["class_a"]["student"]['marks']), 2))
bal3 = str(round(sum(sample_dict["class_e"]["student1"]['marks'].values())/\
        len(sample_dict["class_e"]["student1"]['marks']), 2))
bal4 = str(round(sum(sample_dict["class_e"]["student2"]['marks'].values())/\
        len(sample_dict["class_e"]["student2"]['marks']), 2))
print(st1+'-'+bal1+' balls'+'\n'+st2+'-'+bal2+' balls'+'\n'
      +st3+'-'+bal3+' balls'+'\n'+st4+'-'+bal4+' balls'+'\n')

# 7. Создать словарь со средним баллом за каждого студента;
sredball = {st1: bal1, st2: bal2, st3: bal3, st4: bal4}
print(sredball)

# 8. Определить лучшего студента по успеваемости;
d = dict(zip(sredball.values(), sredball.keys()))
print(d[max(d.keys())]+' - '+max(d.keys()))

# 9. Подсчитать средний бал по каждому классу (результат округлить до 2
# знаков после запятой);
classAbal1 = str(round((sum(sample_dict["class_a"]["student"][
                               'marks'].values())\
            +sum(sample_dict["class_a"]["student2"]['marks'].values()))\
             /len(sample_dict["class_a"]), 2))
classAbal2 = str(round((sum(sample_dict["class_e"]["student1"][
                              'marks'].values())\
            +sum(sample_dict["class_e"]["student2"]['marks'].values()))\
             /len(sample_dict["class_e"]), 2))
print('Class_a sredniy bal- '+classAbal1+'\n'+'Class_b sredniy bal- '
                                              ''+classAbal2)

# 10. Создать словарь со средним баллом за классы;
srdbclass = {'class_a': classAbal1, 'class_e': classAbal2}
print(srdbclass)

# 11. Определить лучший класс по успеваемости.
cl = dict(zip(srdbclass.values(), srdbclass.keys()))
print(cl[max(cl.keys())]+' - '+max(cl.keys()))


