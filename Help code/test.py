# This program allows you to encode and decode lines of text using RLE
# First function allows a line of data to be encoded

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        # If the prev and current characters
        # don't match...
        if char != prev_char:
            # ...then add the count and character
            # to our encoding
            if prev_char:
                encoding += str(count) + prev_char
                #encoding = ("{:02d}".format(encoding))
            count = 1
            prev_char = char
        else:
            # Or increment our counter
            # if the characters do match
            count += 1
    else:
        # Finish off the encoding
        encoding += str(count) + prev_char

    return encoding

#Now test the code for encoding using RLE

print (rle_encode('AAAABBFFFFF'))

#Second function allows a line of lossless compressed data to be decoded

def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        # If the character is numerical...
        if char.isdigit():
            # ...append it to our count
            count += char
        else:
            # Otherwise we've seen a non-numerical
            # character and need to expand it for
            # the decoding
            decode += char * int(count)
            count = ''
    return decode

#Now test the code for decoding using RLE

print (rle_decode('4A2B5F'))

#instructions and menu

print("This program allows you to compress or decompress lines of data")
print("Using lossless compression")
print("Options for you to choose from are")
print("1. Enter RLE")
print("2. Display ASCII art")
print("3. Convert to ASCII art")
print("4. Convert to RLE")
print("5. Quit the program")

choice = int(input("Please type 1, 2, 3, 4 or 5 to select an option\n  >>"))

'''#validation check to check user input

while 1>choice or 5<choice:
    try:
        choice=int(input("Please type 1,2,3,4 or 5 to select an option\n >>"))
    except:
        ValueError
        print("You have made an invalid choice")

    #Code if user chooses choice 1 - enter rle data

if choice==5:
    print("Thanks for using the program, goodbye")

elif choice==1:
    print("You have chosen to enter compressed data")
    lines=int(input("Please enter number of lines of data to encode\n >>")

    #user enters lines of rle and validation check applied
                         
    '''if lines <2:
        try:
            lines=int(input("Number of lines of data must be greater than 2"))
        except:
            ValueError
            print("Number of lines of data is less than 2")
        
        #else:
            #for i in lines_of_rle:
               # data = input("enter line of data to encode\n >>")
               # rle_encode(data)
               # print(rle_encode(data)) '''   
                
              
            

             
       
