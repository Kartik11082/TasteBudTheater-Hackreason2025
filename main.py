from llama_model import LlamaModel
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

llama_model = LlamaModel()

def write_facts_to_file(facts, filename="facts.pl"):
    with open(filename, "a") as file:
        file.write(facts + "\n")

def main():
    llama_model.start_server()
    print(f"{Fore.CYAN}Welcome to the {Style.BRIGHT}Movie Facts and Recommendations Generator!")
    print(f"{Fore.YELLOW}Please choose an option from the menu below:")
    print(f"{Fore.GREEN}1.{Style.RESET_ALL} Generate movie facts in Prolog format")
    print(f"{Fore.GREEN}2.{Style.RESET_ALL} Generate a Prolog query for movie recommendations")
    
    choice = input(f"{Fore.BLUE}Enter your choice (1 or 2): ").strip()
    print(f"{Fore.MAGENTA}You selected option: {choice}")

    if choice == "1":
        question = input(f"{Fore.LIGHTCYAN_EX}Please enter the details of the movies you want to include (e.g., movie name, actors, genres, directors): {Style.RESET_ALL}").strip()
        prompt = (
            f"Generate facts in Prolog format using the following details provided by the user: {question}. "
            f"Format each fact as: movie('movie name', ['genre1', 'genre2'], ['actor1', 'actor2'], 'director').(Just give me the prolog code nothing else)"
        )
        answer = llama_model.ask_question(prompt)
        print(f"{Fore.LIGHTGREEN_EX}Generated Prolog facts:\n{Fore.RESET}{answer}")
        write_facts_to_file(answer)
        print(f"{Fore.GREEN}Facts have been successfully written to 'facts.pl'.")
        llama_model.clear_session()
        llama_model.stop_server()
        
    elif choice == "2":
        question = input(f"{Fore.LIGHTCYAN_EX}Please enter user preferences for favorite actors, directors, and genres: {Style.RESET_ALL}").strip()
        prompt = f"""
            This is the code for the recommendation system in prolog:
            movie('Mad Max: Fury Road', ['Action', 'Adventure'], ['Tom Hardy', 'Charlize Theron'], 'George Miller').

            % Recommended movies for a single user
            recommended_movies(UserGenre, UserActor, UserDirector, Movie) :-
                movie(Movie, Genres, Actors, Director),
                (member(UserGenre, Genres); member(UserActor, Actors); Director = UserDirector).

            % Finding common movies for any number of users (up to 5)
            common_movies(User1Genre, User1Actor, User1Director, User2Genre, User2Actor, User2Director, CommonMovie) :-
                recommended_movies(User1Genre, User1Actor, User1Director, CommonMovie),
                recommended_movies(User2Genre, User2Actor, User2Director, CommonMovie),
                !.

            common_movies(User1Genre, User1Actor, User1Director, User2Genre, User2Actor, User2Director, User3Genre, User3Actor, User3Director, CommonMovie) :-
                recommended_movies(User1Genre, User1Actor, User1Director, CommonMovie),
                recommended_movies(User2Genre, User2Actor, User2Director, CommonMovie),
                recommended_movies(User3Genre, User3Actor, User3Director, CommonMovie).

            common_movies(User1Genre, User1Actor, User1Director, User2Genre, User2Actor, User2Director, User3Genre, User3Actor, User3Director, User4Genre, User4Actor, User4Director, CommonMovie) :-
                recommended_movies(User1Genre, User1Actor, User1Director, CommonMovie),
                recommended_movies(User2Genre, User2Actor, User2Director, CommonMovie),
                recommended_movies(User3Genre, User3Actor, User3Director, CommonMovie),
                recommended_movies(User4Genre, User4Actor, User4Director, CommonMovie).

            common_movies(User1Genre, User1Actor, User1Director, User2Genre, User2Actor, User2Director, User3Genre, User3Actor, User3Director, User4Genre, User4Actor, User4Director, User5Genre, User5Actor, User5Director, CommonMovie) :-
                recommended_movies(User1Genre, User1Actor, User1Director, CommonMovie),
                recommended_movies(User2Genre, User2Actor, User2Director, CommonMovie),
                recommended_movies(User3Genre, User3Actor, User3Director, CommonMovie),
                recommended_movies(User4Genre, User4Actor, User4Director, CommonMovie),
                recommended_movies(User5Genre, User5Actor, User5Director, CommonMovie).
            This is the prompt of user: {question}. I want you to generate a query(This is the syntax: common_movies('Sci-Fi', 'Leonardo DiCaprio', 'Christopher Nolan', 'Action', 'Christian Bale', 'Christopher Nolan', 'Romance', 'Leonardo DiCaprio', 'James Cameron', CommonMovie). (But fill the actors, directors and genres names with proper names)) for the recommendation system in prolog for the given user prompt and give me just the query to run nothing else.
        """
        answer = llama_model.ask_question(prompt)
        print(f"{Fore.LIGHTGREEN_EX}Generated Prolog query:\n{Fore.RESET}{answer}")
        llama_model.clear_session()
        llama_model.stop_server()
        
    else:
        print(f"{Fore.RED}Invalid selection. Please run the program again and choose either option 1 or 2.")
    
if __name__ == "__main__":
    main()
