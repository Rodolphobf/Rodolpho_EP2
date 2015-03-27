# -*- coding: utf-8 -*-

"RODOLPHO BENINI FILGUEIRAS"
"PROJETO 2 -> FORCA"

from random import *

lista = open("entrada1.txt" , encoding="utf-8")

conteudo = lista.readlines()

limpa = []

for palavra in conteudo:
    p = palavra.strip()
    if p != "":
        limpa.append(p)
    

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
    
    forca.circle(15)       #cabeca
cabeca()

def corpo ():
    
    forca.penup()        #corpo
    forca.left(90)
    forca.fd(30)
    forca.pendown()
    forca.left(0) 
    forca.fd(50)
corpo()

def braco_1():
    
    forca.left(115)
    forca.fd(30)
    forca.penup()    #Braco 1   
    forca.left(180)
    forca.fd(40)
    forca.pendown()
    forca.backward(30)


def braco_2():
    
    forca.left(130)     # braco 2
    forca.fd(30)
    forca.backward(30)


def perna_1():
    
    forca.left(295)
    forca.penup()       #perna 1
    forca.left(0)
    forca.fd(40)
    forca.pendown()
    forca.left(330)
    forca.fd(40)



def perna_2():
    
    forca.backward(40) #perna 2
    forca.left(60)
    forca.fd(40)
    forca.back(40)

tracos= turtle.Turtle()
tracos.pensize(9)



def traco (palavra):
    for c in palavra:
        if c == " ":
            tracos.penup()
            tracos.fd(30)
            tracos.pendown()
            
        if c != " ":
            tracos.pendown
            tracos.fd(20)
            tracos.penup()
            tracos.fd(10)
            tracos.pendown()
            
jogao = choice(limpa)

traco(jogao)


variavel_texto = window.textinput("FORCA 13", "Escolha uma letra :")

window.mainloop() # fecha a janela
