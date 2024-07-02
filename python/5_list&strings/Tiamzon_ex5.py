# This program encrypts a list of text using Ceasar's Cipher in two level.
# Created by: Edgar Alan Emmanuel B. Tiamzon III
# Re-exericse #5
# 12/21/23

# References
# enumerate() - https://www.w3schools.com/python/ref_func_enumerate.asp
# ceasar cipher - https://www.scaler.com/topics/caesar-cipher-python/
 
# Global variable
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
texts_list = []
encrypted_texts1 = []
encrypted_texts2 = []

def display_menu():
    print()
    print("╔═════════════════════════════╗")
    print("║ [1] Enter List of Texts     ║")
    print("║ [2] Encrypt Text/s          ║")
    print("║ [3] View Encrypted Texts    ║")
    print("║ [4] Exit                    ║")
    print("╚═════════════════════════════╝")

    choice = int(input("Enter choice: "))
    return choice


# The 'encrypt_all' function performs a caesar cipher encryption by shifting each alphabet letter in the input text by a specified 
# number of positions (determined by the shift value), while the letters and non-alphabetic characters remains unchanged.
def encrypt_all(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                shifted_index = (ALPHABET.index(char.lower()) + shift) % 26
                result += ALPHABET[shifted_index].upper()
            else:
                shifted_index = (ALPHABET.index(char) + shift) % 26
                result += ALPHABET[shifted_index]
        else:
            result += char

    return result

# The 'add_texts' serves the user to input a specific number of texts, clears existing texts, 
# and updates the texts_list with the new input texts for encryption.
def add_texts():
    text_count = int(input("How many texts do you want to add: "))

    texts_list.clear()
    encrypted_texts1.clear()
    encrypted_texts2.clear()
    
    for i in range(text_count):
        count = input(f"Enter text [{i+1}]: ")
        texts_list.append(count)

    return texts_list

def encrypt_all_2(text, shift1, shift2):
    encrypted_text = encrypt_all(text, shift1)
    double_encrypted = encrypt_all(encrypted_text, shift2)
    return double_encrypted

def encrypt_texts(shift1, shift2):
    if len(texts_list) == 0:
        print("Enter text first!")
        return []

    encrypted_texts1.clear()
    encrypted_texts2.clear()

    for text in texts_list:
        encrypted1 = encrypt_all(text, shift1)
        encrypted_texts1.append(encrypted1)
        
        encrypted2 = encrypt_all(encrypted1, shift2)
        encrypted_texts2.append(encrypted2)
        
    return encrypted_texts2

def view_encrypted():
    if not encrypted_texts1:
        print("No encrypted text available")
        return
    
    counter = 1
    for text in texts_list:
        print(f"[{counter}] {text} =====> {encrypted_texts1[counter-1]} =====> {encrypted_texts2[counter-1]}")
        counter += 1 

# MAIN PROGRAM LOOP
running = True
while running:
    choice = display_menu()
    if choice == 1:
        texts_list = add_texts()
    elif choice == 2:
        level_shift1 = int(input("First Level Shift: "))
        level_shift2 = int(input("Second Level Shift: "))
        encrypted_texts2 = encrypt_texts(level_shift1, level_shift2)
    elif choice == 3:
        view_encrypted()
    elif choice == 4:
        running = False
        print("Goodbye!")
    else:
        print("Invalid choice! Please try again.")
