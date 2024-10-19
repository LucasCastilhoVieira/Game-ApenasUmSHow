import pygame
from sys import exit
from pygame.locals import *


class Niveis:
    def __init__(self):
        self.state = 'niveis'
        pygame.init()
        self.largura = 1600
        self.altura = 900
        self.start_game()
        
        
    def Tela(self):
        
        self.tela = pygame.display.set_mode([self.largura,self.altura])
        return self.tela
    
    def tela_position(self):

        fundo = pygame.image.load('img/niveis.png')
        redimensionartela = pygame.transform.scale(fundo, (self.largura, self.altura))
        tela = self.tela.blit(redimensionartela,(0,0))
        return tela
    
    def title(self):
         game = pygame.display.set_caption('REGULAR SHOW GAME')
         return game
        

        
    def button_back(self):
        from menu import Game_tela2
        botaovoltar = pygame.image.load('img/botoes/voltar.png')
        voltar = pygame.transform.scale(botaovoltar, (300, 100))
        location_button_voltar = voltar.get_rect(center=(1350,800))
        ButtonBack = self.tela.blit(voltar, location_button_voltar)
        
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONDOWN:
               if location_button_voltar.collidepoint(evento.pos):
                     Game_tela2()
               elif evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                     
        return ButtonBack
        
        

    def title_nivel(self):
        
        level_title = pygame.image.load('./img/niveis/niveis.png')
        title = pygame.transform.scale(level_title, (800, 200))
        title_show = self.tela.blit(title, (100, 50)) 
        return title_show
    
        
    def button_easy(self):
        
        easy = pygame.image.load('./img/niveis/facil.png')
        button_easy = pygame.transform.scale(easy, (300, 100))
        button_easy_position = button_easy.get_rect(center=(470, 400))
        ButtonEasy = self.tela.blit(button_easy, button_easy_position)
        
        return ButtonEasy
    
    def button_medium(self):
        
        medium = pygame.image.load('./img/niveis/medio.png')
        button_medium = pygame.transform.scale(medium, (300, 100))
        button_medium_position = button_medium.get_rect(center=(470, 550))
        ButtonMedium = self.tela.blit(button_medium, button_medium_position)
        
        return ButtonMedium
        
        
    def button_hard(self):
        
        hard = pygame.image.load('./img/niveis/dificil.png')
        button_hard = pygame.transform.scale(hard, (300, 100))
        button_hard_position = button_hard.get_rect(center=(470, 700))
        ButtonHard = self.tela.blit(button_hard, button_hard_position)
        
        return ButtonHard
        
        
        
                
    def start_game(self):
        
        self.Tela()
        self.title()

        while True:
            self.tela_position()
            
            self.button_back()
            self.title_nivel()
            self.button_easy()
            self.button_medium()
            self.button_hard()            
            pygame.display.flip()
            

if __name__ == "__main__":
    Niveis()

        
        