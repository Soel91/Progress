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
# abs - превращает любое число в аргументе в абсолютное число (без каких либо знаков)
print (abs(-1235))
# sum - суммирует все числа
print (sum([2, 3, 5, 10])) # выдаст 20 = 2+3+5+10

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

# исключения
#ImportError - когда произведён неверно импорт
#IndexError - когда при попытке получитьдоступ к ячейке списка которой в нём нет
#NameError - при использовании переменной, которой не существует
#SyntaxEroor - в проге допущена синтаксическая ошибка
prin("Test")a
#TypeError - при попытке передачи в функцию аргумент, тип которого не совместим
print ("Test" + 5)
#ValueError - когда тип переданой переменной или значения тот что нужен, но значение не то что нужно

# контроль исключений
try:
	print( 7/0 )
except ZeroDivisionError:
	print ("поймано исключение ДелениеПоНулю")
print("программа завершена")

try:
	print( 7/0 )
	ы
except:
	print ("поймано исключение какое-то")
print("программа завершена")
# SyntaxEroor: синтаксическое исключение так поймать невозможно (только с помощью eval)
# eval - исполнить произвольный код
try:
	eval ("print (7/4)ы")
except SyntaxError:
	print ("поймано исключение синтаксиса")
print ("конец")
# пречисление исключений
try:
	print( number/0 )
except (ZeroDivisionError, NameError, ValueError, TypeError):
	print ("поймано исключение")
print("программа завершена")
# исполнение кода в не зависимости поймано исключение или нет
try:
	print( number/0 )
except (ZeroDivisionError, NameError, ValueError, TypeError):
	print ("поймано исключение")
finally:
	print ("Конец поимки")
print("программа завершена")
# как выбрасывать свои собственные исключения (raise)
try:
	pogoda = "Плохая"
	if pogoda == "Плохая":
		raise TypeError
except TypeError:
	print ("Поймано исключение TypeError")
# описание почему выброшено исключение в ()
pogoda = "Плохая"
if pogoda == "Плохая":
	raise TypeError("Test")
# когда вызывается raise внутри except, он выбрасывает своё исключение по которому был вызван
try:
	print( 7/0 )
except:
	raise
print("программа завершена")
# создание исключения через создание класса
class SoelErrorr(Exception):
	pass
#raise SoelErrorr("Test") решётка в начале не нужна !!!!!!!!!!!!!

# assert - утверждение
def exc(text):
	print(str(text) + "!")
exc("hello")
# точки проверки такие ли участки кода какие надо
def exc(text):
	assert text != " "
	print(str(text) + "!")
exc(" ")

def test(number):
	assert number > 0
	print(str(number))
test(-10)
# текст, который выведится вмсте с исключением
def test(number):
	assert number > 0, "число меньше нуля"
	print(str(number))
test(-10)

# read - чтение всей информации файлов, открытие файлов - open
file = open("коммандная консоль.py")

# режим открытия файла
# r - чтение файла
file = open("коммандная консоль.py", "r")
print (file.read())
file.close()
# чтение количества символов в файле
filename = input("Укажите файл: ")
file = open(filename, "r")
print ( "в данном файле " + str(len(file.read())) + " символов")
file.close()
# 1 символ в текстовом файле формата UTF-8 = 2 байта (1 байт 1 символ + 1 байт на документ)
# указание сколько байтов прочетать в документе
file = open("test.txt", "r")
print(file.read(4))
print(file.read(3)) # 3 байта будут прочитаны после 4 байт
file.close()
# чтение с определённого момента (например по 100кБ за проход)
file = open("test.txt", "r")
print(file.read(1024 * 100))
file.close()
# w - перезапись файла
# перезапись это командой стирает данные файла или создаёт его если его не существует
file = open("test.txt", "w")
file.close()
# что бы внести данные в файл - write:
file = open("test.txt", "w")
file.write("привет мир")
file.close()
# создание файла и внесение в него своего текста
filename = input("Введите имя файла: ")
text = input("Какой текст ввести в файл: ")
file = open(filename, "w")
file.write (text)
file.close()
# a - добавление файла (append)
# (каждый запуск добавляет TEST)
file = open("test.txt", "a")
file.write( "TEST" )
file.close()
# b - Binary mode: для чтения медиаконтента(изображения, музыка и т.д.), т.е. ту инфу, для которой нужен бинарный доступ

