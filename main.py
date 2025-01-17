from llama_model import LlamaModel


llama_model = LlamaModel()
def main():
    choice = input("1. Generate facts using Natural language\n2. Generate recommendation using natural language\nEnter your choice: ")
    print("Choice:", choice)

    if choice == "1":
        question = input("Enter facts of movies that you want to include. It should contain movie's name, actors, genres and directors: ")
        prompt = f"Generate facts in prolog and give me just the code of facts in prolog(In this format: movie('movie name', ['genre1', 'genre2'], ['actor1', 'actor2'], 'director').) nothing else for this facts about movies gviven by user in natural language:{question}"
        answer = llama_model.ask_question(prompt)
        print(f"Answer: {answer}, type: {type(answer)}")
        llama_model.clear_session()
        llama_model.stop_server()
    elif choice == "2":
        question = input("Enter your question: ")
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
            This is the prompt of user: {question}. I want you to generate a query(Like this: common_movies('user1genre', 'user1actor', 'user1director', 'user2genre', 'user2actor', 'user2director', CommonMovie). (But fill the actors, directors and genres names with proper names)) for the recommendation system in prolog for the given user prompt and give me just the query to run nothing else.
        """
        answer = llama_model.ask_question(prompt)
        print(f"Answer: {answer}")
        llama_model.clear_session()
        llama_model.stop_server()
    else:
        print("Invalid choice. Please enter a valid choice.")
    
if __name__ == "__main__":
    main()