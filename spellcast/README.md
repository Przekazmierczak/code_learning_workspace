# Spellcast solver

## Overview

This is a Flask web application for finding words on a Discord's Spellcast game board. It utilizes a Trie data structure for efficient word lookup.
Rules: https://discord.fandom.com/wiki/SpellCast

## Features

- **Trie Data Structure:** The application uses a Trie to store and search for valid Scrabble words.
- **Web Interface:** Users can input game board configurations via a web form.
- **Word Finder:** The application identifies words on the game board, considering special blocks and their point values.

## How to Run

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the Flask application:

    ```bash
    flask --app app run
    ```

3. Open your web browser and navigate to [http://localhost:5000/](http://localhost:5000/) to use the application.

## Dependencies

- Flask==2.1.1

## File Structure

- `app.py`: The main Flask application file.
- `templates/`: Directory containing html file.
- `static/`: Directory containing java script and css files.
- `words/`: Directory containing JSON files with Scrabble words.

## Contributing

Feel free to contribute by opening issues or submitting pull requests. Your contributions are welcome!