# копирование фалов
filename1 = input("ввели название копируемого файла: ")
filename2 = input("введи куда копировать файл (в какой файл): ")
file1 = open(filename1, "r")
file2 = open(filename2, "w")
file2.write (file1.read())
file1.close()
file2.close()
print ("копирование завершено")
# бэкап файла
filename1 = input("ввели название копируемого файла: ")
filename2 = "backup_" + filename1
file1 = open(filename1, "r")
file2 = open(filename2, "w")
file2.write (file1.read())
file1.close()
file2.close()
print ("бэкап завершён")

# бэкап бинарного файла (к символу a, w, и т.д. дописать b), так же подходит и для обычных текстовых файлов
filename1 = input("ввели название копируемого файла: ")
filename2 = "backup_" + filename1
file1 = open(filename1, "rb")
file2 = open(filename2, "wb")
file2.write (file1.read())
file1.close()
file2.close()
print ("бэкап завершён")

# чтение строк
file = open("test.txt", "r")
strings = file.readlines()
print (strings)
file.close()

file = open("test.txt", "r")
strings = file.readlines()
for string in strings:
    print (string)
file.close()

# with - с помощью (помогает автоматически закрыть файл по выполнению кода with)
with open("test.txt", "r") as f:
    print (f.read())

# после with нельзя считать файл повторно
with open("test.txt", "r") as f:
    print (f.read(5))
print (f.read()) # попытка считать оставшийся файл

# типы данных
# None - означает пустоту, если превратить в булево значение оно будет false
# есть ли переменная test
test = None
if (test == None):
    print ("есть")
# в первом случае вызывается Test, её результат присваивается в aha и так как она с помощью return ничего не возвращает, python стандартно возвращает значение None
def test():
    print ("Test")
aha = test()
print (aha)

# Dictionary - словарь (любой тип данных)
test = {
    "ключ1" : "значение1",
    "ключ2" : "значение2"
}
print(test["ключ1"])

test = {
    "ключ1" : "значение1",
    "ключ2" : "значение2"
}
try:
    print(test["тестовый ключ"])
except KeyError:
    print( "такого ключа не существует" )
# существует ли ключ
test = {
    "ключ1" : "значение1",
    125 : "сто двадцать пять"
}
if 125 in test:
    print("существует")
else:
    print("не существует")
# ключа не существует?
test = {
    "ключ1" : "значение1",
    125 : "сто двадцать пять"
}
if 125 not in test:
    print("не существует")
else:
    print("существует")
# пример поиска
contakt = {
    "первый" : "+123456789",
    "второй" : "+546531351",
    "третий" : "+684645654",
}
test = input("кого ищем? ")
if test in contakt:
    print("есть такой: " + contakt[test])
else:
    print("нет такого")
# метод get передаёт None или введённое значение
contakt = {
    "первый" : "+123456789",
    "второй" : "+546531351",
    "третий" : "+684645654",
}
print (contakt.get("второйЫ", "нету номера"))

'''Многострочный
комментарий'''

# pass - команда, которая оставляет блок кода пустым (она ничего не делает)
def main():
    pass

# кортеж - Tuple (он ведёт себя как списки, но в отличии от них не может быть изменён). С его помощью удобнее создавать неизменяемы списки
# обычный список
name = ["John", "James", "Jack"]
name[0] = "Miha"
print(name[0])
# кортеж. выдаст ошибку
name = ("John", "James", "Jack")
name[0] = "Miha"
print(name[0])

# Срез списков (индексирование элементов списков) - List indexing
# выведет цифры с 3 по 5 (до 6)
digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
digit2 = digit[ 2:5 ]
print ( digit2 )
# диапазон к этой функции
for i in range (10):
    print(i)
