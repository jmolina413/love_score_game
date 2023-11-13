import random


# Function to calculate love score and provide feedback
def calculate_love_score():
    # Generate a random love score
    love_score_text = random.randint(1, 100)

    # Determine feedback based on the love score
    if love_score_text <= 30:
        feedback_text = "This relationship needs work."
        heart_text = "♥"
    elif love_score_text <= 60:
        feedback_text = "You have potential. Keep working on it."
        heart_text = "♥♥"
    else:
        feedback_text = "You're deeply in love. It's a match made in heaven."
        heart_text = "♥♥♥"
    return love_score_text, heart_text, feedback_text


# Storytelling function
def tell_love_story():
    print(f"Once upon a time, there was a love story between {your_name} and {partner_name}.")
    print(f"They decided to check their love compatibility and the result was in...")
    print(f"Love score for {your_name} and {partner_name} is {love_score}%")
    print(f"Visual Representation: {heart}")
    print(f"Feedback: {feedback}")
    print(f"This is what the stars have to say about their love. Will they live happily ever after?")


# Ask the user to input their name and their partner's name
while True:
    your_name = input("Enter your name: ")
    partner_name = input("Enter your partner's name: ")

    # Calculate the love score, visual representation, and feedback
    love_score, heart, feedback = calculate_love_score()

    # Print the love score, visual representation, and feedback along with the names
    tell_love_story()

    # Ask the user if they want to play again
    play_again = input("Play again? (yes or no): ")
    if play_again.lower() != "yes":
        break
