import base64

#Encoding Fuction
def text_encoder():
    text=input("What would you like to convert: ")
    text = text.encode("ASCII")
    conv_text = base64.b64encode(text)
    print("")
    print(str(text)+ "converted is " + str(conv_text))

#Decoding Fuction
def text_decoder():
    encoded_text=input("What would you like me to decode: ")
    decoded_text = base64.b64decode(encoded_text)
    print(str(encoded_text) + " Decoded is " + str(decoded_text))

#Main fuction
def base64Conv():
    print("Welcome to my Base64 converter! \n 1.Encode text \n 2.Encode image(WIP) \n 3.Decode Text \n 4.Decode Image" ) 
    user_input = int(input("what can I do for you: "))
    if user_input == 1:
        print("")
        text_encoder()
    elif user_input ==2:
        print("WIP")
    elif user_input ==3:
        print("")
        text_decoder()
        
base64Conv()