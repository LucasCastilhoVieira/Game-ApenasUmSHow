import pygame
from sys import exit
from pygame.locals import *


class Game_math:
    def __init__(self):
        self.state = 'math'
        self.sprite = []
        
        self.largura = 1600
        self.altura = 900
        pygame.init()
        self.start_game()
        
        
        
    def players(self):
        
        self.sprite.append(pygame.image.load('./img/personagens/mordecai/animation_mordecai0.png'))
        self.sprite.append(pygame.image.load('./img/personagens/mordecai/animation_mordecai1.png'))
        self.atual = 0
        self.image = self.sprite[self.atual]
        self.image = pygame.transform.scale(self.image, (100, 200))
        self.rect = self.image.get_rect(center=(600, 590))
        write = self.tela.blit(self.image, self.rect)
        return write
        
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
            self.players()

            pygame.display.flip()
            

if __name__ == "__main__":
    Game_math()

        
        