"""This file show how to do spelling correction using Python."""

from textblob import TextBlob


if __name__ == "__main__":
    sentence = input("Enter your sentence : ")
    corrected_sentence = TextBlob(sentence).correct()
    print("Your sentence with corrected words : ")
    print(corrected_sentence)
