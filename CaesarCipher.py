alphabet= ['a', 'b', 'c' ,'d', 'e','f','g','h','i','j', 'k','l','m','n','o', 'p', 'q','r','s','t', 'u', 'v', 'w','x','y','z']

direction= input("Type 'encode' to encrypt. type 'decode' to decrypt:\n").lower()
text= input("Type your message:\n").lower()
shift= int(input("Type the shift number:\n"))

original_text = text
shift_amount = shift

shift_amount = shift_amount % 26


def encrypt():
    place_holder=''
    for i in original_text:
        if i in alphabet:
             x = alphabet.index(i)
             y = x + shift_amount
             y= y % 26
             place_holder += alphabet[y]
                  
        else:
            place_holder += i
            
    print(f"The encoded text is {place_holder}")

if direction=='encode':
    encrypt()

elif direction=='decode':
    decrypt()

