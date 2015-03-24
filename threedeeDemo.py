
import pygame
import random
import math
import threedeeshapes

# Window dimensions
width = 640
height = 400

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

sphere = threedeeshapes.Sphere(radius=60)

smallSphere = threedeeshapes.Sphere()

oct = threedeeshapes.Octohedron(position=(200,100,32))

xx=0
yy=0
foo=0
while running:
    xx+=.01*(math.pi-(math.sqrt(abs(math.pi-xx))))
    yy+=30#*random.random()
    foo+=.001
    if foo > 2*math.pi:
        foo-=2*math.pi
    if yy > 2*math.pi:
        yy-=2*math.pi
    if xx > 2*math.pi:
        xx-=2*math.pi
        screen.fill((0,0,0))
    
    print(foo)
    print(oct.add(foo,0,sphere))
    l,w,h=oct.add(math.pi,foo,sphere)
    smallSphere.position=(l,w,h)
    l,w,h=smallSphere.drawPoint(xx,yy)
    if 2*w-64>0 and 2*w-64<255:
        screen.set_at((l,100+w),(h,0,h))
        screen.set_at((200+l,75+h),(2*w-64,2*w-64,w))

    l,w,h=sphere.drawPoint(xx,yy)
    if h>0 and h<255:
        screen.set_at((l,w),(h,0,h))
        screen.set_at((200+l,h),(w,w,0))

    l,w,h=oct.drawPoint(xx,yy)
    if h>0 and h<255:
        screen.set_at((l,w),(h,0,h))
        screen.set_at((l,100+w),(0,h,0))
        screen.set_at((200+l,h),(w,w,0))
        screen.set_at((200+l,125+h),(0,w,0))

    l,w,h=oct.add(xx,yy,sphere)
    if h>0 and h<255:
        screen.set_at((l,100+w),(h,0,h))
        screen.set_at((200+l,100+h),(w,w,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick()#100000)
