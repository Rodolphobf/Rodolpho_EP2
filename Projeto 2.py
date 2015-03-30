# -*- coding: utf-8 -*-

"RODOLPHO BENINI FILGUEIRAS"
"PROJETO 2 -> FORCA"

import random

lista = open("entrada1.txt" , encoding="utf-8").read().splitlines()

#conteudo = lista.readlines()
escolha = random.choice(lista).strip().lower()

limpa = []

#for palavra in conteudo:
   # p = palavra.strip()
    #if p != "":
     #   limpa.append(p)
    

import turtle

window = turtle.Screen()    #abre a janela 
window.bgcolor('white')
forca = turtle.Turtle() #muda o nome do turtle
window.title('JOGO DA FORCA')
forca.speed(30)
forca.hideturtle()
forca.penup()
forca.setpos(-230,-30)      #linhas 10 a 27 construcao da forca
forca.pendown()
#forca.pensize(9)


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


def corpo ():
    
    forca.penup()        #corpo
    forca.left(90)
    forca.fd(30)
    forca.pendown()
    forca.left(0) 
    forca.fd(50)


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
#tracos.pensize(9)
tracos.penup()
tracos.setpos(-200,-100)
tracos.pendown()
tracos.setpos(-200,-100) 


def traco (palavra):
    for c in palavra:
        if c == " ":
            tracos.penup()
            tracos.fd(30)
            tracos.pendown()
            
        if c != " ":
            tracos.pendown()
            tracos.fd(20)
            tracos.penup()
            tracos.fd(10)
            tracos.pendown()
  

             
#jogao = choice(limpa)
jogao = list(escolha)


traco(escolha)


#a = window.textinput("FORCA 13", "Escolha uma letra :")

acerto = 0
erro = 0

letra = turtle.Turtle()
#letra = pensize(9)


while erro < 6 and acerto < len(escolha):
    
    a = window.textinput("FORCA 13", "Escolha uma letra :")
    acerto2 = 0
   # acertos = 0
   #erros = 0

    letra = turtle.Turtle()
    #letra = pensize(9)
    
   # while acerto == len(escolha) :
        
    for r in range(0,len(escolha)):
     
        if a == jogao[r]:
        
            letra.penup()
            letra.setx(-200 + r*30)
            letra.sety(-90)
            letra.pendown()
            letra.write(a ,move=False, align="left", font=("Arial", 20, "normal"))
            acerto += 1
            acerto2 += 1
           #else :
            
              #  for i in escolha:
                    #if a != i:
    if acerto2 == 0:
        erro += 1
            
        if erro == 1 :
            cabeca()
        if erro == 2:
            corpo()
        if erro == 3:
            braco_1()
        if erro == 4:
            braco_2()
        if erro == 5:
            perna_1()
        if erro == 6:
            perna_2()
if acerto == len(escolha):
    #codigo ganhar
#if erro == 6 :
    #codigo perder
window.mainloop() # fecha a janela
