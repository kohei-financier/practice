# 宇宙船と弾の発射
import sys
import pygame

# プログラム開始
if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("pygame07")

    # 宇宙船
    ship_image = pygame.image.load("Pygame\\ship.bmp")
    ship_rect = ship_image.get_rect()
    ship_rect.midbottom = (400, 500)

    # 弾
    bullet_rect = pygame.Rect(0, 0, 3, 15)  # とりあえず初期位置は0,0

    # 移動用管理フラグ
    ship_right = False
    ship_left = False
    ship_bullet = False

    # 宇宙船と弾の座標
    ship_x = float(ship_rect.x)
    bullet_y = float(ship_rect.y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship_right = True
                elif event.key == pygame.K_LEFT:
                    ship_left = True
                elif event.key == pygame.K_SPACE:
                    if ship_bullet == False:
                        ship_bullet = True

                        # 弾は宇宙船の座標
                        bullet_rect.midbottom = ship_rect.midbottom

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship_right = False
                elif event.key == pygame.K_LEFT:
                    ship_left = False

        # 宇宙船の移動
        if ship_right == True and ship_rect.right < 800:
            ship_x += 0.1
        elif ship_left == True and ship_rect.left > 0:
            ship_x -= 0.1
        ship_rect.x = ship_x

        screen.fill((230, 230, 230))

        # 弾の移動
        if ship_bullet == True:
            if bullet_rect.top > 0:
                bullet_y -= 0.3
            else:
                ship_bullet = False
                bullet_y = ship_rect.y
            bullet_rect.y = bullet_y
            pygame.draw.rect(screen, (60, 60, 60), bullet_rect)

        screen.blit(ship_image, ship_rect)
        pygame.display.flip()