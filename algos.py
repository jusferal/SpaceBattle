from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import math
import random 
import numpy as np

### Algorithms ###
width, height = 680, 400

def set_pixel(x, y, r, g, b, size):
    glColor3f(r/255, g/255, b/255)
    glPointSize(size)

    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    #pygame.display.flip()

def color_pixel(width, height, x, y, size):
    rgb =glReadPixels(width / 2 + x, height / 2 + y, size, size,GL_RGB, GL_UNSIGNED_BYTE, None)
    rgb=list(rgb)    
    return rgb[:3]

def DDA(x0, y0, x1, y1, r, g, b, size):
    points = []
    dx = x1 - x0
    dy = y1 - y0

    x = x0
    y = y0

    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    xi = dx / steps
    yi = dy / steps

    set_pixel(round(x), round(y), r, g, b, size)
    points.append((round(x), round(y)))
    for k in range(int(steps)):
        x += xi
        y += yi
        set_pixel(round(x), round(y), r, g, b, size)
        points.append((round(x), round(y)))
    return points

def Bressennham(x0, y0, x1, y1, r, g, b, size):
    # |m| < 1
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    """ if x1 - x0 == 0:
		m = 0
	else:
		m = (y1 - y0) / (x1 - x0) """

    r = 2 * dy
    s = 2 * dy - 2 * dx

    p = 2 * dy - dx

    if x0 > x1:
        x = x1
        y = y1
        x1 = x0
    else:
        x = x0
        y = y0

    set_pixel(x, y, 1, 0, 0, size)
    k = 0
    # print(m, dx, dy)
    while k < dx:
        x += 1
        if p < 0:
            p = p + r
        else:
            y += 1
            p = p + s
        """ if m < 1:#dx == 0:
			set_pixel(x, y, r, g, b, size)
		else:
			set_pixel(x, y, r, g, b, size) """
        set_pixel(x, y, r, g, b, size)
        k += 1

def Circle8v(xc, yc, radio, r, g, b, size):
    # set_pixel(xc, yc + radio, 0, 1, 0, size)
    # set_pixel(xc, yc - radio, 0, 0, 1, size)
    # set_pixel(xc + radio, yc, 0, 1, 0, size)
    # set_pixel(xc - radio, yc, 0, 0, 1, size)

    for x in range(math.ceil(radio / math.sqrt(2)) + 1):
        y = math.ceil(math.sqrt(radio * radio - x * x))
        set_pixel(xc + x, yc + y, r, g, b, size)
        set_pixel(xc - x, yc + y, r, g, b, size)
        set_pixel(xc - x, yc - y, r, g, b, size)
        set_pixel(xc + x, yc - y, r, g, b, size)

        set_pixel(xc + y, yc + x, r, g, b, size)
        set_pixel(xc - y, yc + x, r, g, b, size)
        set_pixel(xc - y, yc - x, r, g, b, size)
        set_pixel(xc + y, yc - x, r, g, b, size)

def CirclePM(xc, yc, radio, r, g, b, size):
    # k starting in 0
    x = 0
    y = radio

    p = 1 - radio  # (5 / 4) - radio

    """ set_pixel(xc + x, yc + y, r, g, b, size)
	set_pixel(xc - x, yc + y, r, g, b, size)
	set_pixel(xc - x, yc - y, r, g, b, size)
	set_pixel(xc + x, yc - y, r, g, b, size)

	set_pixel(xc + y, yc + x, r, g, b, size)
	set_pixel(xc - y, yc + x, r, g, b, size)
	set_pixel(xc - y, yc - x, r, g, b, size)
	set_pixel(xc + y, yc - x, r, g, b, size) """

    while x < y:
        # x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

        set_pixel(xc + x, yc + y, r, g, b, size)
        set_pixel(xc - x, yc + y, r, g, b, size)
        set_pixel(xc - x, yc - y, r, g, b, size)
        set_pixel(xc + x, yc - y, r, g, b, size)

        set_pixel(xc + y, yc + x, r, g, b, size)
        set_pixel(xc - y, yc + x, r, g, b, size)
        set_pixel(xc - y, yc - x, r, g, b, size)
        set_pixel(xc + y, yc - x, r, g, b, size)
        x += 1

"""def Circle(xc, yc, radio, r, g, b, size):
    angle = 0
    while angle < 45:
        x = radio * math.cos(math.radians(angle))
        y = radio * math.sin(math.radians(angle))

        set_pixel(xc + x, yc + y, r, g, b, size)
        set_pixel(xc - x, yc + y, r, g, b, size)
        set_pixel(xc - x, yc - y, r, g, b, size)
        set_pixel(xc + x, yc - y, r, g, b, size)

        set_pixel(xc + y, yc + x, r, g, b, size)
        set_pixel(xc - y, yc + x, r, g, b, size)
        set_pixel(xc - y, yc - x, r, g, b, size)
        set_pixel(xc + y, yc - x, r, g, b, size)

        angle += 1 / radio"""

