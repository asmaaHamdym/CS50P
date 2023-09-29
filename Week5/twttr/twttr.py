def main():
    SEN = input("Input: ")
    print(shorten(SEN))




def shorten(word):
    letters = ["a", "e", "i", "o", "u"]

    for c in word:
        if c.lower() in letters:
            word=word.replace(c, "")
    return word



if __name__ == "__main__":
    main()