string = "Hello World"
string_without_spaces = string.replace(" ", "")
print(string_without_spaces)

string_without_spaces = "".join(string.split())
print(string_without_spaces)
