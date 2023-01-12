print("Enter Your Message Below :) ")
message = input()

while message:
    msg = message.replace("die", "****")
    print(f"message {msg} has been sent")
    print("Enter Message, (Q) Quit")
    message = input()

    if message == "":
        print("Enter Message, (Q) Quit")
        message = input()
    elif message.lower() == "q":
        break