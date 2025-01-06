class Settings:
    
    def __init__(self):
        """ゲームの初期設定"""
        # 画面に関する設定
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        
        # 宇宙船の設定
        self.ship_speed = 1.5