
import math

colourCoo=1


class Shape():
    def __init__(self,radius=25,position=(127,127,32)):
        self.position=position
        self.radius=25
        self.average=.5
        self.max=-10
        self.min=10
        self.times=1

    def drawPoint(self,x,y):
        length,width,height=self.renderPoint(x,y)
      # if height>self.max:
      #     self.max=height
      # if height<self.min:
      #     self.min=height
      # self.average=(self.average*self.times+height)/(self.times+1)
      # self.times=self.times+1
      # print("average {} max {} min {}".format(self.average,self.max,self.min))
        return(int(length*self.radius+self.position[0]), int(width*self.radius+self.position[1]), int(height*self.radius*colourCoo+self.position[2]),)

    def add(self,x,y,other):
        length,width,height=self.renderPoint(x,y)
        otherl,otherw,otherh=other.renderPoint(x,y)
        return(int((length+otherl)*self.radius+self.position[0]),
                int((width+otherw)*self.radius+self.position[1]),
                int((height+otherh)*self.radius+self.position[2]))

class Sphere(Shape):
    def renderPoint(self,x,y):
        height=x/(math.pi)
        #print(1-((x/math.pi)-1))
        length=math.cos(y)*math.sqrt((1-((x/math.pi)-1)**2))
        width =math.sin(y)*math.sqrt((1-((x/math.pi)-1)**2))
        return(length,width,height)

class Octohedron(Shape):
    def renderPoint(self,x,y):
        height=x/(math.pi)
        length=math.cos(y)*abs(math.cos(y))*(1-abs((x/math.pi)-1))
        width =math.sin(y)*abs(math.sin(y))*(1-abs((x/math.pi)-1))
        return(length,width,height)


