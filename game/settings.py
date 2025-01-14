class Settings:
    # エイリアン侵略の全設定を格納するクラス

    def __init__(self):
        # ゲームの初期設定

        # 画面に関する設定
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 弾の設定
        self.bullet_speed = 1.5 
        self.bullet_width = 300
        self.bullet_height = 15 
        self.bullet_color = (255, 0, 0) 
        self.bullets_allowed = 3

        # エイリアンの設定
        self.alien_speed = 0.1
        self.fleet_drop_speed = 0.5
        # 艦隊の移動方向を表し、１は右、ー１は左に移動することを表す
        self.fleet_direction = 1

        # ship settings
        self.ship_speed =1.5
        self.ship_limit = 3
