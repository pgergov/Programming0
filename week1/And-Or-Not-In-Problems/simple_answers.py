text = input("Enter some random text: ")

if ("hello" in text) or ("Hello" in text):
    print("Hello there, good stranger!")
elif "how are you" in text:
    print("I am fine, thanks. How are you?")
elif "feelings" in text:
    print("I am a machine. I have no feelings baby!")
elif "age" in text:
    print("I have no age. Only current timestamp")
else:
    print("I'm not interested!")
