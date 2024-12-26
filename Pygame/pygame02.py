# スクリーンを描画する

import sys      # インタプリタや実行環境に関するライブラリ
import pygame   # pygame（パイゲーム）は画像処理、音声処理機能を含んだゲーム開発用ライブラリ

# プログラム開始
if __name__ == "__main__":

    # Pygameを使用するにあたり必要な初期化処理
    pygame.init()

    # 「pygame.display」はウィンドウ、Surfaceはウィンドウ内の描画領域

    # 戻り値はSurface（描画領域）
    screen = pygame.display.set_mode((800, 600))    # 引数は(横幅, 縦幅)

    # タイトル
    pygame.display.set_caption("pygame02")

    # 画面を再描画するループ
    while True:

        # イベントを取得する
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # ウィンドウを閉じる
                sys.exit()                  # プログラム終了

        # 描画領域を再描画する
        screen.fill((230, 230, 230))        # 引数は背景色

        # ウィンドウを最新の状態にする
        pygame.display.flip()