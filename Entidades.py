import charc as ch
from algos import *
width, height = 680, 400
class Jugador:
    def __init__(self):
        self.m=ch.jugador()
        self.x=-width/2
        self.y=51-height/2
        self.direccion=1
        self.disparar=Bullet(self.x,self.y,self.direccion,0)
    def Draw(self):
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                r=(int)(self.m[i][j][0])
                g=(int)(self.m[i][j][1])
                b=(int)(self.m[i][j][2])
                if(r!=0 and g!=0 and b!=0): 
                    if self.direccion: set_pixel(self.x+j,self.y-i,r,g,b, 2)
                    else: set_pixel(self.x-j,self.y-i,r,g,b, 2)
        #pygame.display.flip()
    def Kill(self):
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                r=(int)(self.m[i][j][0])
                g=(int)(self.m[i][j][1])
                b=(int)(self.m[i][j][2])
                if(r!=0 and g!=0 and b!=0): 
                    if self.direccion: set_pixel(self.x+j,self.y-i,0,0,0, 2)
                    else: set_pixel(self.x-j,self.y-i,0,0,0, 2)
        #pygame.display.flip()
    def update(self,keys):
        ok=0
        x,y=self.x,self.y
        direccion=self.direccion
        if keys[K_UP]:
            self.Kill()
            if direccion: mov=Translate([(x,y,1)],8,51)
            else :  mov=Translate([(x,y,1)],-8,51)
            x,y=mov[0][0],mov[0][1]
            ok=1
            self.x,self.y=x,y
            self.Draw()
            pygame.display.flip()
        elif keys[K_LEFT]:
            mov=Translate([(x,y,1)],-8,0)
            x,y=mov[0][0],mov[0][1]
            ok=1
            direccion=0
        elif keys[K_RIGHT]:
            mov=Translate([(x,y,1)],8,0)
            x,y=mov[0][0],mov[0][1]
            ok=1
            direccion=1
        elif keys[K_a]:
            self.disparar=Bullet(self.x,self.y,self.direccion,1)
        self.disparar.update() 
        pygame.display.flip()
        if x<-width/2:  x=-width/2
        if x>width/2-32:  x=width/2-32
        if y<-height/2+45:  y=-height/2+45
        if y>-height/2+55:
            self.Kill()
            y=-height/2+49
            if direccion: x+=8
            else: x-=8
            self.x,self.y=x,y
            self.Draw()
            pygame.time.wait(2)
            pygame.display.flip()
        if ok==1:
            self.Kill()
            self.x,self.y=x,y
            self.direccion=direccion
            self.Draw()
            pygame.display.flip()
class Bullet:
    def __init__(self,x,y,dir,estado):
        self.m=ch.bala()
        self.x=x
        self.y=y
        self.direccion=dir
        self.activo=estado
    def Draw(self):
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                r=(int)(self.m[i][j][0])
                g=(int)(self.m[i][j][1])
                b=(int)(self.m[i][j][2])
                if(r!=0 and g!=0 and b!=0): 
                    if self.direccion: set_pixel(self.x+j,self.y-i,r,g,b, 2)
                    else: set_pixel(self.x-j,self.y-i,r,g,b, 2)
        #pygame.display.flip()
    def Kill(self):
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                r=(int)(self.m[i][j][0])
                g=(int)(self.m[i][j][1])
                b=(int)(self.m[i][j][2])
                if(r!=0 and g!=0 and b!=0): 
                    if self.direccion: set_pixel(self.x+j,self.y-i,0,0,0, 2)
                    else: set_pixel(self.x-j,self.y-i,0,0,0, 2)
        #pygame.display.flip()
    def update(self):
        self.Kill()
        if self.activo :
            if self.direccion: self.x+=16
            else: self.x-=16
        if self.activo :
            self.Draw()
            pygame.time.wait(3)
        if self.x<-width/2:
            self.Kill()
            self.activo=0
        if self.x>width/2-32:
            self.Kill()
            self.activo=0            
class Enemy:
    def __init__(self):
        self.m=ch.enemigo()
        self.x=width/2-57
        self.y=79-height/2
        self.direccion=1
        self.disparar=Bullet(self.x,self.y,self.direccion,0)
        self.vida=9
    def Draw(self,factor):
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                r=min((int)(self.m[i][j][0])*factor,255)
                g=min((int)(self.m[i][j][1])*factor,255)
                b=min((int)(self.m[i][j][2])*factor,255)
                if(r!=0 and g!=0 and b!=0): 
                    if self.direccion: set_pixel(self.x+j,self.y-i,r,g,b, 2)
                    else: set_pixel(self.x-j,self.y-i,r,g,b, 2)
    def Kill(self):
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                r=(int)(self.m[i][j][0])
                g=(int)(self.m[i][j][1])
                b=(int)(self.m[i][j][2])
                if(r!=0 and g!=0 and b!=0): 
                    if self.direccion: set_pixel(self.x+j,self.y-i,0,0,0, 2)
                    else: set_pixel(self.x-j,self.y-i,0,0,0, 2)
    def update(self,ataque):
        if self.vida==0: self.Kill()
        elif ataque:
            self.vida-=ataque
            self.Kill()
            self.Draw(2.7)
            pygame.display.flip()
            self.Kill()
            self.Draw(1)

class Planet:
    def __init__(self):
        self.m=ch.planeta()
        self.x=-width/2
        self.y=height/2-79
    def Draw(self):
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                r=(int)(self.m[i][j][0])
                g=(int)(self.m[i][j][1])
                b=(int)(self.m[i][j][2])
                if(r!=0 and g!=0 and b!=0): 
                    set_pixel(self.x+j,self.y-i,r,g,b, 2)
    def Kill(self):
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                r=(int)(self.m[i][j][0])
                g=(int)(self.m[i][j][1])
                b=(int)(self.m[i][j][2])
                if(r!=0 and g!=0 and b!=0): 
                    set_pixel(self.x+j,self.y-i,0,0,0, 2)
        #pygame.display.flip()
