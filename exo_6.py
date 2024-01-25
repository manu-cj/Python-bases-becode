def HelloSir(username):
    if username == "":
        print("Hello Anonymous")
    elif username != "":
        print(f"Hello {username}")
        if username == "Steve Jobs":
            print("What ! You are Steve Jobs ?")
    
    
name = input("Whats your name sir ? ")
HelloSir(name)