# int (integer) (целое число)
number = 5
age = 30

# float (дробное число)
fnumber = 5.7

# str (string "строка")
name = "soel"

# вывод (ковычки указывают на аргумент)
print ("что нужно вывести")

# конкатенация
print ("привет, я " + name + "!")
print ("мне " + str(age) + " лет")

# экранирование (символ \ экранирует последующий символ)
print ("a \"b\" c")
print ('a "b" c')

# перевод строки
print ("A")
print ("B")

print ("A\nB")


# текст запроса
input ("ты кто?")
# запрос с выводом на экран
print ( input ("ты кто?") )

# умножение строк
print ( "Слово" * 4 )
# строка выведется 4 раза

# удаление переменной
test = 10
del test

# метасинтаксические пересенные
# foo, bar аналогично как x, y в математике

# in-Place (уместные операторы сокращают код) (+= , -= , *= , /= , %= и т.д.)
test = 10
test = test + 10
# =20
test += 10
# тоже =20
x = "Test"
x *= 5
# переменная Test выведется 5 раз (строка умножится)

# bool (Булево значение: правда / ложь)
status = True
status = False
# сравнение (10=11?)
print ( 10 == 11 )
# (10 не = 11?)
print ( 10 != 11 )

# лексиграфическое сравнение
Test > Tesa
# у каждой буквы своё значение и поэтому t > a
print ("test" > "tesa")

# условия: if - если
# условие выполняется и выводится на экран
pogoda = "Зима"
if pogoda == "Зима" :
	print ("Сейчас холодно")
# условие не выполняется и не выводится на экран
pogoda = "Весна"
if pogoda == "Зима" :
	print ("Сейчас холодно")
# вложенное условие
pogoda = "Зима"
time = "Ночь"
if pogoda == "Зима" :
	print ("Сейчас холодно")
	if time == "Ночь" :
		print ("Не иди")
# удвоенное условие
if pogoda == "Зима" and (time == "Ночь" or time == "Вечер") :
	print ("Не иди")

# условие не выполнится потому что не = дождю (not - не) (not инвертирует if)
pogoda = "Дождь"
if not pogoda == "Дождь"
	print ("что-то")

# elif - сокращение от else if
time = "День"
if time == "День" :
	print ("можно гулять")
elif time == "Утро" :
	print ("кофе попей")
elif time == "Вечер" :
	print ("спать иди")

# else - другое
# если день: можно гулять, если другое условие: не стоит идти
time = "День"
if time == "День" :
	print ("можно гулять")
else:
	print ("не стоит идти")
	
# высший приоритет имеют (), затем **, * /, + -

# цикл while - пока (делай что-то "пока"...)
# цикл вывидится 1 раз потому что после вывода test = False
test = True
while test:
	print ("вывод")
	test = False
	
# пока i <= 5 цикл повторяется
i = 1
while i <= 5:
	print (i)
	i = i + 1
	
# остановка цикла в консоли Ctrl + C
# break останавливакт цикл (сдесь остановит на 999 при условии что i достигнет 1000)
i = 1
while 1 == 1:
	print ("ы, " + str(i))
	i += 1
	
	if i == 1000:
		break
		
print ("конец")

# continue - продолжение прогоаммы
# исполнение цикла 1000 раз если число не делиьмя на 2 по модулю (%), пропустить операцию
num = 0
while num <= 1000:
	num += 1
	if (num % 2) != 0:
		continue;
	print ("чётное число " + str(num))
	
# списки [ ]
test = [1, 2, 3, 4, 5]
print (test)

# 1й элемент списка тмеет индекс 0, 2й - 1 и т.д.
test = [1, 2, 3, 4, 5]
print (test[2])

# список в списке
# выведится d потому что 2й список имеет индекс 3, а d имеет индекс внутри 2го списка 0
test = ["a", "b", "c", ["d", "e", "f"]]
print (test[3] [0])
# списки можно умножать (выводить несколько раз)
test = [1, 2, 3]
print (test * 2)
# списки можно слаживать
test = [1, 2, 3]
print (test + [4, 5, 6])
# вывод из списка если есть элемент
test = [1, 3, 8, 9]
if 4 in test:
    print ("4")
if 3 in test:
	print ("3")
# вывод элемента если его нет в списке
test = [1, 3, 8, 9]
if 4 not in test:
    print ("4 is not in list")

# добавить элемент в список (append - дбавитьв конец списка)
test =[]
test. append ("привет")
test. append (4)
test. append ([1, 2, 3])
print (test)

