from art import logo, vs
from game_data import data
from random import choice
# import os


def clearscreen(number_lines=100):
    """Clear the console.
number_lines is an optional argument used only as a fall-back.
"""

    # if os.name == "posix":
    #     # Unix, Linux, macOS, BSD, etc.
    #     os.system('clear')
    # elif os.name in ("nt", "dos", "ce"):
    #     # DOS/Windows
    #     os.system('CLS')
    # else:
    # Fallback for other operating systems.
    print('\n' * number_lines)


print(logo)

score = 0

comp_a = choice(data)
comp_b = choice(data)

while True:
    while comp_b == comp_a:
        comp_b = choice(data)


    def gen_comp_details(comp):
        details = [comp["name"], comp["description"], comp["country"], comp["follower_count"]]

        return details


    comp_a_name, comp_a_description, comp_a_country, comp_a_followers = gen_comp_details(comp_a)
    comp_b_name, comp_b_description, comp_b_country, comp_b_followers = gen_comp_details(comp_b)

    print(f"Compare A: {comp_a_name}, a {comp_a_description}, from {comp_a_country}")
    print(vs)
    print(f"Against B: {comp_b_name}, a {comp_b_description}, from {comp_b_country}")

    guess = None
    while guess != "A" and guess != "B":
        guess = input("Who has more followers? (A or B): ").upper()

        if guess != "A" and guess != "B":
            print("Invalid input... Guess must be (A or B)!")


    def validate_guess(g, a, b):
        if a > b:
            return g == "A"
        else:
            return g == "B"


    is_correct = validate_guess(guess, comp_a_followers, comp_b_followers)

    if is_correct:
        score += 1
        comp_a = comp_b
        comp_b = choice(data)
        clearscreen()
        print(logo)
        print(f"Your score so far is {score}")
    else:
        print(f"Your score so far is {score}")
        print("You failed! Game ends...")
        higher_follower = comp_a_name if comp_a_followers > comp_b_followers else comp_b_name
        lower_follower = comp_b_name if higher_follower == comp_a_name else comp_a_name
        print(f"{higher_follower} has more follower than {lower_follower}")
        break
