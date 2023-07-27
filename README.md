# Color Guesser
Here's how it works:

The program stores all of the colors it knows about in a list called "total_colors_base". The reason this is the base version is because each time a user inputs a color that the program has not heard of, it appends that color to another list called "total_colors_mod". It saves this list, along with a few others, to the disk using Pickle.

It then creates two more lists: "disliked_colors" (all colors that the user dislikes), and "possible_liked_colors" (the list of colors that the user could like). Based on these lists along with user input, the program tries to guess your favorite color in the determine_color() function. It does this in a while loop.

The program will even ask you if your favorite color is a warm color (red, yellow), a cool color (blue, green), or a neutral color (white, gray). Based on this input, it will remove all other colors from the possible_liked_colors list. Example: if I said that my favorite color was a cool color, the program would then remove every value from the warm color and neutral color lists.
