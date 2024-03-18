def machine():
    keys ="abcdefghijklmnopqrstuvwxyz !"
    value = keys[-1] + keys[0:-1]

    encryptDict = dict(zip(keys,value))
    decryptDict = dict(zip(value,keys))

    message = input("please Enter you message : ")
    mode = input("Please Enter the mode : Encode(E) or Decode(D): ")

    if mode == 'E':
        newMessage = ''.join ([encryptDict[letter] for letter in message.lower()])
    elif mode.upper()=='D':
        newMessage = ''.join([decryptDict[letter] for letter in message.lower()])
    else:
        print("Please enter a correct choice")

    return newMessage

print(machine())
