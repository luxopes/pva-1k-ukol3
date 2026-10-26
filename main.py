import second as s

def main():
    user_input = input("Zadejte text s kódovanými emoji (např. Jsem šťastný :joy:): ")
    result = s.replace_emojis(user_input)
    print("Výsledek:", result)

if __name__ == "__main__":
    main()
