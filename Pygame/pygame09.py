# 当たり判定
import sys
import pygame

# プログラム開始
if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("pygame09")

    # 宇宙船
    ship_image = pygame.image.load(r"C:\\Users\\0902JP\\python_workspace\\Pygame\\ship.bmp")
    ship_rect = ship_image.get_rect()
    ship_rect.midbottom = (400, 500)
    ship_x = float(ship_rect.x)

    # 弾
    bullet_rect = pygame.Rect(0, 0, 3, 15)
    bullet_y = float(ship_rect.y)

    # エイリアン
    alien_image = pygame.image.load(r"C:\\Users\\0902JP\\python_workspace\\Pygame\\alien.bmp")
    alien_rect = alien_image.get_rect()

    # エイリアンの初期位置
    alien_rect.x = 0
    alien_rect.y = 0

    # エイリアンの座標
    alien_x = float(alien_rect.x)
    alien_y = float(alien_rect.y)

    # 移動用管理フラグ
    ship_right = False
    ship_left = False
    ship_bullet = False
    alien_right = False
    alien_left = True

    # エイリアンの存在
    alien_exis = True

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

        # エイリアンの移動
        if alien_exis == True:
            if alien_left == True:
                alien_x += 0.1
                if alien_rect.right >= 800:
                    alien_left = False
                    alien_right = True
            elif alien_right == True:
                alien_x -= 0.1
                if alien_rect.left <= 0:
                    alien_left = True
                    alien_right = False
            alien_rect.x = alien_x

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

            # 当たり判定
            if alien_exis == True and bullet_rect.x <= alien_rect.right and bullet_rect.x >= alien_rect.left and bullet_rect.y <= alien_rect.bottom:
                alien_exis = False

        # エイリアンの存在
        if alien_exis == True:
            screen.blit(alien_image, alien_rect)

        screen.blit(ship_image, ship_rect)
        pygame.display.flip()