import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    
    def __init__(self, ai_game):
        """エイリアンを作成する"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # エイリアンの画像を読み込み、サイズを取得する
        self.image = pygame.image.load('invadergame\images\\alien.bmp')
        self.rect = self.image.get_rect()
        
        # 新しいエイリアンを画面の左上の近くに配置する
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # エイリアンの実際の位置を格納する
        self.x = float(self.rect.x)
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom:
            return True

    def update(self):
        """エイリアンを右に移動する"""
        self.rect.y += self.settings.alien_speed