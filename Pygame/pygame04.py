# 宇宙船の操作 その1
import sys
import pygame

# プログラム開始
if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("pygame04")

    ship_image = pygame.image.load("Pygame\\ship.bmp")
    ship_rect = ship_image.get_rect()
    ship_rect.midbottom = (400, 300)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:      # キーを押した時
                if event.key == pygame.K_w:        # wキー
                    ship_rect.y -= 50
                elif event.key == pygame.K_s:    # sキー
                    ship_rect.y += 50
                elif event.key == pygame.K_d:   # dキー
                    ship_rect.x += 50
                elif event.key == pygame.K_a:    # aキー
                    ship_rect.x -= 50
            # ship_rectのx、yはオブジェ左上の座標

        # 再描画
        screen.fill((230, 230, 230))
        screen.blit(ship_image, ship_rect)
        pygame.display.flip()