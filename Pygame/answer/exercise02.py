# 課題2
import sys
import pygame
import random

# 乱数取得
def get_random(max):
    return random.randint(1, max)

# 画面横幅
SCREEN_WIDTH = 800

# 画面縦幅
SCREEN_HEIGHT = 600

# 移動距離
MOVE_DISTANCE = 0.1

# プログラム開始
if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("課題2")

    ship_image = pygame.image.load("ship.bmp")
    ship_rect = ship_image.get_rect()

    # X座標の最大値
    x_max = SCREEN_WIDTH - ship_rect.width

    # 初期位置
    ship_rect.x = get_random(x_max)
    ship_rect.y = 0

    # ship_rectの座標
    ship_x = float(ship_rect.x)
    ship_y = float(ship_rect.y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 落下
        ship_y += MOVE_DISTANCE

        # 当たり判定
        if ship_rect.top >= SCREEN_HEIGHT:
            ship_x = get_random(x_max)
            ship_y = 0

        ship_rect.x = ship_x
        ship_rect.y = ship_y

        # 再描画
        screen.fill((230, 230, 230))
        screen.blit(ship_image, ship_rect)
        pygame.display.flip()