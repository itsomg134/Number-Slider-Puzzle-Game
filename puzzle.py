import pygame
import random
import sys
import os

try:
    pygame.init()
    pygame.display.set_mode((400, 460))
    pygame.display.quit()
except Exception as e:
    print(f"Error initializing pygame: {e}")
    print("Please make sure you have a display available.")
    sys.exit(1)

pygame.init()

WINDOW_SIZE = 400
GRID_SIZE = 4
TILE_SIZE = WINDOW_SIZE // GRID_SIZE
INFO_HEIGHT = 60
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (0, 100, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GRAY = (200, 200, 200)

class PuzzleGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + INFO_HEIGHT))
        pygame.display.set_caption("Number Slider Puzzle")
        
        try:
            self.font = pygame.font.Font(None, 36)
            self.small_font = pygame.font.Font(None, 24)
        except:
            self.font = pygame.font.Font(None, 36)
            self.small_font = pygame.font.Font(None, 24)
        
        self.clock = pygame.time.Clock()
        self.reset_game()
        
        self.print_instructions()
    
    def print_instructions(self):
        """Print instructions to console"""
        print("\n" + "="*50)
        print("NUMBER SLIDER PUZZLE")
        print("="*50)
        print("Instructions:")
        print("1. Click on tiles to move them")
        print("2. Arrange numbers from 1-15 in order")
        print("3. Press R to reset")
        print("4. Press ESC to quit")
        print("="*50 + "\n")
    
    def reset_game(self):
        """Initialize or reset the game"""
        self.board = [[i * GRID_SIZE + j + 1 for j in range(GRID_SIZE)] 
                      for i in range(GRID_SIZE)]
        self.board[GRID_SIZE-1][GRID_SIZE-1] = 0
        
        self.shuffle_board()
        
        self.moves = 0
        self.game_won = False
        print("New game started!")
        
    def shuffle_board(self):
        """Shuffle the board by making random valid moves"""
        moves = 100
        for _ in range(moves):
            empty_pos = self.find_empty()
            possible_moves = self.get_valid_moves(empty_pos)
            if possible_moves:
                move = random.choice(possible_moves)
                self.swap_tiles(empty_pos, move)
    
    def find_empty(self):
        """Find the position of the empty tile (0)"""
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.board[i][j] == 0:
                    return (i, j)
        return (GRID_SIZE-1, GRID_SIZE-1)
    
    def get_valid_moves(self, pos):
        """Get valid moves from current empty position"""
        i, j = pos
        moves = []
        if i > 0: moves.append((i-1, j))
        if i < GRID_SIZE-1: moves.append((i+1, j))
        if j > 0: moves.append((i, j-1))
        if j < GRID_SIZE-1: moves.append((i, j+1))
        return moves
    
    def swap_tiles(self, pos1, pos2):
        """Swap two tiles on the board"""
        i1, j1 = pos1
        i2, j2 = pos2
        self.board[i1][j1], self.board[i2][j2] = self.board[i2][j2], self.board[i1][j1]
    
    def make_move(self, click_pos):
        """Handle player move"""
        if self.game_won:
            return
        
        i, j = click_pos
        empty_pos = self.find_empty()
        
        if (abs(i - empty_pos[0]) + abs(j - empty_pos[1])) == 1:
            self.swap_tiles((i, j), empty_pos)
            self.moves += 1
            print(f"Move {self.moves} made")
            self.check_win()
    
    def check_win(self):
        """Check if puzzle is solved"""
        solved = True
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                expected = i * GRID_SIZE + j + 1
                if i == GRID_SIZE-1 and j == GRID_SIZE-1:
                    expected = 0
                if self.board[i][j] != expected:
                    solved = False
                    break
            if not solved:
                break
        
        if solved:
            self.game_won = True
            print("\n🎉 CONGRATULATIONS! You solved the puzzle! 🎉")
            print(f"Total moves: {self.moves}")
    
    def handle_events(self):
        """Handle game events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.reset_game()
                elif event.key == pygame.K_ESCAPE:
                    return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if y < WINDOW_SIZE:
                    grid_x = x // TILE_SIZE
                    grid_y = y // TILE_SIZE
                    if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
                        self.make_move((grid_y, grid_x))
                        self.print_board()
                elif WINDOW_SIZE <= y < WINDOW_SIZE + INFO_HEIGHT:
                    if 150 <= x <= 250:
                        self.reset_game()
        return True
    
    def print_board(self):
        """Print current board state to console"""
        print("\nCurrent Board:")
        for row in self.board:
            print(" ".join(f"{num:2}" if num != 0 else " ." for num in row))
    
    def draw(self):
        """Draw the game screen"""
        try:
            self.screen.fill(WHITE)
            
            for i in range(GRID_SIZE):
                for j in range(GRID_SIZE):
                    x = j * TILE_SIZE
                    y = i * TILE_SIZE
                    value = self.board[i][j]
                    
                    if value != 0:
                        if self.game_won:
                            color = GREEN
                        else:
                            color = LIGHT_BLUE
                        pygame.draw.rect(self.screen, color, (x, y, TILE_SIZE-2, TILE_SIZE-2))
                        
                        pygame.draw.rect(self.screen, DARK_BLUE, (x, y, TILE_SIZE-2, TILE_SIZE-2), 2)
                        
                        text = self.font.render(str(value), True, BLACK)
                        text_rect = text.get_rect(center=(x + TILE_SIZE//2, y + TILE_SIZE//2))
                        self.screen.blit(text, text_rect)
                    else:
                        pygame.draw.rect(self.screen, GRAY, (x, y, TILE_SIZE-2, TILE_SIZE-2))
                        pygame.draw.rect(self.screen, BLACK, (x, y, TILE_SIZE-2, TILE_SIZE-2), 2)
            
            for i in range(GRID_SIZE + 1):
                pygame.draw.line(self.screen, BLACK, (i * TILE_SIZE, 0), 
                               (i * TILE_SIZE, WINDOW_SIZE), 2)
                pygame.draw.line(self.screen, BLACK, (0, i * TILE_SIZE), 
                               (WINDOW_SIZE, i * TILE_SIZE), 2)
            
            pygame.draw.rect(self.screen, LIGHT_GRAY, (0, WINDOW_SIZE, WINDOW_SIZE, INFO_HEIGHT))
            pygame.draw.line(self.screen, BLACK, (0, WINDOW_SIZE), 
                            (WINDOW_SIZE, WINDOW_SIZE), 2)
            
            moves_text = self.small_font.render(f"Moves: {self.moves}", True, BLACK)
            self.screen.blit(moves_text, (10, WINDOW_SIZE + 10))
            
            if self.game_won:
                win_text = self.small_font.render("🎉 YOU WIN! 🎉", True, RED)
                self.screen.blit(win_text, (10, WINDOW_SIZE + 35))
            
            pygame.draw.rect(self.screen, DARK_BLUE, (150, WINDOW_SIZE + 10, 100, 40))
            reset_text = self.small_font.render("RESET", True, WHITE)
            reset_rect = reset_text.get_rect(center=(200, WINDOW_SIZE + 30))
            self.screen.blit(reset_text, reset_rect)
            
            pygame.display.flip()
        except Exception as e:
            print(f"Drawing error: {e}")
    
    def run(self):
        """Main game loop"""
        running = True
        print("\nGame window should appear now...")
        print("If you don't see a window, check your display settings.")
        
        self.print_board()
        
        while running:
            running = self.handle_events()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        print("\nThanks for playing!")
        sys.exit()

def run_console_version():
    """Run a console-based version of the game"""
    print("\n" + "="*50)
    print("CONSOLE NUMBER SLIDER PUZZLE")
    print("="*50)
    print("Since pygame display isn't working, here's a console version:")
    
    board = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 0]]
    
    # Simple shuffle
    for _ in range(50):
        empty_pos = None
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    empty_pos = (i, j)
        if empty_pos:
            i, j = empty_pos
            moves = []
            if i > 0: moves.append((i-1, j))
            if i < 3: moves.append((i+1, j))
            if j > 0: moves.append((i, j-1))
            if j < 3: moves.append((i, j+1))
            if moves:
                move = random.choice(moves)
                mi, mj = move
                board[i][j], board[mi][mj] = board[mi][mj], board[i][j]
    
    print("\nUse W/A/S/D to move (W=up, A=left, S=down, D=right)")
    print("Enter 'quit' to exit")
    
    moves = 0
    while True:
        print("\nCurrent board:")
        for row in board:
            print(" ".join(f"{num:2}" if num != 0 else " ." for num in row))
        print(f"Moves: {moves}")
        
        solved = True
        expected = 1
        for i in range(4):
            for j in range(4):
                if i == 3 and j == 3:
                    if board[i][j] != 0:
                        solved = False
                else:
                    if board[i][j] != expected:
                        solved = False
                    expected += 1
        
        if solved:
            print("\n🎉 YOU WIN! 🎉")
            print(f"Total moves: {moves}")
            break
        
        move = input("\nEnter move (W/A/S/D): ").upper()
        if move == 'QUIT':
            break
        if move not in ['W', 'A', 'S', 'D']:
            print("Invalid input! Use W, A, S, or D")
            continue
        
        empty_pos = None
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    empty_pos = (i, j)
        
        if empty_pos:
            i, j = empty_pos
            if move == 'W' and i < 3:  # Move tile from below up
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                moves += 1
            elif move == 'S' and i > 0:  # Move tile from above down
                board[i][j], board[i-1][j] = board[i-1][j], board[i][j]
                moves += 1
            elif move == 'A' and j < 3:  # Move tile from right left
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                moves += 1
            elif move == 'D' and j > 0:  # Move tile from left right
                board[i][j], board[i][j-1] = board[i][j-1], board[i][j]
                moves += 1
            else:
                print("Can't move that direction!")

if __name__ == "__main__":
    try:
        game = PuzzleGame()
        game.run()
    except Exception as e:
        print(f"\nError running pygame version: {e}")
        print("\nFalling back to console version...")
        run_console_version()