# вывод количечтва элементов (len - функция)
test = [5, 2, 4, 7]
print ("в массиве test находится " + str (len(test)) + "элеметов" )

# удаление элементов
test = [5, 2, 4, 7]
test.append ("5")
print ("в массиве test находится " + str (len(test)) + "элементов" )
test.remove ("5")
print ("в массиве test находится " + str (len(test)) + "элементов" )
# добавление в нужную прозицию
# вставка в нулевую позицию
test = [5, 2, 4, 7]
test.insert (0, 4)
print (test)

# вывод max значения ( 3 )
test = (1, 2, 3)
print (max(test))
# вывод min значения ( 1 )
test = (1, 2, 3)
print (min(test))

# метод count (количество) - нужен чтобы получить колличество вхождений определённых значений в список (4ка повторяется 2 раза)
test = [ 1, 2, 3, 4, 5, 5, 6, 3, 2, 1, 3, 4, 5]
print ( test.count (4) )

# переворот значения массива (в 3,2,1)
test = [1, 2, 3]
test.reverse()
print (test)

# диапазоны - range. list - преобразует свой аргумент в список
number = list(range(100))
print (number)
# диапазоны между аргументами (от 50 до 99)
number = list(range(50, 100))
print (number)
# шаг генерации ( каждая вторая)
number = list(range(0, 100, 2))
print (number)
# как обойти список (создаётся иторационная переменная)
num = [1, 2, 3, 4, 5]
i = 0
length = len(num) -1
while i <= length:
	print(num[i])
	i += 1
# for - цикл
number = [1, 2, 3, 4, 5]
for element in number:
	print (element)

# определение и повторение функции, def - define (определение)
def print_spam():
	print ("spam")
	print ("spam")
	print ("spam")
print_spam()

#получится 10
# аргументами называют значения, которые передаю при вызове функции (5). в определении функции (def) его называют параметром
def multiply(number):
	print(number * 2)
multiply(5)

# возвращение функции (ковертация)
converted = str(123123)
print(coverted)

# возвращение строки
name = input ("введи имя: ")
age = input ("ввести возраст: ")

print ("привет " + name + "!")
print ("тебе " + age + "? норм:)")

# когда происходит исполнение return, она останавливает исполнение программы
def max(x, y):
	if x > y:
		return x
	else:
		return y
print (max (5, 10) )

# возвращение с запросом чисел
def max(x, y):
	if x > y:
		return x
	else:
		return y
x = float(input("Число 1: "))
y = float(input("Число 2: "))
print (max (x, y) )

# строки документирования
def soel():
	'''описание функциии'''
	print ("soel")
print (soel.__doc__)

# определение переменной
def soel():
	'''описание функциии'''
	print ("soel")
print (soel.__doc__)
test = "asd"
print ( soel() )
# дублированеи функции и вывод
my = soel
my()

# передача аргумента
def soel(name):
	'''описание функциии'''
	print ("soel" + name)
soel ("саша")
# функции можно передавать в качестве аргумента другим функциям
def soel(name):
	'''описание функциии'''
	print ("soel" + name)
def read_name():
	return ":::" + input("введи имя: ") + ":::"
soel( read_name() )
# или
def soel(name):
	'''описание функциии'''
	print ("soel" + name())
def read_name():
	return ":::" + input("введи имя: ") + ":::"
soel( read_name )

# модули и их импорт
import random
print ( random.randint (2, 100) )
# вывод 10ти рандомных чисел
import random
for i in range (10):
	print ( random.randint (2, 100) )
# иморт математики (sqrt - корень из числа)
import math
num = 9
print (math.sqrt(num))

import math
print (math.pi)
# импорт модуля и его содержания
# импорт отдельной функции модуля
from random import randint
print (randint (1, 10))
# импорт нескольких функций модуля
from math import sqrt, pi
# импорт ВСЕХ(*) переменных и функций из модуля
from random import *
print (randint (1, 10))

from math import *
print ( pi )
# переименование функции
from math import sqrt as koren
print (koren (25))

# STL - стандарт лайблери. Делятся модули на 3 типа: те что сами написали, загруженные с инета и те что интегрированы в сам питон
# PyPi - репазиторий для питона с его модулями
# установка из PyPi - pip
установка модуля: pip install vkapi
использование модуля: import vkapi
# некоторые модули не ставятся через pip, нужно скачивать установку exe