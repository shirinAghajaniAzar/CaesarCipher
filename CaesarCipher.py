import asciiart

alphabet= ['a', 'b', 'c' ,'d', 'e','f','g','h','i','j', 'k','l','m','n','o', 'p', 'q','r','s','t', 'u', 'v', 'w','x','y','z']

print(asciiart.logo)

cipher = True


def caeser(original_text, shift, direction):
      place_holder=''
      if direction=='decode':
        shift *= -1
      for letter in original_text:
        if letter in alphabet:
            x = (alphabet.index(letter) + shift) % len(alphabet)
            place_holder += alphabet[x]
        else:
            place_holder += letter
      print(f"The message is:\n {place_holder}")

while cipher:

    direction= input("Type 'encode' to encrypt. type 'decode' to decrypt:\n").lower()
    text= input("Type your message:\n").lower()
    shift= int(input("Type the shift number:\n"))

    shift = shift % len(alphabet)

    caeser(original_text=text, shift= shift, direction= direction)
    
    while True:

        continue_encryption = input("Would you like to continue?\njust 'Yes' or 'No' ").lower()
        if continue_encryption == 'yes':
            break
        elif continue_encryption == 'no':
            cipher = False
            print("Ok!\nGoodbye:>")
            break
        else:
            print("\n*I told you just 'Yes' or 'No'!*\n")