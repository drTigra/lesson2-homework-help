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


def ask_user(question):
    dict_1={'Как дела?':'Хорошо!', 'Что делаешь?':'Программирую', 'Получается?': 'Пока не очень('}
    while True:
        question=input('Введите вопрос: ')
        if question in dict_1:                 
            print (dict_1.get(question))       
            break
        else:
           print ('В моем словаре нет этого..')
        
    

ask_user('question')
