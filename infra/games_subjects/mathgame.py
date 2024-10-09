import pygame
from sys import exit
from pygame.locals import *


class Game_math:
    def __init__(self):
        self.state = 'math'
        pygame.init()
        self.largura = 1600
        self.altura = 900
        self.start_game()
        
        
    def Tela(self):
        
        self.tela = pygame.display.set_mode([self.largura,self.altura])
        return self.tela
    
    def tela_position(self):

        fundo = pygame.image.load('img/fundolindo.png')
        redimensionartela = pygame.transform.scale(fundo, (self.largura, self.altura))
        tela = self.tela.blit(redimensionartela,(0,0))
        return tela
    
    def title(self):
         game = pygame.display.set_caption('REGULAR SHOW GAME')
         return game
        


                
                
    def start_game(self):
        
        self.Tela()
        self.title()

        while True:
            self.tela_position()

            pygame.display.flip()
            

if __name__ == "__main__":
    Game_math()

        
        