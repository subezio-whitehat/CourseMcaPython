#13. Create a list of colors from comma-separated color names entered by user. Display
#first and last colors.
items = input("Input comma separated sequence of words:")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))