# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils
total_length = 0
with open("birth_dev.tsv") as tsv:
    lines = tsv.readlines()
    total_length = len(lines)

accuracy = utils.evaluate_places("birth_dev.tsv", ["London"] * total_length)
print(f"Correct {accuracy[1]} of {accuracy[0]}, Accuracy: {accuracy[1] / accuracy[0] * 100}%")