print ("Индекс массы тела\n ")
a = float (input ("Введите массу тела в килограммах: "))
b = float (input ("Введите рост в сантиметрах: "))

c = a/(b/100)**2
# сокращение до 2 цифр после запятой
c = float('{:.2f}'.format(c))
print ("Индекс тела: "+ str(c))

if (c >= 1 and c <=16.5):
	print ("Диапазон: 1 - 16.5")
	print ("Критический недостаток веса")
	
elif (c >=16.5 and c <=18.5):
	print ("Диапазон: 16.5 - 18.5")
	print ("Недостаток в весе")

elif (c >=18.5 and c <=25):
	print ("Диапазон: 18.5 - 25")
	print ("Нормальный вес тела")
	
elif (c >=25 and c <=30):
	print ("Диапазон: 25 - 30")
	print ("Избыточная масса тела")
	
elif (c >=30 and c <=35):
	print ("Диапазон: 30 - 35")
	print ("Ожирение (Класс 1)")
	
elif (c >=35 and c <=40):
	print ("Диапазон: 35 - 40")
	print ("Ожирение (Класс 2)")
	
elif (c >=40 and c <=100):
	print ("Диапазон: 40 - 100")
	print ("Ожирение (Класс 3)")
	
else:
	print ("Неверный результат")

input()