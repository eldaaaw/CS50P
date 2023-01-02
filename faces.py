def main():
    msg=input("Enter your msg: ")
    newMsg = msg.replace(":)","🙂").replace(":(","🙁")
    print(newMsg)

main()