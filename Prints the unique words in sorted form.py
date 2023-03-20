items = "Input comma separated sequence of words"
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(items)))))