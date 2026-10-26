import emoji

def s(text):
    return emoji.emojize(text)

if __name__ == "__main__":
    print(s(":thumbs_up:"))
