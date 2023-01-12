Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
totalsum = 0
S = int(input("Введите количество билетов для покупки:\n"))
Введите количество билетов для покупки:
1
M = 1
print()

for amount in range(1, S + 1):
    print("Номер билета:", M)
    age = int(input("Введите возраст участника:"))
    price1 = 0
    price2 = 990
     price3 = 1390
     
SyntaxError: unexpected indent
 price3 = 1390
 
SyntaxError: unexpected indent
    price3 = 1390
    
SyntaxError: unexpected indent
price3 = 1390
if age < 18:
 print("Стоимость билета:", price1, "рублей.")
 elif 18 <= age <=25:
     
SyntaxError: invalid syntax
elif 18 <= age <=25:
    
SyntaxError: invalid syntax
elif 18 <= age <=25:
    
SyntaxError: invalid syntax
elif 18 <= age <= 25:
    
SyntaxError: invalid syntax
>>> if age < 18:
...     print("Стоимость билета:", price1, "рублей.")
... elif 18 <= age <=25:
...     print("Стоимость билета:", price2, "рублей.")
...     totalsum += price2
... else:
...     print("Стоимость билета:", price3, "рублей.")
...     totalsum += price3
... M = M+1
SyntaxError: invalid syntax
>>>     M = M+1
...     
SyntaxError: unexpected indent
>>>    M = M+1
...    
SyntaxError: unexpected indent
>>>  M = M+1
...  
SyntaxError: unexpected indent
>>> M = M+1
>>> print()

>>> rint("-----")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    rint("-----")
NameError: name 'rint' is not defined. Did you mean: 'print'?
>>> print("-----")
-----
>>> print()

>>> print("Количество билетов:",  S)
Количество билетов: 1
>>> print("Сумма к оплате:",totalsum)
Сумма к оплате: 0
>>> if S > 3 and totalsum > 0:
...     sum_with_discount = totalsum * 0.9
...     print("Вам предоставлена скидка 10% за регистрацию более 3-х участников.\nСумма к оплате с учетом скидки:", sum_with_discount, "рублей.")
