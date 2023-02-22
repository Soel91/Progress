# пример изменяемость и неизменяемость кортежей с помощью игры а анаграммы
import random

# последовательность слов для выбора
WORDS = ('питон', 'анаграмма', 'простая', 'сложная', 'ответ', 'подстаканник')

# подсказки
python_clue = ('язык проги')
anagram_clue = ('пример на основе этой игры')
easy_clue = ('лёгкая сложность')
hard_clue = ('высокая сложность')
answer_clue = ('дают при вопросе')
coaster_clue = ('туда ставят стакан в поездах')
yes = 'да'

# извлечение случайного элемента из последовательности
word = random.choice(WORDS)

# переменная, с которой будет сопоставлена версия ввода
correct = word
jumble = ' '
while word:
	# выбор случайной позиции в слове
	position = random.randrange(len(word))
	jumble += word[position]
	# конкатенацию двух строк делаем значением переменной word, которая равна самой себе за вычетом одной буквы word[position]
	word = word[ : position] + word[(position+1) :]
	print('анаграмма: ', jumble)
guess = input('\nИсходное слово: ')
clue = input('если хотите получить подсказку? "да/нет": ')
if correct == 'питон':
	if clue == yes:
		print(python_clue)
elif correct == 'анаграмма':
	if clue == yes:
		print(anagram_clue)
elif correct == 'простая':
	if clue == yes:
		print(easy_clue)
elif correct == 'сложная':
	if clue == yes:
		print(hard_clue)
elif correct == 'ответ':
	if clue == yes:
		print(answer_clue)
elif correct == 'подстаканник':
	if clue == yes:
		print(coaster_clue)
while guess != correct and guess != ' ':
	print('неправильно')

	guess = input('\nИсходное слово: ')
else:
	print('правильно')

if clue == yes:
    print('начислено 1 очко')
else:
    print('начислено 2 очка')
    
input ()