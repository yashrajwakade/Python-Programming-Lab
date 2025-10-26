# Program to encode a message by adding a key-value pair to every character


message = input("Enter your message: ")
key = int(input("Enter key value: "))


encoded_message = ""

for ch in message:
    if ch.isalpha(): 

        if ch.isupper():
            encoded_message += chr((ord(ch) - 65 + key) % 26 + 65)

        else:
            encoded_message += chr((ord(ch) - 97 + key) % 26 + 97)
    else:

        encoded_message += ch

print("Encoded message:", encoded_message)