# пропуск индексов срезов
# если не ставить первую цифру, то пайтон понимает что надо начинать с начала списка
digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
digit2 = digit[:4]
print ( digit2 )
# если не ставить вторую цифру, то пайтон понимает что надо читать список до конца с определённого индекса
digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
digit2 = digit[2:]
print ( digit2 )
# шаг индексирования
# начнёт считать с первого индекса каждый второй индекс
digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 1,3,5,7,9
digit2 = digit[::2]
print ( digit2 )
#
digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 3,5,7,9
digit2 = digit[2:10:2]
print ( digit2 )
# выводится от 3 до 99 каждое третье число
digit = range (3, 101)[::3]
for i in digit:
    print (i)
# получение индекса с конца списка
# выдаст 7, 8, 9
digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
digit2 = digit[-4:-1]
print ( digit2 )
# реверс индексов
digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
digit2 = digit[::-1]
print ( digit2 )
# список перевернётся дважды и будет в обычном порядке
digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
digit2 = digit[::-1][::-1]
print ( digit2 )

# форматирование строк
# когда ставится %, создаётся плейсхолдер - он удерживает это место и в будущем будет при обработке этой строки на реальные данные
Привет ИМЯ!
Тебе уже ЧИСЛО лет!
name = "Джесси"
age = 31
print ("Привет, %s!\nТебе уже %d год!" %(name, age) )
# %s - означает строку (плейсхолдер строки)
# %d - плейсхолдер числа
# %f - плейсхолдер дроби

# .format()
name = "Джесси"
age = 31
print ("Привет, {}!\nТебе уже {} год!".format(name, age) )

# выдаст abra cadabra. воспроизведёт индексы по порядку 0,1,0 (abra,cad,abra)
print ( "{0}{1}{0}".format ( "abra", "cad" ) )

# присвоение имени
idex_name = "Джесси"
index_age = 31
print ("Привет, {name}!\nТебе уже {age} год!".format(name = idex_name, age = index_age) )

human = {
    "name" : "Jassy",
    "age" : 21
}
print ( 'Имя: {person[name]}\nВозраст: {person[age]}'.format (person = human) )

# заполнение строки символами
# Soel******   <
# ******Soel   >
# ***Soel***   ^
# {нулевой аргумент(0): символ заполнитель(*) метод заполнения(^) количество знакомест в которое надо вместить строку(14)}
input_str = "Soel"
print ('{0:*^14}'.format (input_str) )
# если не указать символ заполнения, он заполнится пробелами
input_str = "Soel"
print ('{0:^14}'.format (input_str) )
# если не совпадает количество символов справа и слева
input_str = "Souel"
long = 10
if ( len (input_str) % 2):
    long += 1
print ( ('{0:*^'+str(long)+'}').format (input_str) )

# функци для работы со строками и числами
# перечисление через ,
fruit = ['Лимоны', 'Яблоки', 'Киви', 'Ананасы', 'Клубника']
member = 'James,Jonny,Jessie,John'
print ( ', '.join(fruit))
# перечисление через -
fruit = ['Лимоны', 'Яблоки', 'Киви', 'Ананасы', 'Клубника']
member = 'James,Jonny,Jessie,John'
print ( ' - '.join(fruit))

# замена. если в replace Лёха написать с маленькой, замены не будет (функция регистрозависима)
print( 'Привет, Лёха!'.replace('Лёха', 'Саня') )

# startswith (начинается с:) - проверка с какой буквы начинается

name = input('Ваше имя: ')
if( name.startswith('А') ) or ( name.startswith('а') ):
    print('Ваше имя начинается на А, привет ')

# endswith - (заканчивается на)
word = 'Hello druving'
if ( word.endswith('ing') ):
    print ('Hello ing')
else:
    print ('WTF?')

# lower - перевод в нижний регистр
stroka = input('Ввести что-то: ')
print( stroka.lower() )

# upper - перевод в верхний регистр
stroka = input('Ввести что-то: ')
print( stroka.upper() )

# split - обратное действие методу join (разбивает строку на список или кортеж)
fruit = ['Лимоны', 'Яблоки', 'Киви', 'Ананасы', 'Клубника']
member = 'James,Jonny,Jessie,John'
print ( member.split (',') )
