
import pygame
import random

import shapes

# Window dimensions
width = 640
height = 400

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

bigCircle = shapes.Circle()
bigCircleCopy = shapes.Circle()
smallCircle = shapes.Circle(radius=25)
square = shapes.Square(position=(250,250),radius=100)
circle = shapes.Circle(position=(100,100),radius=40)
oppositeCircle = shapes.Circle(radius=5)
oppositeSquare = shapes.Square(radius=20)
smallSquare = shapes.Square(position=(200,200),radius=10)
otherSquare = shapes.Square(position=(400,100))
otherSmallSquare = shapes.Square(radius=20)
otherOtherSmallSquare = shapes.Square(radius=20)

foo=0
bar=180
while running:
    screen.fill((0,0,0))
    foo+=1
    if foo>360:
        foo=0
    bar+=1
    if bar>360:
        bar=0

    #bigCircle.xPosition,bigCircle.yPosition=square.drawShape(foo)
    bigCircle.xPosition,bigCircle.yPosition=square.drawSub(bigCircle,foo)
    bigCircleCopy.xPosition,bigCircleCopy.yPosition=square.drawAdd(bigCircle,foo)
    oppositeCircle.xPosition,oppositeCircle.yPosition=square.drawShape(bar)
    oppositeSquare.xPosition,oppositeSquare.yPosition=square.drawShape(bar)
    otherSquare.xPosition,otherSquare.yPosition=bigCircleCopy.drawRotAdd(otherSquare,foo,foo)
    smallSquare.xPosition,smallSquare.yPosition=otherSquare.drawRotated(foo,foo)
    otherSmallSquare.xPosition,otherSmallSquare.yPosition=circle.drawSub(otherSmallSquare,foo)
    otherOtherSmallSquare.xPosition,otherOtherSmallSquare.yPosition=circle.drawAdd(otherSmallSquare,foo)

    for ii in range(0,720,1):
        ii=float(ii)/2
        screen.set_at(bigCircle.drawShape(ii),(222,0,0))
        screen.set_at(bigCircleCopy.drawShape(ii),(222,222,222))
       #screen.set_at(bigCircle.drawAdd(smallCircle,ii),(222,222,0))
       #screen.set_at(bigCircle.drawSub(smallCircle,ii),(222,222,0))
        screen.set_at(square.drawShape(ii),(0,222,0))
        screen.set_at(square.drawAdd(bigCircle,ii),(222,222,0))
        screen.set_at(square.drawSub(bigCircle,ii),(222,222,0))
       #screen.set_at(smallCircle.drawShape(ii),(0,0,222))

        screen.set_at(circle.drawShape(ii),(0,0,222))
        screen.set_at(circle.drawAdd(otherSmallSquare,ii),(0,0,222))
        screen.set_at(circle.drawSub(otherSmallSquare,ii),(0,0,222))
        screen.set_at(oppositeCircle.drawShape(ii),(0,222,0))
        screen.set_at(oppositeSquare.drawShape(ii),(55,222,55))

        screen.set_at(otherSmallSquare.drawShape(ii),(222,0,222))
        screen.set_at(otherOtherSmallSquare.drawShape(ii),(222,0,222))

        screen.set_at(smallSquare.drawRotated(ii,foo),(222,0,222))

        screen.set_at(otherSquare.drawRotated(ii,foo),(0,222,222))
        screen.set_at(otherSquare.drawRotAdd(smallSquare,ii,foo),(0,222,222))
        screen.set_at(otherSquare.drawRotSub(smallSquare,ii,foo),(0,222,222))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(1000)
