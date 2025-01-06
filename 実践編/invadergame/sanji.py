import pygame

class Sanji:
    
    def __init__(self, ai_game):
        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load('invadergame\images\onepiece05_sanji.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.center = self.screen_rect.center
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)