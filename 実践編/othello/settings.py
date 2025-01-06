BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
YELLOW = (255, 155, 0)
SIZE = 600
BOARD_SIZE = 12
GRID_SIZE = SIZE // BOARD_SIZE

class Settings:
    
    def __init__(self):
        """ゲームの初期設定"""
        # 画面に関する設定
        self.screen_width = SIZE
        self.screen_height = SIZE
        self.board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        mid = BOARD_SIZE / 2
        self.board[mid - 1][mid - 1] = WHITE
        self.board[mid - 1][mid] = BLACK
        self.board[mid][mid - 1] = BLACK
        self.board[mid][mid] = WHITE
        self.turn = BLACK
        