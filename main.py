import pygame
from sys import exit
from pygame.locals import *


pygame.init()

largura = 1600
altura = 900

tela = pygame.display.set_mode([largura,altura])
pygame.display.set_caption('REGULAR SHOW GAME')


state = 'tela1'
while True:
    #tela1
    fundotela1 = pygame.image.load('img/tela.jpg')
    regularshow_title = pygame.image.load('img/regular show.png')
    title = pygame.transform.scale(regularshow_title, (500, 200))
    botaoiniciar = pygame.image.load('img/botoes/iniciar.png')
    iniciar = pygame.transform.scale(botaoiniciar, (300, 100))
    redimensionartela = pygame.transform.scale(fundotela1, (largura, altura))
    button_rect = iniciar.get_rect(center=(1350,700))
    #finish
    
    #tela2
    fundotela2 = pygame.image.load('img/fundonada.jpg')
    botaovoltar = pygame.image.load('img/botoes/voltar.png')
    voltar = pygame.transform.scale(botaovoltar, (300, 100))
    button_rect2 = voltar.get_rect(center=(1350,800))
    redimensionartela2 = pygame.transform.scale(fundotela2, (largura, altura))
    #finish
            
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if state == 'tela1':
                
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(evento.pos):
                    state = 'tela2'

            tela.blit(redimensionartela,(0,0))
            tela.blit(title, (100, 50)) 
            tela.blit(iniciar, button_rect)
            pygame.display.flip()           

        if state == 'tela2':
        
            tela.blit(redimensionartela2,(0,0))
            tela.blit(voltar, button_rect2)
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if button_rect2.collidepoint(evento.pos):
                    state = 'tela1'
            pygame.display.flip()  
            
            
            
            
            
            
            
        

   
            