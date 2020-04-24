import pygame, sys, math
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
x1 = 300
y1 = 300
size1 = 50
color = (255,0,0)

x2 = 150
y2 = 150
size2 = 30


while 1:
  pygame.time.delay(20) #установка задержки между кадрами
  events = pygame.event.get() #запись всех событий в текущем кадре в переменную events
  keys = pygame.key.get_pressed()

  for ev in events: #цикл по всем событиям в переменной events
    
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
    y2-=1 
  if keys[274]:#стрелка вниз
    y2+=1
  if keys[275]:#стрелка вправо
    x2+=1
  if keys[276]:#стрелка влево
    x2-=1
  if keys[32]:#клавиша пробел
    pass


  window.fill((0,0,0))
  pygame.draw.circle(window, color, (x1,y1), size1)
  pygame.draw.circle(window, color, (x2,y2), size2)
  pygame.draw.line(window, (255,255,255), (x1,y1), (x2,y2))
  pygame.draw.line(window, (255,255,0), (x1,y2), (x2,y2))
  pygame.draw.line(window, (0,0,255), (x1,y2), (x1,y1))
  a = abs(x1-x2)
  b = abs(y1-y2)
  c = math.sqrt(a*a+b*b)
  if c<size2+size1:
  	size2+=1
  	size1-=1
  print(c)
  pygame.display.update()
