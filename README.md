# Number Slider Puzzle Game

A classic 15-puzzle style sliding number puzzle game built with Python and Pygame. Challenge yourself to arrange the numbers in order by sliding tiles into the empty space!

<img width="1211" height="864" alt="image" src="https://github.com/user-attachments/assets/4cb8a5e3-e1d4-4df3-a6fd-9aa5cc3efb0c" />

## Game Overview

The Number Slider Puzzle is a digital version of the classic 15-puzzle. The goal is to arrange the numbered tiles in ascending order from 1 to 15, with the empty space at the bottom right. Players can slide tiles adjacent to the empty space, testing their problem-solving skills and patience.

### Features

- **4x4 Grid Layout** - Classic 15-puzzle mechanics
- **Random Shuffle** - Each game starts with a unique, randomized board
- **Move Counter** - Track your progress with a move counter
- **Win Detection** - Automatic detection when puzzle is solved with victory message
- **Visual Feedback** - Color changes when you win (tiles turn green)
- **Reset Functionality** - Start a new game anytime
- **User-Friendly Interface** - Clean design with intuitive controls
- **Console Feedback** - Game state printed to console for debugging

### How to Play

1. **Objective**: Arrange all numbers from 1 to 15 in order (left to right, top to bottom)
2. **Empty Space**: The bottom-right corner should be empty when solved
3. **Movement**: Click on any tile adjacent to the empty space to slide it
4. **Strategy**: Plan your moves carefully to avoid getting stuck

### Controls

| Control | Action |
|---------|--------|
| **Mouse Click** | Move selected tile |
| **R Key** | Reset the game |
| **ESC Key** | Quit the game |
| **Reset Button** | Start a new game |

## Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Step 1: Clone or Download the Repository
```bash
git clone https://github.com/yourusername/number-slider-puzzle.git
cd number-slider-puzzle
```

### Step 2: Install Required Dependencies
```bash
pip install pygame
```

### Step 3: Run the Game
```bash
python puzzle.py
```

## Project Structure

```
number-slider-puzzle/
│
├── puzzle.py           # Main game file
├── README.md           # This file
├── screenshot.png      # Game screenshot (optional)
└── requirements.txt    # Dependencies (optional)
```

## Game Design

### Visual Elements
- **Grid Size**: 400x400 pixels
- **Tile Colors**: Light blue tiles with dark blue borders
- **Empty Space**: Gray tile
- **Win State**: Tiles turn green
- **Info Panel**: Shows moves counter and reset button

### Game Mechanics
- The empty space is represented by 0 in the game logic
- Valid moves are only possible with tiles adjacent to the empty space
- The shuffle algorithm performs 100 random valid moves to ensure solvability

## Technical Implementation

### Key Components

1. **PuzzleGame Class**: Main game class handling all logic
2. **Board Representation**: 4x4 matrix storing tile values
3. **Move Validation**: Checks adjacency before allowing moves
4. **Win Condition**: Verifies if board matches solved state
5. **Event Handling**: Processes user input (mouse clicks, keyboard)
6. **Rendering**: Draws game state using Pygame

### Core Functions

- `shuffle_board()`: Randomizes board using valid moves
- `find_empty()`: Locates empty space position
- `get_valid_moves()`: Returns list of valid moves from empty space
- `check_win()`: Determines if puzzle is solved
- `make_move()`: Processes tile movement

## Troubleshooting

### Common Issues

**Issue: Game window doesn't appear**
- Ensure pygame is properly installed: `pip install pygame`
- Check if you have a display server running
- Try running as administrator

**Issue: "No module named pygame"**
- Install pygame: `pip install pygame`
- Use pip3 if on Linux/Mac: `pip3 install pygame`

**Issue: Game runs but no window shows (headless environment)**
- The game includes a console fallback mode
- Or use the console version by uncommenting the fallback code

## Future Enhancements

Planned features for future releases:
- [ ] Timer to track solving time
- [ ] Different difficulty levels (3x3, 4x4, 5x5)
- [ ] High score tracking
- [ ] Hint system
- [ ] Sound effects
- [ ] Undo/Redo functionality
- [ ] Save/Load game state
- [ ] Multiple themes/color schemes

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Add comments for complex logic
- Update documentation as needed
- Test thoroughly before submitting

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the classic 15-puzzle game
- Built with Pygame - thanks to the Pygame community
- Special thanks to all contributors and testers

## Contact & Support

- **Email**: your.email@example.com
- **GitHub Issues**: For bug reports and feature requests
- **Discussions**: Join the conversation in GitHub Discussions

## Fun Facts

- The 15-puzzle was invented by Noyes Palmer Chapman in 1874
- The puzzle has approximately 1.3 trillion possible configurations
- Half of all random configurations are unsolvable (our shuffle ensures solvability!)

---

**Enjoy the game! Challenge your friends and see who can solve it in the fewest moves!** 🧩✨

[⬆ Back to Top](#-number-slider-puzzle-game)
