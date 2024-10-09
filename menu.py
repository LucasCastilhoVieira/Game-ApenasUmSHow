import pygame
from sys import exit
from pygame.locals import *


class Game_tela2:
    def __init__(self):
        self.state = 'menu'
        pygame.init()
        self.largura = 1600
        self.altura = 900
        self.start_game()
        
        
    def Tela(self):
        
        self.tela = pygame.display.set_mode([self.largura,self.altura])
        return self.tela
    
    def tela_position(self):

        fundo = pygame.image.load('img/fundonada.jpg')
        redimensionartela = pygame.transform.scale(fundo, (self.largura, self.altura))
        tela = self.tela.blit(redimensionartela,(0,0))
        return tela
    
    def title(self):
         game = pygame.display.set_caption('REGULAR SHOW GAME')
         return game
        

        
    def button_back(self):
        from game import Game_Main
        
        botaovoltar = pygame.image.load('img/botoes/voltar.png')
        voltar = pygame.transform.scale(botaovoltar, (300, 100))
        location_button_voltar = voltar.get_rect(center=(1350,800))
        ButtonBack = self.tela.blit(voltar, location_button_voltar)
        
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONDOWN:
               if location_button_voltar.collidepoint(evento.pos):
                     Game_Main()
               elif evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                     
        return ButtonBack
        
        
    def button_math(self):
        
        math = pygame.image.load('./img/botoes/materias/matematica.png')
        buttonmath = pygame.transform.scale(math, (300, 100))
        button_math_position = buttonmath.get_rect(center=(400, 300))
        ButtonMath = self.tela.blit(buttonmath, button_math_position)
        
        return ButtonMath
    
    
    def button_science(self):
    
        science = pygame.image.load('./img/botoes/materias/ciencia.png')
        button_science = pygame.transform.scale(science, (300, 100))
        button_science_position = button_science.get_rect(center=(900, 300)) 
        ButtonScience = self.tela.blit(button_science, button_science_position)  
           
        return ButtonScience
        
    def button_portuguese(self):
        
        portuguese = pygame.image.load('./img/botoes/materias/portugues.png')
        button_portuguese = pygame.transform.scale(portuguese, (300, 100))
        button_portuguese_position = button_portuguese.get_rect(center=(900, 500))
        ButtonPortuguese = self.tela.blit(button_portuguese, button_portuguese_position)
        
        return ButtonPortuguese
        
        
        
    def button_english(self):
        
        english = pygame.image.load('./img/botoes/materias/ingles.png')
        button_english = pygame.transform.scale(english, (300, 100))
        button_english_position = button_english.get_rect(center=(400, 500))
        ButtonEnglish = self.tela.blit(button_english, button_english_position)
        
        return ButtonEnglish
        
        
        
    def exit_game(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
                
                
    def start_game(self):
        
        self.Tela()
        self.title()

        while True:
            self.tela_position()
            self.button_back()
            self.button_math()
            self.button_portuguese()
            self.button_science()
            self.button_english()
            pygame.display.flip()
            

if __name__ == "__main__":
    Game_tela2()

        
        