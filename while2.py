"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""


def ask_user(ask_1):
    dict_1={'Как дела?':'Хорошо!', 'Что делаешь?':'Программирую', 'Получается?': 'Пока не очень('}
    while True:
        ask_1=input('Введите вопрос: ')
        if ask_1==dict_1.get(f'{ask_1}'): #КАК обратиться к ключу словаря??
            print (dict_1['ask_1'])       #КАК обратиться к соответсвующему значению словаря????
            break
       # else:
       #    print ('В моем словаре нет этого..')
        
    

ask_user('ask_1')
