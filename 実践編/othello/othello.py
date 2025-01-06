import pygame
import sys
from settings import Settings

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
YELLOW = (255, 155, 0)
SIZE = 600
BOARD_SIZE = 12
GRID_SIZE = SIZE // BOARD_SIZE

class Othello:
    """ゲームのアセットと動作を管理する全体的なクラス"""
    
    def __init__(self):
        """ゲームを初期化し、ゲームのリソースを作成する"""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("オセロゲーム")