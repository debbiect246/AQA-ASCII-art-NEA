#importing necessary modules
import sys
import time

#the function for encoding
def encoder(art):
    #set variables
    #holds data to be encoded
    codify = ''
    #hold character before characrter in codify 
    previous_character = ''
    #counts number of letters in ascii image
    counter = 1

    if not art: return ''

    #loop, for characters in string add to counter
    for char in art:
        if char != previous_character:
            if previous_character:
                codify += str(counter) + previous_character
            counter = 1
            previous_character = char
            if counter>10:
                string.insert(0)
        else:
            counter += 1
    else:

        codify += str(counter) + previous_character
        return codify
#The function for decoding
def decoder(data):  
    decode = ''
    add = ''
    for char in data:
        if char.isdigit():
            add += char
        else:
            decode += char * int(add)
            add = ''
    return decode

#menu
while True:
    print("******************************************MAIN MENU******************************************")
    print('                                                                                            ')
    choice = input("""                                                                                 
                      A: Enter RLE                                                                     
                      B: Display ASCII art
                      C: Convert to ASCII art
                      D: Convert to RLE
                      Q: Quit
                      Please enter a letter corresponding to your choice: """)
    if choice == "A" or choice =="a":
        while True:
            RLE = int(input('How many lines of RLE compressed data do you want to enter:'))
            if RLE > 1:
                Enter = input('Enter the code line by line until all lines entered:')
                lemon=decoder(Enter)
                print(lemon)
            else:
                print ('Please enter a value greater than 1')
                time.sleep(0.1)
    elif choice == "B" or choice =="b":
        art = input('Enter file name as _____.txt: ')
        s = open(art).read()
        print(s)
    elif choice == "C" or choice =="c":
        rle = input('Enter file name as _____.txt: ')
        decoding=decoder(rle)
        print(decoding)
    elif choice=="D" or choice=="d":
        ConverttoRLE()
    elif choice=="Q" or choice=="q":
        print('Goodbye')
        sys.exit
    else:
        print("You must only select either A,B,C, or D.")
        print("Please try again")
        
