#импорт модуля рандом
import random
print('Начинаем игру: Угадай число от 1 до 100!')
# рандом загадывает число
rannum = random.randint (1, 101)
# ввод своего числа
number = int ( input('Угадайте число: ') )
# количество попыток +1 за каждый ввод числа
tries = 1
# цикл отгадывания
while number != rannum:
	if number > rannum:
		print( 'Меньше :(' )
	else:
		print( 'Больше :(' )
	number = int ( input('Угадайте число: ') )
	tries += 1
print( 'Поздравляю! Вы угадали число', rannum )
print( 'Количество попыток:', tries )