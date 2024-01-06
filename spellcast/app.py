import json
from flask import Flask, render_template, request

class Trie:
    """
    Nodes of a prefix tree, with alphabet letters as prefix.

    self.end: indicate if the end of the word is reached.
    self.letters: dictionary (hash map):
        key: alphabet letter.
        value: position to next node.
    """
    def __init__(self):
        self.end = False
        self.letters = {}

# FLASK components
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Build the Trie data structure
        trie_root = build_trie()

        # Create game boards from user input
        game_board, special_block_board = create_boards()

        # Flatten the game board arrays for rendering
        letters_array = flat(game_board)
        letters_array = [x.upper() for x in letters_array]
        special_block_array = flat(special_block_board)

        # Find words on the game board using the Trie
        words_found = find_words(game_board, special_block_board, trie_root)

        # Sort and format the results
        answers = dict(sorted(words_found.items(), key=lambda item: item[1][1], reverse=True))
        post = True

        return render_template("index.html", answers=answers,
                               post=post,
                               letters_array=letters_array,
                               special_block_array=special_block_array)
    
    return render_template("index.html")

# Helper functions

def build_trie():
    """
    Build a Trie.
    
    Read English words (legal in Scrabble) from JSON files and create Trie nodes.
    """
    trie_root = Trie()
    # Loop from 2 to 15 - words are stored in 14 seperate files
    for i in range(2, 16):
        file_name = f"words/{i}-letter-words.json"
        with open(file_name, encoding="utf-8") as file:
            words = json.load(file)
            for word in words:
                curr_node = trie_root
                curr_word = word['word']
                for letter in curr_word:
                    if letter not in curr_node.letters:
                        curr_node.letters[letter] = Trie()
                    curr_node = curr_node.letters[letter]
                curr_node.end = True
    return trie_root


def flat(array):
    """
    Flatten the input array.

    Parameters:
        array: List[List[]]

    Returns:
        flat_list: List[]

    Example:
        Input: array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        Return: flat_list = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
    """
    flat_list = []
    for row in array:
        flat_list.extend(row)

    return flat_list


def create_boards():
    """
    Import user inputs from webpage and create two arrays.

    Returns:
        - game_board: List[List[]] (2D array with input letters).
        - special_block_board: List[List[]] (2D array with input special blocks (double letter, tripple letter, double points)).

    Example:
        Return:
            - game_board: [[h, a, r, r, y][p, o, t, t, e]]
            - special_block_board: [["normal_block", "normal_block", "normal_block", "normal_block", "normal_block"]],
                                    ["normal_block", "double_letter", "normal_block", "normal_block", "double_points"]]
    """
    game_board = []
    special_block_board = []
    # Count position of the block from 1 to 25
    counter = 1
    # For rows
    for _ in range(5):
        # Arrays to store whole rows
        temp_array = []
        temp_block_array = []
        # For columns
        for _ in range(5):
            # Get letter and special block from webpage with form request
            letter = (request.form.get(f"{counter}")).lower()
            special_block = (request.form.get(f"special_block_{counter}"))

            temp_array.append(letter)
            temp_block_array.append(special_block)

            counter += 1

        game_board.append(temp_array)
        special_block_board.append(temp_block_array)

    return game_board, special_block_board


def find_words(game_board, special_block_board, trie):
    """
    Find words that can be create on the input board.

    Parameters:
        - game_board: List[List[]] (2D array with input letters).
        - special_block_board: List[List[]] (2D array with input special blocks (double letter, tripple letter, double points)).
        - trie: Root of the trie with input Scrabble words.

    Returns:
        result: dictionary (hashmap)
            - key: string (word)
            - value: tuple(List[], int)
                - List[]: board positions of letters
                - int: value of the word according to the value of letters in points and special blocks value

    Example:
        Input: game_board: [[c, a, t][d, o, g]], special_block_board: [["normal_block", "normal_block", "normal_block"], ["normal_block", "normal_block", "normal_block"]], trie: root
        Return: result: {cat: ([1, 2, 3], 8), dog: ([4, 5, 6], 7)}
    """
    result = {}
    # For rows
    for row in range(5):
        # For columns
        for col in range(5):
            check_position(row, col, trie, set(), [], game_board, special_block_board, result)
    return result


def check_position(row, col, node, visited, path, game_board, special_block_board, result):
    """
    Find every word that is possible to be created from the input position and put it in result dictionary.

    Parameters:
        - row: int
        - col: int
        - node: class (object)
        - visited: set(tuple(int, int)) (hash set with visited positions.)
        - path: List[tuple(int, int)] (array with visited positions.)
        - game_board: List[List[]] (2D array with input letters.)
        - special_block_board: List[List[]] (2D array with input special blocks (double letter, tripple letter, double points).)
        - result: dictionary (hashmap)
            - key: string (word)
            - value: tuple(List[], int)
                - List[]: board's position of letters
                - int: value of word according to the value of letters in points and special blocks value
    """
    # Base case
    if row not in range(5) or col not in range(5) or (row, col) in visited or game_board[row][col] not in node.letters:
        return
    
    curr_node = node.letters[game_board[row][col]]
    visited.add((row, col))
    path.append((row, col))

    # curr_node.end == True means that we found a word
    if curr_node.end:
        # Dictionary with letters and theirs points
        letters_values = {"a":1, "b":4, "c":5, "d":3, "e":1, "f":5, "g":3, "h":4, "i":1, "j":7, "k":6, "l":3, "m":4,
                           "n":2, "o":1, "p":4, "q":8, "r":2, "s":2, "t":2, "u":4, "v":5, "w":5, "x":7, "y":4, "z":8}
        
        double = False
        # Create a list with word's letters
        word_list = []
        # create a list with letters' positions on the board (from 1 to 25)
        position_in_numbers = []
        value = 0

        # Iterate through positions in the path to reconstruct the word and calculate points
        for position in path:
            word_row, word_col = position
            letter = game_board[word_row][word_col]
            special_block = special_block_board[word_row][word_col]
            letter_value = letters_values[letter]
            # Check if the current positon is one of the special blocks
            if special_block == "double_letter":
                letter_value *= 2
            elif special_block == "triple_letter":
                letter_value *= 3
            elif special_block == "double_points":
                double = True

            word_list.append(letter)
            value += letter_value
            position_in_numbers.append(word_row * 5 + word_col + 1)
        
        # If one of the blocks was "double_points", double the final value
        if double:
            value *= 2
        # If the word is longer than 5 characters, count it as a "long word" and add extra 10 points
        if len(path) > 5:
            value += 10

        # Change word_list into a string
        word_string = "".join(word_list).capitalize()

        # Check if the word is already in the result and if its value is bigger than current one
        if word_string not in result or result[word_string][1] < value:
            result[word_string] = (position_in_numbers, value)

    # Create an array of neighbour blocks
    neighbours = [(row - 1, col + 1), (row, col + 1), (row + 1, col + 1), 
                    (row - 1, col), (row + 1, col), 
                    (row - 1, col - 1), (row, col - 1), (row + 1, col - 1),]
    
    # Recursive call on neighbour blocks
    for neighbour in neighbours:
        neighbour_row, neighbour_col = neighbour
        check_position(neighbour_row, neighbour_col, curr_node, visited, path, game_board, special_block_board, result)
    
    # Remove the last position from visited and path after checking that way
    visited.remove((row, col))
    path.pop()