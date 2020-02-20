"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def main():
    scholl = [
    {'scholl_class':'1a','scores':[2,3,2,4,5,3,4]},
    {'scholl_class':'1b','scores':[4,4,4,5,2,4]},
    {'school_class':'1c','scores':[3,3,4,5,2,2,2,2]}
    ]
    for klass in scholl:
        sum_of_scholl=(float(sum(klass['scores']))/len(klass['scores'])) 
        print (f'Средняя оценка в {klass} - {sum_of_scholl}')
         # не могу обратиться к значению класса {klass['scholl_class']} не работает
        sum_of_scholls=0
        sum_of_scholls=float(sum_of_scholls + sum_of_scholl)
    sum_of_scholls_total=(float(sum_of_scholls)/len(scholl))    
    print (f'Средняя оценка по школам = {sum_of_scholls_total}')

if __name__=='__main__': 
    main()

