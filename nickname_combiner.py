import random

def generate_nicknames(first_name, last_name, style):
    """ Generate creative nicknames using letters from anywhere in the name. """
    emojis = ["🔥", "💎", "✨", "🐉", "🌟", "🦄", "💥", "🖤", "❤️", "⚡"]
    symbols = ["-", "_", "*", "#", "@", "$"]
    
    name_combined = first_name + last_name  # Merge full name for random selection

    short_names = [
        first_name[:3] + last_name[-3:],  
        last_name[:3] + first_name[-3:],  
        first_name[:2] + last_name[:2],  
        "".join(random.sample(name_combined, 4)),  # Random 4 letters from anywhere in name
    ]

    fun_names = [
        first_name[::-1] + last_name[::-1],  
        "".join(random.sample(name_combined, 5)) + random.choice(symbols),  # Random letters + symbol  
        first_name.capitalize() + random.choice(emojis) + last_name.lower(),  
        "".join(random.sample(name_combined, 6)),  # Random 6 letters from anywhere in name
    ]

    formal_names = [
        first_name + " " + last_name,  
        first_name.capitalize() + " " + last_name.capitalize(),  
        f"{first_name} {last_name} {random.choice(emojis)}",  
        "".join(random.sample(name_combined, 5)) + "_" + "".join(random.sample(name_combined, 3)),  # Random parts joined with "_"
    ]

    # Choose style
    if style == "short":
        nicknames = short_names
    elif style == "fun":
        nicknames = fun_names
    elif style == "formal":
        nicknames = formal_names
    else:
        nicknames = short_names + fun_names + formal_names  # Default: Mix all styles

    return nicknames

def save_nicknames_to_file(nicknames):
    """ Save generated nicknames to a file with UTF-8 encoding. """
    with open("nicknames.txt", "w", encoding="utf-8") as file:
        for nickname in nicknames:
            file.write(nickname + "\n")

def nickname_combiner():
    """ Main function to get user input and generate nicknames. """
    print("\n🎭 Welcome to Auto Nickname Combiner! 🎭")
    
    first_name = input("🖊️ Enter your first name: ")
    last_name = input("🖊️ Enter your last name: ")
    
    print("\n🎨 Choose a nickname style:")
    print("1. Short")
    print("2. Fun")
    print("3. Formal")
    style_choice = input("Enter style (short/fun/formal): ").strip().lower()

    nicknames = generate_nicknames(first_name, last_name, style_choice)

    print("\n✨ Generated Nicknames ✨")
    for nickname in nicknames:
        print("👉 " + nickname)

    save_nicknames_to_file(nicknames)
    print("\n💾 Nicknames saved in 'nicknames.txt'!")

# Run the nickname generator
nickname_combiner()
