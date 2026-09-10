origin_text = "Hello, world!"

result = ""

for char in origin_text:
    result += ord(char) * "+"
    result += "."
    result += ">"
    result += "\n"

print(result)
