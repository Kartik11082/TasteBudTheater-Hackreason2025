# Movie Facts and Recommendation System

This project leverages the Llama3.2 model to generate Prolog-based movie facts and provide personalized movie recommendations based on user preferences.

## Project Overview

- **`llama_model.py`**: Contains the `LlamaModel` class for interacting with the Llama3.2 model.
- **`main.py`**: The primary script for running the application.
- **`README.md`**: Documentation for setting up and using the project.

## Requirements

- Python 3.x
- `requests` library
- SWI-Prolog (for executing Prolog queries)

## Installation

1. **Install Python dependencies**:

   ```bash
   pip install requests
   ```

2. **Ensure SWI-Prolog is installed**:

   Install SWI-Prolog from [SWI-Prolog official website](https://www.swi-prolog.org/).

3. **Ensure Llama3.2 server availability**:

   Start the Llama3.2 server using the command:

   ```bash
   ollama serve
   ```

## Usage Instructions

1. **Run the main script**:

   ```bash
   python main.py
   ```

2. **Options in the application**:

   - **Option 1**: Generate movie facts from natural language input.

     Example:

     ```
     Enter your choice: 1
     Enter facts of movies that you want to include. It should contain the movie's name, actors, genres, and directors: Inception, Leonardo DiCaprio, Sci-Fi, Christopher Nolan
     ```

     Output:

     ```
     movie('Inception', ['Sci-Fi'], ['Leonardo DiCaprio'], 'Christopher Nolan').
     ```

   - **Option 2**: Generate movie recommendations based on user preferences provided in natural language.

     Example:

     ```
     Enter your choice: 2
     Enter preferences for all users about their favourite actors, directors, and genres: Sci-Fi, Leonardo DiCaprio, Christopher Nolan
     ```

     Output:

     ```
     common_movies('Sci-Fi', 'Leonardo DiCaprio', 'Christopher Nolan', 'Action', 'Tom Hardy', 'George Miller', CommonMovie).
     ```

## Example Queries

1. **Generate Movie Facts**:

   - Input:
     ```
     Enter facts of movies that you want to include: Titanic is a movie made by James and has Leo and Kate in it and it is a romance movie.
     ```
   - Output:
     ```
     movie('The Dark Knight', ['Action'], ['Christian Bale'], 'Christopher Nolan').
     ```

2. **Generate Movie Recommendations**:

   - Input:
     ```
     Enter preferences for all users: user 1 likes romances movies with Leo in it and made by James cameron and user 2 likes drama with marlon Brando and made by Francis Ford Coppola
     ```
   - Output:
     ```
     common_movies('Action', 'Christian Bale', 'Christopher Nolan', 'Sci-Fi', 'Matthew McConaughey', 'Christopher Nolan', CommonMovie).
     ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or new features.
