# 課題1
import sys
import pygame
from enum import Enum

# 横移動
class LateralMove(Enum):
    Left = 1
    Right = 2

# 縦移動
class VerticalMove(Enum):
    Up = 1
    Down = 2

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
    pygame.display.set_caption("課題1")

    ship_image = pygame.image.load("ship.bmp")
    ship_rect = ship_image.get_rect()

    # 初期位置
    ship_rect.midbottom = (400, 300)

    # ship_rectの座標
    ship_x = float(ship_rect.x)
    ship_y = float(ship_rect.y)

    # 移動の管理
    lateral_move = LateralMove.Left
    vertical_move = VerticalMove.Down

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 横移動
        if lateral_move == LateralMove.Left:
            ship_x -= MOVE_DISTANCE
        elif lateral_move == LateralMove.Right:
            ship_x += MOVE_DISTANCE
        ship_rect.x = ship_x

        # 縦移動
        if vertical_move == VerticalMove.Up:
            ship_y -= MOVE_DISTANCE
        elif vertical_move == VerticalMove.Down:
            ship_y += MOVE_DISTANCE
        ship_rect.y = ship_y

        # 当たり判定
        if ship_rect.left <= 0:
            lateral_move = LateralMove.Right

        if ship_rect.right >= SCREEN_WIDTH:
            lateral_move = LateralMove.Left

        if ship_rect.top <= 0:
            vertical_move = VerticalMove.Down

        if ship_rect.bottom >= SCREEN_HEIGHT:
            vertical_move = VerticalMove.Up

        # 再描画
        screen.fill((230, 230, 230))
        screen.blit(ship_image, ship_rect)
        pygame.display.flip()