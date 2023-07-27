import pickle

# Read Files
with open("total_colors.pickle", "rb") as file:
    total_colors_mod = pickle.load(file)
with open("warm_colors.pickle", "rb") as file:
    warm_colors = pickle.load(file)
with open("cool_colors.pickle", "rb") as file:
    cool_colors = pickle.load(file)
with open("neutral_colors.pickle", "rb") as file:
    neutral_colors = pickle.load(file)

# CHANGE FILE HERE :)
# you can use: data.remove(x) where x is the specific value
# total_colors_mod.remove("safety green")
# warm_colors.remove("safety green")

print("total colors", total_colors_mod)
print("warm colors", warm_colors)
print("cool colors", cool_colors)
print("neutral colors", neutral_colors)



# Write Changes
with open("total_colors.pickle", "wb") as file:
    pickle.dump(total_colors_mod, file)

with open("warm_colors.pickle", "wb") as file:
    pickle.dump(warm_colors, file)

with open("cool_colors.pickle", "wb") as file:
    pickle.dump(cool_colors, file)

with open("neutral_colors.pickle", "wb") as file:
    pickle.dump(neutral_colors, file)