import pygame, sys
# импортирование модулей 
# pygame - основной дял создания игр
# sys - модуль для работы с системой, на данный момент с помощью него выходим из игры
from random import randint as r
# импортируем функцию randint и записываем ее в переменную r
# теперь r(a,b) выдает случайное число от a до b
pygame.init()

class Wall():
	def __init__(self):
		self.width = r(10,30)
		self.height = r(30,70)
		self.y = height - self.height
		self.x = width + 100
		self.color = (r(0,255), r(0,255), r(0,255))
	def move(self):
		self.x-=1
		pygame.draw.rect(window, self.color, (int(self.x), self.y, self.width, self.height))
	def col(self):
		if ((self.x>x and self.x < x+size) and (self.y>y and self.y<y+size)) or ((self.x+width>x and self.x+width < x+size) and (self.y+height>y and self.y+height<y+size)) :
			print("Удар")
		else:
			print("ВСе ок")

screenSize = width, height = 800, 200
# создаем переменную screenSize, которая является кортежем (800, 600)
# а так же две переменных width = 800 и height = 600
window = pygame.display.set_mode(screenSize)
#создаем переменную window, которая является игровым окошком

#Начальные характеристики персонажа
x = 50
y = 100
size = 20
color = (255,0,0)
g = 0.1
speed = 0
a = []
timer = 3000
while 1:
  pygame.time.delay(10) #установка задержки между кадрами
  events = pygame.event.get() #запись всех событий в текущем кадре в переменную events
  keys = pygame.key.get_pressed()
  if (pygame.time.get_ticks()-timer)> 2500:
  	timer = pygame.time.get_ticks()
  	a.append(Wall())
  for ev in events: #цикл по всем событиям в переменной events
    # print(ev)
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
    if y>height - size - size:
      speed = -5
  
  y += speed

  if y>=height - size:
  	speed = 0
  	y =height - size
  else:
  	speed += g 


  window.fill((0,0,0))
  for z in a:
  	z.move()
  	z.col()

  pygame.draw.rect(window, color, (int(x),int(y), size,size) )
  pygame.display.update()