#                                                               Проверка пароля на недопустимые символы


# Мой вариант
from string import ascii_letters as l


d = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
p = True

def alphanumeric(password):
    for i in password:
        if i in l or i in d:
            p = True
        else:
            p = False
            break
    if len(password) > 0:
        print(p)
    else:
        print('False')
        
# Вариант профи (вот я и узнал про isalnum)
        
def alphanumeric_1(string):
    return string.isalnum()        
    
    
    
    
    
    
    
    
    
    pass
