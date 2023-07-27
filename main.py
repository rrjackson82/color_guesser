# This is a python script to guess your favorite color!

import random
import pickle
import time

# wcn stands for warm cool neutral

has_guessed_color = False
ran_out_of_guesses = False
has_compared_wcn = False

total_colors_base = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black", "white", "grey",
                     "purple", "pink", "teal", "maroon"]
warm_colors = ["red", "orange", "yellow", "pink", "maroon", "gold", "mauve", "brown"]
cool_colors = ["green", "blue", "indigo", "violet", "purple", "teal", "country blue"]
neutral_colors = ["black", "white", "grey", "silver"]
my_disliked_colors = ["yellow", "pink", "purple", "teal", "brown", "violet", "indigo"]

total_colors_mod = total_colors_base[:]
disliked_colors = []
possible_liked_colors = total_colors_mod[:]

liked_color = ""

questions_asked = 0

with open("total_colors.pickle", "rb") as file:
    total_colors_mod = pickle.load(file)
with open("warm_colors.pickle", "rb") as file:
    warm_colors = pickle.load(file)
with open("cool_colors.pickle", "rb") as file:
    cool_colors = pickle.load(file)
with open("neutral_colors.pickle", "rb") as file:
    neutral_colors = pickle.load(file)

possible_liked_colors = total_colors_mod[:]

print("This program tries to guess your favorite color by eliminating all your disliked/non-favorite colors. ")
time.sleep(2)

def remove_wcn(list):
    # The program asks if your favorite color is warm, neutral, or cool. It would remove all other colors
    # I ran into an issue with this. If I had already removed a color (x) that was (y (warm, cool, neutral)),
    # and tried to remove all values in list y from possible_liked_colors, it would throw an error.
    # How could you remove something that isn't there?
    # This function checks if color z is even in possible_liked_colors before it removes it.

    for i in range(len(list)):
        if list[i] in possible_liked_colors:
            possible_liked_colors.remove(list[i])


def reference():
    wm = ", ".join(warm_colors)
    cm = ", ".join(cool_colors)
    nm = ", ".join(neutral_colors)
    print("Warm colors:", wm + ".\nCool colors:", cm + ".\nNeutral colors:", nm + ".")


def is_wcn(color):
    warm_cool_or_neutral = input("Would you consider " + color + "a warm, neutral, or cool color? ")
    match warm_cool_or_neutral[0]:
        case "w":
            warm_colors.append(color)
        case "c":
            cool_colors.append(color)
        case "n":
            neutral_colors.append(color)

def compare_wcn():
    # This function returns true if there is in imbalance between warm, neutral, and cool colors in the
    #   disliked_colors list.
    c = 0
    w = 0
    n = 0
    for i in range(len(disliked_colors)):
        # print(disliked_colors, i)
        if disliked_colors[i] in warm_colors:
            w += 1
        if disliked_colors[i] in cool_colors:
            c += 1
        if disliked_colors[i] in neutral_colors:
            n += 1
    if c >= (len(disliked_colors)/2):
        return True
    elif w >= (len(disliked_colors)/2):
        return True
    elif n >= (len(disliked_colors)/2):
        return True
    elif c <= (len(disliked_colors)/2):
        return True
    elif w <= (len(disliked_colors)/2):
        return True
    elif n <= (len(disliked_colors)/2):
        return True
    else:
        return False


def determine_color():
    i = random.randint(0, (len(possible_liked_colors) - 1))
    return possible_liked_colors[i]


for _ in range(3):
    disliked_color = input("What color do you not like/is not your favorite color? ").lower()
    if disliked_color not in total_colors_mod:
        print("Hmm... I haven't heard of that color.")
        total_colors_mod.append(disliked_color)
        is_wcn(disliked_color)
        has_guessed_color = False
    if disliked_color in possible_liked_colors:
        possible_liked_colors.remove(disliked_color)
    disliked_colors.append(disliked_color)
    questions_asked += 1


while not has_guessed_color:
    with open("total_colors.pickle", "rb") as file:
        total_colors_mod = pickle.load(file)
    with open("warm_colors.pickle", "rb") as file:
        warm_colors = pickle.load(file)
    with open("cool_colors.pickle", "rb") as file:
        cool_colors = pickle.load(file)
    with open("neutral_colors.pickle", "rb") as file:
        neutral_colors = pickle.load(file)
    if not has_guessed_color:
        if len(possible_liked_colors) > 0:
            if len(possible_liked_colors) == 1:
                liked_color = possible_liked_colors[0]
                fc = input("Is " + liked_color.capitalize() + " your favorite color (y/n)? ")
                if fc[0] == "y":
                    liked_color = guess
                    has_guessed_color = True
                    break
                elif fc[0] == "n":
                    possible_liked_colors.remove(guess)
            guess = determine_color()
            q = input("Is " + guess + " your favorite color (y/n)? ").lower()
            if q[0] == "y":
                liked_color = guess
                has_guessed_color = True
                break
            elif q[0] == "n":
                possible_liked_colors.remove(guess)
                # has_guessed_color = False
        elif len(possible_liked_colors) <= 0:
            ran_out_of_guesses = True
            liked_color = input("Aw man. Im all out of guesses. What is your favorite color? ")
            total_colors_mod.append(liked_color)
            has_guessed_color = True
            questions_asked += 1
            alt = True
            break

        if not has_compared_wcn:
            is_wcn_imbalance = compare_wcn()
            if is_wcn_imbalance:
                wcn = input("Is your favorite color a warm color, a neutral color, or a cool color? "
                            "(type 'what' if you need a reference) ").lower()
                if wcn == "what":
                    reference()
                    wcn = input("Is your favorite color a warm color, a neutral color, or a cool color? "
                                "(type 'what' if you need a reference) ").lower()
                if wcn[0] == "w" and wcn != "what":
                    print("Got it.")
                    remove_wcn(cool_colors)
                    remove_wcn(neutral_colors)
                if wcn[0] == "c":
                    print("Got it.")
                    remove_wcn(neutral_colors)
                    remove_wcn(warm_colors)
                if wcn[0] == "n":
                    print("Got it.")
                    remove_wcn(cool_colors)
                    remove_wcn(warm_colors)
                has_compared_wcn = True

        disliked_color = input("What color do you not like/is not your favorite color? ").lower()
        if disliked_color not in total_colors_mod:
            print("Hmm... I haven't heard of that color.")
            total_colors_mod.append(disliked_color)
            is_wcn(disliked_color)
            has_guessed_color = False
        if disliked_color in possible_liked_colors:
            possible_liked_colors.remove(disliked_color)
        disliked_colors.append(disliked_color)
        questions_asked += 1

    with open("total_colors.pickle", "wb") as file:
        pickle.dump(total_colors_mod, file)

    with open("warm_colors.pickle", "wb") as file:
        pickle.dump(warm_colors, file)

    with open("cool_colors.pickle", "wb") as file:
        pickle.dump(cool_colors, file)

    with open("neutral_colors.pickle", "wb") as file:
        pickle.dump(neutral_colors, file)

if ran_out_of_guesses:
    print("I would never have guessed that", liked_color + "was your favorite color.")
if has_guessed_color:
    if liked_color in my_disliked_colors:
        print(liked_color.capitalize(), "kinda sucks IMO.")
    else:
        print("Nice!", liked_color.capitalize(), "is a great color!")
