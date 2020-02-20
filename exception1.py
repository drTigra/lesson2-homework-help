"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user(question):     
    try:
        dict_1={'Как дела?':'Хорошо!', 'Что делаешь?':'Программирую', 'Получается?': 'Пока не очень('}   
        while True:
            question=input('Введите вопрос: ')
            if question in dict_1:                 
                print (dict_1.get(question))       
                break
            else:
                print ('В моем словаре нет этого..')              
    except KeyboardInterrupt:
        print ('Пока!')
      
ask_user('question')
