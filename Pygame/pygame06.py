# 弾の発射
import sys
import pygame

# プログラム開始
if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("pygame06")

    # 弾のオブジェを作成する
    bullet_rect = pygame.Rect(400, 600, 3, 15)  # 引数は(X座標, Y座標, 横幅, 縦幅)

    # bullet_rectのY座標
    bullet_y = float(bullet_rect.y)

    # 移動用管理フラグ
    ship_bullet = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:     # スペースキー
                    ship_bullet = True

        screen.fill((230, 230, 230))

        # 弾の移動
        if ship_bullet == True:
            if bullet_rect.top > 0:
                bullet_y -= 0.3
            else:
                ship_bullet = False
                bullet_y = 600
            bullet_rect.y = bullet_y

            # screenにbullet_rectを描画する
            pygame.draw.rect(screen, (60, 60, 60), bullet_rect)

        pygame.display.flip()