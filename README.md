# CS50 AI Minesweeper

A Minesweeper game with an AI that uses logical inference to identify safe moves and mine locations. 

## Contributions

`minesweeper.py`:

**Sentence Class**

`known_mines`: Returns a set of cells in the sentence that are known to be mines.

`known_safes`: Returns a set of cells in the sentence that are known to be safe.

`mark_mine`: Updates the sentence by removing the cell known to be a mine while maintaining logical correctness.

`mark_safe`: Updates the sentence by removing the cell known to be safe while maintaining logical correctness.

**MinesweeperAI Class**

`add_knowledge`: Marks a cell as safe, adds a new sentence to the AI's knowledge based on neighboring mine counts, and makes new inferences about safe cells or mines.

`make_safe_move`: Returns a safe move (a cell) that hasn’t been made yet, or None if no safe moves are available.

`make_random_move`: Returns a random move that hasn't been made and is not known to be a mine, or None if no valid moves are available.

### Testing

A test script (`test_minesweeper.py`) has been developed to verify the correct operation of all listed functions.

### Technologies Used

- `Unittest`
- `PyGame`

### Usage

- main: `python3 runner.py`
- test: `python3 test_minesweeper.py`