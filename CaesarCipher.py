import asciiart

alphabet= ['a', 'b', 'c' ,'d', 'e','f','g','h','i','j', 'k','l','m','n','o', 'p', 'q','r','s','t', 'u', 'v', 'w','x','y','z']


print(asciiart.logo)
direction= input("Type 'encode' to encrypt. type 'decode' to decrypt:\n").lower()
text= input("Type your message:\n").lower()
shift= int(input("Type the shift number:\n"))

shift = shift % len(alphabet)

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

caeser(original_text=text, shift= shift, direction= direction)