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
    #fundo
    fundotela1 = pygame.image.load('img/tela.jpg')
    
    #titulo game
    regularshow_title = pygame.image.load('img/regular show.png')
    title = pygame.transform.scale(regularshow_title, (500, 200))
    
    #buttoninit
    botaoiniciar = pygame.image.load('img/botoes/iniciar.png')
    iniciar = pygame.transform.scale(botaoiniciar, (300, 100))
    button_rect = iniciar.get_rect(center=(1350,700))
    
    
    redimensionartela = pygame.transform.scale(fundotela1, (largura, altura))
    #finish
    
    
    
    
    
    #tela2
    fundotela2 = pygame.image.load('img/fundonada.jpg')
    botaovoltar = pygame.image.load('img/botoes/voltar.png')
    #button back
    voltar = pygame.transform.scale(botaovoltar, (300, 100))
    button_rect2 = voltar.get_rect(center=(1350,800))
    
    #button math
    math = pygame.image.load('./img/botoes/materias/matematica.png')
    buttonmath = pygame.transform.scale(math, (300, 100))
    button_math_position = buttonmath.get_rect(center=(400, 300))
    
    #button science
    science = pygame.image.load('./img/botoes/materias/ciencia.png')
    button_science = pygame.transform.scale(science, (300, 100))
    button_science_position = button_science.get_rect(center=(900, 300))
    
    #button portuguese
    portuguese = pygame.image.load('./img/botoes/materias/portugues.png')
    button_portuguese = pygame.transform.scale(portuguese, (300, 100))
    button_portuguese_position = button_portuguese.get_rect(center=(900, 500))
    
    
    #button english
    english = pygame.image.load('./img/botoes/materias/ingles.png')
    button_english = pygame.transform.scale(english, (300, 100))
    button_english_position = button_english.get_rect(center=(400, 500))
    
    
    
    
    
    #redimensionamento da tela
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
            tela.blit(buttonmath, button_math_position)
            tela.blit(button_science, button_science_position)
            tela.blit(button_portuguese, button_portuguese_position)
            tela.blit(button_english, button_english_position)
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if button_rect2.collidepoint(evento.pos):
                    state = 'tela1'
                elif button_english_position.collidepoint(evento.pos):
                    state = 'ingles'
                    print('entrou no ingles')
                    
                elif button_portuguese_position.collidepoint(evento.pos):
                    state = 'portugues'
                    print('entrou no portugues')
                    
                elif button_science_position.collidepoint(evento.pos):
                    state = 'ciencias'
                    print('entrou na cienciass')
                    
                elif button_math_position.collidepoint(evento.pos):
                    state = 'matematica'
                    print('entrou na matematica')
                    
            pygame.display.flip()  
            
            
            
            
            
            
            
        

   
            