def Circle(xc, yc, radio, r, g, b, size):
    lx = [1, -1, -1, 1]
    ly = [1, 1, -1, -1]
    angle = 0
    while angle < 45:
        x = radio * math.cos(math.radians(angle))
        y = radio * math.sin(math.radians(angle))
        for i in range(4):
            set_pixel(xc+lx[i]*x, yc+ly[i]*y, r, g, b, size)
            set_pixel(xc+lx[i]*y, yc+ly[i]*x, r, g, b, size)
        angle += 1 / radio

def bfs(width, height, size, xi, yi,OldColor,NewColor):
    dx4 = [0, 1, 0, -1]
    dy4 = [-1, 0, 1, 0]
    q = []
    q.append((xi, yi))
    if color_pixel(width, height, xi, yi, size) == list(OldColor):
        set_pixel(xi, yi, NewColor[0], NewColor[1], NewColor[2], size)
    while len(q) != 0:
        x, y = q.pop(0)
        print(x,y,"::::")
        for i in range(2):
            r = x+dx4[i]
            c = y+dy4[i]
            print(r,c,">>",color_pixel(width, height, r, c, size),list(OldColor))
            if color_pixel(width, height, r, c, size) == list(OldColor):
                print(r,c)
                set_pixel(r, c, NewColor[0], NewColor[1], NewColor[2], size)
                q.append((r, c))

def DrawPolygon(vertices, r, g, b, size):
    # vertices = [(x1, x2), (x2, y2), ..., (xn, yn)]
    vertices.append(vertices[0])
    for k in range(len(vertices) - 1):
        # print(vertices[k])
        x0, y0 = vertices[k][:2]
        x1, y1 = vertices[k + 1][:2]
        DDA(x0, y0, x1, y1, r, g, b, size)
    vertices.pop()

def SimpleSeedFill(width, height, size, vertices, xi, yi, r, g, b):
    #r, g, b = 255 * r, 255 * g, 255 * b
    stack = []
    stack.append((xi, yi))
    while len(stack) > 0:
        x, y = stack.pop()

        if color_pixel(width, height, x, y, size) != [r, g, b]:
            print(color_pixel(width, height, x, y, size))
            set_pixel(x, y, r, g, b, size)
            

        # examine surrounding pixels to see if they should be placed onto stack
        if color_pixel(width, height, x + 1, y, size) != [r, g, b]:
            stack.append((x + 1, y))

        if color_pixel(width, height, x + 1, y + 1, size) != [r, g, b]:
            stack.append((x + 1, y + 1))

        if color_pixel(width, height, x, y + 1, size) != [r, g, b]:
            stack.append((x, y + 1))

        if color_pixel(width, height, x - 1, y + 1, size) != [r, g, b]:
            stack.append((x - 1, y + 1))

        if color_pixel(width, height, x - 1, y, size) != [r, g, b]:
            stack.append((x - 1, y))

        if color_pixel(width, height, x - 1, y - 1, size) != [r, g, b]:
            stack.append((x - 1, y - 1))

        if color_pixel(width, height, x, y - 1, size) != [r, g, b]:
            stack.append((x, y - 1))

        if color_pixel(width, height, x + 1, y - 1, size) != [r, g, b]:
            stack.append((x + 1, y - 1))

def Translate(vertices, tx, ty):
    T = [
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ]
    result = []
    for item in vertices:
        point = np.dot(T, item)
        result.append(point)
    return result

def Rotation(vertices, angle):
    angle = math.radians(angle)
    R = [
        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1]
    ]
    result = []
    for item in vertices:
        point = np.dot(R, item)
        result.append(point)
    return result
def Reflexion(vertices):
    T = [
        [-1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    result = []
    for item in vertices:
        point = np.dot(T, item)
        result.append(point)
    return result

def floatRgb(mag, cmin, cmax):
    """ Return a tuple of floats between 0 and 1 for R, G, and B. """
    # Normalize to 0-1
    try:
        x = float(mag-cmin)/(cmax-cmin)
    except ZeroDivisionError:
        x = 0.5  # cmax == cmin
    blue = min((max((4*(0.75-x), 0.)), 1.))
    red = min((max((4*(x-0.25), 0.)), 1.))
    green = min((max((4*math.fabs(x-0.5)-1., 0.)), 1.))
    return red, green, blue

def scenario():
    x,y=211,211
    h=-height/2
    for i in range(11):
        Bressennham(-width/2, h, width/2, h, 34, 46, 17, 2)
        pygame.display.flip()
        h+=1
    for i in range(4):
        Bressennham(-width/2, h, width/2, h, 114, 86, 67, 2)
        pygame.display.flip()
        h+=1        
    for i in range(45):
        x=random.randint(-width/2, width/2)
        y=random.randint(-45, height/2)
        set_pixel(x, y,255,255,2555, 2)
        pygame.display.flip()
def display_openGL(width, height, scale):
    pygame.display.set_mode((width, height), pygame.OPENGL)

    glClearColor(0/255, 0/255, 0/255, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # glScalef(scale, scale, 0)

    gluOrtho2D(-1 * width / 2, width / 2, -1 * height / 2, height / 2)
