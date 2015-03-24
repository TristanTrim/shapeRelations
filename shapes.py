
import math

def shift180(degree):
    degree+=180
    if degree>360:
        degree-=360
    return(degree)

class Shape():
    def drawShape(self,degree):
        x,y=self.shape(degree)
        return(int(self.xPosition+x),int(self.yPosition+y))

    def add(self,other,degree):
       otherx,othery=other.shape(degree)
       x,y=self.shape(degree)
       return(otherx+x,othery+y)
    def drawAdd(self,other,degree):
        x,y=self.add(other,degree)
        return(int(self.xPosition+x),int(self.yPosition+y))

    def sub(self,other,degree):
       otherx,othery=other.shape(degree)
       x,y=self.shape(degree)
       return(x-otherx,y-othery)
    def drawSub(self,other,degree):
        x,y=self.sub(other,degree)
        return(int(self.xPosition+x),int(self.yPosition+y))

    def rotated(self,degree,shift):
        newdegree=degree+shift
        if newdegree>360:
            newdegree-=360
        x,y=self.shape(newdegree)
        vect=math.sqrt(x**2+y**2)
        x=math.cos(math.radians(degree))*vect
        y=math.sin(math.radians(degree))*vect
        return(x,y)
    def drawRotated(self,degree,shift):
        x,y=self.rotated(degree,shift)
        return(int(self.xPosition+x),int(self.yPosition+y))

    def drawRotAdd(self,other,degree,shift):
        newdegree=degree+shift
        if newdegree>360:
            newdegree-=360
        x,y=self.add(other,newdegree)
        vect=math.sqrt(x**2+y**2)
        x=math.cos(math.radians(degree))*vect
        y=math.sin(math.radians(degree))*vect
        return(int(self.xPosition+x),int(self.yPosition+y))

    def drawRotSub(self,other,degree,shift):
        newdegree=degree+shift
        if newdegree>360:
            newdegree-=360
        x,y=self.sub(other,newdegree)
        vect=math.sqrt(x**2+y**2)
        x=math.cos(math.radians(degree))*vect
        y=math.sin(math.radians(degree))*vect
        return(int(self.xPosition+x),int(self.yPosition+y))

class Bob(Shape):
    def __init__(self,position=(50,50),radius=25):
        self.size=radius
        self.xPosition=position[0]
        self.yPosition=position[1]
    def shape(self,degree):
        x=math.cos(math.radians(degree))*self.size+math.cos(math.radians(degree*4))*self.size/2
        y=math.sin(math.radians(degree))*self.size+math.sin(math.radians(degree*4))*self.size/2
        return(x,y)

class Circle(Shape):
    def __init__(self,position=(50,50),radius=25):
        self.size=radius
        self.xPosition=position[0]
        self.yPosition=position[1]

    def shape(self,degree):
        x=math.cos(math.radians(degree))*self.size
        y=math.sin(math.radians(degree))*self.size
        return(x,y)

class Square(Shape):
    def __init__(self,position=(50,50),radius=25):
        self.size=radius
        self.xPosition=position[0]
        self.yPosition=position[1]
    def shape(self,degree):
        if degree >= 315:
            x=self.size
            y=self.size*(degree-360)/45
        elif degree < 45:
            x=self.size
            y=self.size*degree/45
        elif degree < 135:
            x=self.size*(90-degree)/45
            y=self.size
        elif degree < 225:
            x=-self.size
            y=self.size*(180-degree)/45
        elif degree < 315:
            x=self.size*(degree-270)/45
            y=-self.size
        return(x,y)



