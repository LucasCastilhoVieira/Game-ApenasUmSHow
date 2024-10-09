import pygame
from sys import exit
from pygame.locals import *


class Game_Main:
    def __init__(self):
        self.state = 'tela1'
        pygame.init()
        self.largura = 1600
        self.altura = 900
        self.start_game()
        
        
    def Tela(self):
        
        self.tela = pygame.display.set_mode([self.largura,self.altura])
        return self.tela
    
    def tela_position(self):
        fundo = pygame.image.load('img/tela.jpg')
        redimensionartela = pygame.transform.scale(fundo, (self.largura, self.altura))
        tela = self.tela.blit(redimensionartela,(0,0))
        return tela
    
    def title(self):
         game = pygame.display.set_caption('REGULAR SHOW GAME')
         return game
        

    
    def title_background(self):
            regularshow_title = pygame.image.load('img/regular show.png')
            title = pygame.transform.scale(regularshow_title, (500, 200))
            title_show = self.tela.blit(title, (100, 50)) 
            return title_show
        
    def Button_start(self):
        from menu import Game_tela2
        
        botaoiniciar = pygame.image.load('img/botoes/iniciar.png')
        iniciar = pygame.transform.scale(botaoiniciar, (300, 100))
        button_start = iniciar.get_rect(center=(1350,700))
        location_button = self.tela.blit(iniciar, button_start)
        
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONDOWN:
               if button_start.collidepoint(evento.pos):
                     Game_tela2()
               elif evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                     
        return location_button
        
        

                
    def start_game(self):
        
    

            self.Tela()
            self.title()
            
            while True:
                self.tela_position()
                #titulo game
                self.title_background()
                #buttoninit
                self.Button_start()
                pygame.display.flip()
        
   
    def verification_game(self, state):
        if state == 'tela1':
            Game_Main()
        else:
            pass
        
        

        
        
        
if __name__ == "__main__":
    Game_Main()