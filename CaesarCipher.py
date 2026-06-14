alphabet= ['a', 'b', 'c' ,'d', 'e','f','g','h','i','j', 'k','l','m','n','o', 'p', 'q','r','s','t', 'u', 'v', 'w','x','y','z']

direction= input("Type 'encode' to encrypt. type 'decode' to decrypt:\n").lower()
text= input("Type your message:\n").lower()
shift= int(input("Type the shift number:\n"))

shift = shift % len(alphabet)

def encrypt(original_text, shift_amount):
    place_holder=''
    for letter in original_text:
        if letter in alphabet:
            x = (alphabet.index(letter) + shift) % len(alphabet)
            place_holder += alphabet[x]
        else:
            place_holder += letter
    print(f"The cipher message is:\n {place_holder}")


def decrypt(cipher_text, shift_amount):
    place_holder= ''
    ceaser_text = text
    shift_amount = shift

    for letter in text:
        if letter in alphabet:
            x = (alphabet.index(letter) - shift) % len(alphabet)
            place_holder += alphabet[x]
        else:
            place_holder += letter
    print(f"The original message was:\n {place_holder}")        

if direction=='encode':
    encrypt(original_text= text ,shift_amount = shift)

elif direction=='decode':
    decrypt(cipher_text = text, shift_amount= shift)