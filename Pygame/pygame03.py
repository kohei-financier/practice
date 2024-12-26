# 宇宙船の描画
import sys
import pygame

# プログラム開始
if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("pygame03")

    # 画像ファイルを取り込む
    ship_image = pygame.image.load("Pygame\\ship.bmp")

    # 画像ファイルから「四角形のオブジェ」を生成する
    ship_rect = ship_image.get_rect()

    # オブジェの描画位置、midbottomはオブジェの中央下部の座標
    ship_rect.midbottom = (400, 300)    # 引数は左上を基点とした(X座標, Y座標)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 描画領域を再描画するのが先
        screen.fill((230, 230, 230))

        # ship_rectの位置にship_imageを描画する
        screen.blit(ship_image, ship_rect)

        pygame.display.flip()