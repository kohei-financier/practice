import pygame.font

class Scoreboard:
    """得点の情報をレポートするクラス"""

    def __init__(self, ai_game):
        """得点を記録するための属性を初期化する"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        # 得点表示用のフォントを設定する
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 初期の得点画像を準備する
        self.prep_score()