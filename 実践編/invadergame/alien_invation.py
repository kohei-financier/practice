import sys
import pygame

from bullet import Bullet
from settings import Settings
from ship import Ship
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """ゲームのアセットと動作を管理する全体的なクラス"""

    def __init__(self):
        """ゲームを初期化し、ゲームのリソースを作成する"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("エイリアン侵略")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Playボタンを作成する
        self.play_button = Button(self, "Play")

    def run_game(self):
        """ゲームのメインループを開始する"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        # キーボードとマウスのイベントを監視する
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """プレイヤーがPlayボタンをクリックしたら新規ゲームを開始する"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:

            # ゲームの設定値をリセットする
            self.settings.initialize_dynaminc_settings()

            # ゲームの統計情報を初期化する
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # 残ったエイリアンと弾を廃棄する
            self.aliens.empty()
            self.bullets.empty()

            # 新しい艦隊を作成し、宇宙船を中央に配置する
            self._create_fleet()
            self.ship.center_ship()

            # マウスカーソルを非表示にする
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """キーを押すイベントに対応する"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """キーを離すイベントに対応する"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False

    def _fire_bullet(self):
        """新しい弾を生成し、bulletsグループに追加する"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """弾の位置を更新し、古い弾を廃棄する"""
        self.bullets.update()

        # 見えなくなった弾を廃棄する
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # 存在する弾を破壊し、新しい艦隊を作成する
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # レベルを増やす
            self.stats.level += 1
            self.sb.prep_level()

    def _create_fleet(self):
        """エイリアンの艦隊を作成する"""
        # 1列のエイリアンを作成する
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (alien_width * 2)
        number_aliens_x = available_space_x // (2 * alien_width)

        # 画面に収まるエイリアンの列数を決定する
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (2 * alien_height)

        # エイリアンの艦隊を作成する
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                # エイリアンを1匹作成し、列の中に配置する
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """エイリアンを1匹作成し、列の中に配置する"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """エイリアンが画面の端に達した場合に適切な処理を行う"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """艦隊を下に移動し、横移動の方向を変更する"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """艦隊にいる全エイリアンの位置を更新する"""
        self._check_fleet_edges()
        self.aliens.update()

        # エイリアンと宇宙船の衝突を探す
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # 画面の一番下に到達したエイリアンを探す
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _ship_hit(self):
        """エイリアンと宇宙船の衝突に対応する"""
        if self.stats.ships_left > 0:
            # 残りの宇宙船の数を減らす
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # 残ったエイリアンと弾を廃棄する
            self.aliens.empty()
            self.bullets.empty()

            # 新しい艦隊を生成し、宇宙船を中央に配置する
            self._create_fleet()
            self.ship.center_ship()

            # 一時停止する
            sleep(0.5)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        # ループを通過するたびに画面を再描画する
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # 得点の情報を描画する
        self.sb.show_score()
        self.sb.check_high_score()

        # ゲームが非アクティブ状態のときに「Play」ボタンを描画する
        if not self.stats.game_active:
            self.play_button.draw_button()

        # 最新の状態の画面を表示する
        pygame.display.flip()


if __name__ == "__main__":
    # ゲームのインスタンスを作成し、ゲームを実行する
    ai = AlienInvasion()
    ai.run_game()
