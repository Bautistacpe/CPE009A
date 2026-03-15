def word_censor():
    bad_words = ["fuck","shit","bitch","damn","Fuck","Shit","Bitch","Damn"]
    text = (input("Enter a sentence: "))
    for word in bad_words:
        if word in text:
            text = text.replace(word, "*" * len(word))
    return text

print(word_censor())