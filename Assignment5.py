def encoder(plain_text):
    coded_text = ""
    
    for char in plain_text:
        x = str(ord(char))
        
        if len(x) == 2:
            x = "0" + x
        
        coded_text += x
    
    return coded_text

def decoder(coded_text):
    decoded_text = ""
    decoding_array = []
    
    for i in range(len(coded_text)):
        if (i+1) % 3 == 0:
            decoding_array.append(coded_text[i-2]+coded_text[i-1]+coded_text[i])
        else: 
            pass

    for letter in decoding_array:
        if letter[0] == "0":
            letter = letter[1] + letter[2]
        else:
            pass
        
        decoded_text += chr(int(letter))
        
    return decoded_text

if __name__ == "__main__":

    plain_text = input("Input a sentence here:")
    
    encoded_text = encoder(plain_text)
    decoded_text = decoder(encoded_text)
        
    print(f'Input sentence: {plain_text}')
    print(f'\nEncoded: {encoded_text}')
    print(f'\nDecoded: {decoded_text}')

