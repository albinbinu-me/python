
try:
    text = """happy holy
abcdefghijklmnopqrstuvwxyz
    """
    with open('test.txt','w') as file:
        written = file.write(text)
        if written:
            print("wrote the text->",text)
        else:
            print("unable to wrote")
except Exception as e:
    print(e)