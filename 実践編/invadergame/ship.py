import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """宇宙船を管理するクラス"""

    def __init__(self, ai_game):
        """宇宙船を初期化し、開始時の位置を設定する"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # 宇宙船の画像を読み込み、サイズを取得する
        self.image = pygame.image.load('invadergame\images\ship.bmp')
        self.rect = self.image.get_rect()
        
        # 新しい宇宙船を画面下部の中央に配置する
        self.rect.midbottom = self.screen_rect.midbottom

        # 宇宙船の水平位置の浮動小数点を格納する
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # 移動フラグ
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False
    
    def update(self):
        """移動フラグによって宇宙船の位置を更新する"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
            
        # self.xからrectオブジェクトの位置を更新する
        self.rect.x = self.x
        self.rect.y = self.y
            
        
    def blitme(self):
        """宇宙船を現在位置に描画する"""
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        """宇宙船を画面の中央に配置する"""
        self.rect.centerx = self.screen_rect.centerx  # 画面の中央に横軸を合わせる
        self.rect.bottom = self.screen_rect.bottom - 10  # 宇宙船が画面下端から少し上に配置されるように
        self.x = float(self.rect.x)