import base64
#base 64 fucntions
def b64_encoder():
    text=input("What would you like to convert: ")
    text = text.encode("ASCII")
    conv_text = base64.b64encode(text).decode()
    text = text.decode()
    print("")
    print(str(text)+ " converted is " + str(conv_text))


def b64_decoder():
    encoded_text=input("What would you like me to decode: ")
    decoded_text = base64.b64decode(encoded_text)
    print(str(encoded_text) + " Decoded is " + str(decoded_text))

#base 32 fuctions
def b32_encoder():
    text32=input("What would you like to convert: ")
    text32=text32.encode("ASCII")
    conv_text32 = base64.b32encode(text32).decode()
    text32 = text32.decode()
    print("")
    print(str(text32)+ " converted is " + str(conv_text32))

def b32_decoder():
    encoded_text32=input("What would you like me to decode: ")
    decoded_text32= base64.b32decode(encoded_text32)
    print(str(encoded_text32) + " Decoded is " + str(decoded_text32))

#base 16 fuctions 
def b16_encoder():
    text16=input("What would you like to convert: ")
    text16 = text16.encode("ASCII")
    conv_text16 = base64.b16encode(text16).decode()
    text16 = text16.decode()
    print("")
    print(str(text16)+ " converted is " + str(conv_text16))

def b16_decoder():
    encoded_text16=input("What would you like me to decode: ")
    decoded_text16= base64.b16decode(encoded_text16)
    print(str(encoded_text16) + " Decoded is " + str(decoded_text16))

#Image stuff
def image_encoder():
    file_path = input("Enter File path")
    with open("file_path", "rb") as image_file:
        img_data = image_file.read()
    conversion_type = int(input(print("What base are we going to use \n 1.Base 16 \n 2.Base 32 \n 3.Base 64 \n Selection(Pick a Number):")))
    if conversion_type == 1:
        img_b16_code = base64.b16encode(img_data)
        print(img_b16_code)
    elif conversion_type == 2:
        img_b32_code = base64.b32encode(img_data)
        print(img_b32_code)
    elif conversion_type == 3:
        img_b64_code = base64.b64encode(img_data)
        print (img_b64_code)


#Main fuction
def Encoder():
    print("Welcome to my Base64 converter! \n 1.Encode text \n 2.Encode image(WIP) \n 3.Decode Text \n 4.Decode Image" ) 
    user_input = int(input("what can I do for you: "))
    if user_input == 1:
        print("")
        base_selection = int(input("What base do you want to use \n 1.Base 16 \n 2.Base 32 \n 3.Base 64 \n Selection(Pick a Number):"))
        if base_selection == 1:
            b16_encoder()
        elif base_selection == 2:
            b32_encoder()
        elif base_selection == 3:
            b64_encoder()
    elif user_input ==2:
        image_encoder()

    elif user_input ==3:
        print("")
        base_selection2 = int(input("What is it in \n 1.Base 16 \n 2.Base 32 \n 3.Base 64 \n Selection(Pick a Number):"))
        if base_selection2 == 1:
            b16_decoder()
        elif base_selection2 == 2:
            b32_decoder()
        elif base_selection2 ==3:
            b64_decoder()
        
Encoder()
