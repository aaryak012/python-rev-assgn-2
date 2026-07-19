#Q17
text = "hello world"
new_text = ""
for char in text:
    if char != " ":
        new_text += char.upper()
print(new_text)
