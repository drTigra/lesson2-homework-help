"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

school = [
  {'scholl_class':'1a','scores':[2,3,2,4,5,3,4]},
  {'scholl_class':'1b','scores':[4,4,4,5,2,4]},
  {'school_class':'1c','scores':[3,3,4,5,2,2,2,2]}
]
'''def all_score (score):
    score=(sum(school['scores']))/len(school['scores'])
    return score
'''
for score in school:
    score+=('scores')
    print(score)
