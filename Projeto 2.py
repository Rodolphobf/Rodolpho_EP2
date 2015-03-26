# -*- coding: utf-8 -*-

#RODOLPHO BENINI FILGUEIRAS

import random
import turtle

window = turtle.Screen()    #abre a janela 
window.bgcolor('white')
forca = turtle.Turtle() #muda o nome do turtle
window.title('JOGO DA FORCA')

forca.penup()
forca.setpos(-230,-30)      #linhas 10 a 27 construcao da forca
forca.pendown()
forca.pensize(9)

forca.left(0)
forca.fd(25)
forca.right(180)
forca.fd(50)
forca.left(180)
forca.fd(25)
forca.left(90)
forca.fd(200)
forca.right(90)
forca.fd(100)
forca.left(270)
forca.fd(25)
forca.color('black')
forca.right(90)

def cabeca():
    return forca.circle(15)       #cabeca

def corpo ():
    return forca.penup()        #corpo
forca.left(90)
forca.fd(30)
forca.pendown()
forca.left(0) 
forca.fd(50)
def braco_1():
    return forca.left(115)
forca.fd(30)
forca.penup()    #Braco 1   
forca.left(180)
forca.fd(40)
forca.pendown()
forca.backward(30)

def braco_2():
    return forca.left(130)     # braco 2
forca.fd(30)
forca.backward(30)

forca.left(295)
forca.penup()       #perna 1
forca.left(0)
forca.fd(40)
forca.pendown()
forca.left(330)
forca.fd(40)

forca.backward(40) #perna 2
forca.left(60)
forca.fd(40)
forca.back(40)

variavel_texto = window.textinput("FORCA 13", "Escolha uma letra :")

window.mainloop() # fecha a janela
