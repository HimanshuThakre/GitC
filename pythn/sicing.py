text = "hello world"

substring = text[0:5]  # Extracts 'hello'
print(substring)  # Output: hello
substring = text[:4]
print(substring)  # Output: hell
substring = text[6:]  # Extracts 'world'
print(substring)  # Output: world
substring = text[-5:]  # Extracts 'world' using negative indexing
print(substring)  # Output: world   
substring = text[-11:-6]  # Extracts 'hello' using negative indexing
print(substring)  # Output: hello
substring = text[-11:]  # Extracts 'hello world' using negative indexing
print(substring)  # Output: hello world\
substring = text[::2]  # Extracts every second character
print(substring)  # Output: hlowrd