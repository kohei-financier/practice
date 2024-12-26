# 宇宙船の操作 その2
import sys
import pygame

# プログラム開始
if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("pygame05")

    ship_image = pygame.image.load("Pygame\\ship.bmp")
    ship_rect = ship_image.get_rect()
    ship_rect.midbottom = (400, 300)

    # 移動用管理フラグ
    ship_right = False
    ship_left = False

    # ship_rectのX座標
    # ship_rect.xはint型で演算されるので、float型のローカル変数を使用している
    ship_x = float(ship_rect.x)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:      # キーを押した時
                if event.key == pygame.K_RIGHT:     # 右キー
                    ship_right = True
                elif event.key == pygame.K_LEFT:    # 左キー
                    ship_left = True
            elif event.type == pygame.KEYUP:        # キーを離した時
                if event.key == pygame.K_RIGHT:     # 右キー
                    ship_right = False
                elif event.key == pygame.K_LEFT:    # 左キー
                    ship_left = False

        # ship_rect.rightはship_rectの右上のX座標、ship_rect.leftは左上のX座標
        if ship_right == True and ship_rect.right < 800:
            ship_x += 0.1
        elif ship_left == True and ship_rect.left > 0:
            ship_x -= 0.1
        ship_rect.x = ship_x

        # 再描画
        screen.fill((230, 230, 230))
        screen.blit(ship_image, ship_rect)
        pygame.display.flip()