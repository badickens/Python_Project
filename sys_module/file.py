#! python3

'''
Making a program that will be given a file name and a word.  It will look for
the word in the file and count it's number of occurrences

sys.argv is a list - the first index is always the name of the program file itself
 - the second index (sys.argv[1]) will be the file we are checking for the word
 - the third index (sys.argv[2]) will be the word we are looking for in the file
 
'''

import sys

def main():
    
    if (len(sys.argv) < 3) :  # need 3 arguments to run this program
       sys.stderr.write("E: usage " + sys.argv[0] + " <filename> <word>")  
       sys.stderr.flush()

       exit( 2 )  
    else:  
        filename = sys.argv[1]
        needle = sys.argv[2]  # this is the word we are looking for 
    
   
    counter = 0    

    file_handle = open( filename )
    for line in file_handle.readlines():
        words = line.split(" ")

        for word in words:

            if (word == words[-1]):
                # word = word.replace("\n", "")  # a way to remove the return char
                word = word[:-1]   # finding the last character - note - "\n" is one character
                
            if (word == needle):
                counter += 1

    print(counter)

       
if (__name__ == "__main__" ): 
    main()


