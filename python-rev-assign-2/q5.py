#Q5
text = "python"
count = 0
for letter in text:
    if letter in "aeiou":
        count += 1
print(f"Found {count} vowels")
