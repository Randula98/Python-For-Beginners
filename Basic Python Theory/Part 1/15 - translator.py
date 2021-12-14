
def translate(text):
    output = ""
    for letter in text:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                output = output + "*"
            else:
                output = output + "#"
        else:
            output = output + letter
    return output


input = input("Enter a Text : ")
print(translate(input))