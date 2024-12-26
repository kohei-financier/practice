# 宇宙船の操作 その2
import sys
import pygame

# プログラム開始
if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("課題01")

    ship_image = pygame.image.load(r"C:\\Users\\0902JP\\python_workspace\\Pygame\\ship.bmp")
    ship_rect = ship_image.get_rect()
    ship_rect.midbottom = (400, 300)

    # 移動用管理フラグ
    ship_right = True
    ship_left = True
    ship_up = True
    ship_down = True

    # ship_rectのX座標
    # ship_rect.xはint型で演算されるので、float型のローカル変数を使用している
    ship_x = float(ship_rect.x)
    ship_y = float(ship_rect.y)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # ship_rect.rightはship_rectの右上のX座標、ship_rect.leftは左上のX座標
        if ship_right == True and ship_rect.right:
            if ship_rect.right >= 800:
                ship_x -= 0.3

        if ship_left == True and ship_rect.left:
            if ship_rect.left < 0:
                ship_x += 0.3
        
        ship_rect.x = ship_x
        
        if ship_up == True and ship_rect.top:
            if ship_rect.bottom >= 600:
                ship_y -= 0.3
            
        if ship_down == True and ship_rect.bottom:
            if ship_rect.top < 0:
                ship_y += 0.3
        
        ship_rect.y = ship_y
    

        # 再描画
        screen.fill((230, 230, 230))
        screen.blit(ship_image, ship_rect)
        pygame.display.flip()