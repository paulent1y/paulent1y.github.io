import pygame, sys
# импортирование модулей 
# pygame - основной дял создания игр
# sys - модуль для работы с системой, на данный момент с помощью него выходим из игры
from random import randint as r
# импортируем функцию randint и записываем ее в переменную r
# теперь r(a,b) выдает случайное число от a до b

pygame.init()

screenSize = width, height = 800, 600
# создаем переменную screenSize, которая является кортежем (800, 600)
# а так же две переменных width = 800 и height = 600
window = pygame.display.set_mode(screenSize)
#создаем переменную window, которая является игровым окошком

#Начальные характеристики персонажа
x = 300
y = 300
size = 50
color = (255,0,0)


while 1:
	pygame.time.delay(20) #установка задержки между кадрами
	events = pygame.event.get() #запись всех событий в текущем кадре в переменную events
	keys = pygame.key.get_pressed()

	for ev in events: #цикл по всем событиям в переменной events
		print(ev)
		if ev.type == 12:
			sys.exit()
		if ev.type == 5: #клавиши мыши и колесико
			if ev.button == 1:#клик левой кнопкой мыши
				pass 
			if ev.button == 2:#клик колесом кнопкой мыши
				pass 
			if ev.button == 3:#клик правой кнопкой мыши
				pass 
			if ev.button == 4:#вращение колесика вперед
				pass 
			if ev.button == 5:#вращение колесика назад
				pass 
	if keys[273]:#стрелка вверх
		pass 
	if keys[274]:#стрелка вниз
		pass
	if keys[275]:#стрелка вправо
		pass
	if keys[276]:#стрелка влево
		pass
	if keys[32]:#клавиша пробел
		pass


	window.fill((0,0,0))
	pygame.draw.circle(window, color, (x,y), size)
	pygame.display.update()
	
