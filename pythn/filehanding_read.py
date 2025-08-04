try:
    with open("demo.txt", "r") as f:
        content = f.read()
        if content:
            print(content)
        else:
            print("File is empty.")
except FileNotFoundError:
    print("demo.txt not found.")