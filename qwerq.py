def kot(age, name, hungry):
	if age > 5:
		print("Пять лет назад мне было", age - 5)
	else: 
		print("Я еще очень маленький")
	print("Первая буква моего имени ", name[0])
	if hungry:
		print("я хочу КУШАЦ")
	else:
		print("нет спасибо я не голодный")


kot(18, "Макс", True)
kot()
kot()
kot()