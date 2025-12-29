anime_flashcards = {
    "naruto": [
        ("Who is Naruto's father?", "minato"),
        ("What is Naruto's dream?", "hokage"),
        ("What is the nine-tailed beast called?", "kurama")
    ],
    "one piece": [
        ("Who is the captain of Straw Hat pirates?", "luffy"),
        ("What is the treasure called?", "one piece"),
        ("Who is the swordsman?", "zoro")
    ],
    "attack on titan": [
        ("Who is the main protagonist?", "eren"),
        ("What are humans fighting against?", "titans"),
        ("Who is the strongest soldier?", "levi")
    ]
}




def choose_anime():
    print("\nAvailable Anime:")
    for anime in anime_flashcards:
        print("-", anime.title())

    while True:
        choice = input("\nChoose an anime: ").lower()
        if choice in anime_flashcards:
            return choice
        else:
            print(" Invalid choice. Please choose from the list.")


def play_game(anime_name):
    score = 0
    questions = anime_flashcards[anime_name]

    print(f"\n Starting Flashcard Game: {anime_name.upper()}\n")

    for question, answer in questions:
        user_answer = input(question + " ").lower()

        if user_answer == answer:
            print(" Correct!\n")
            score += 1
        else:
            print(f" Wrong! Correct answer: {answer}\n")

    print(f" Final Score: {score}/{len(questions)}")


def main():
    print(" Welcome to the Anime Flashcard Game ")

    while True:
        anime = choose_anime()
        play_game(anime)

        replay = input("\nDo you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("\n Thanks for playing. See you next time!")
            break


main()