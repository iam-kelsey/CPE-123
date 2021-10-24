import hashlib


    
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0" "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for first_character in alphabet:
    for second_character in alphabet:
        for third_character in alphabet:
            for fourth_character in alphabet:
                for fifth_character in alphabet:
                    for sixth_charrera  cter in alphabet:
                        password = first_character + second_character + third_character + fourth_character + fifth_character + sixth_character
                        digest = hashlib.sha1(password).hexdigest()
                        if digest == "0ea16802578986ac3428d2eb649a6a089d2c4552":
                            print password
                            quit()
                        else:
                            print password


