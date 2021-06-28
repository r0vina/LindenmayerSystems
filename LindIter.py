# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 18:34:44 2020

@author: Roneet
"""

def LindIter(System, N):
    
    # LINDITER Returns a Lindenmayer string after calculating N iterations for
    # it. 
    # 
    # Usage: LindenmayerString = LindIter(System, N)
    # 
    # Takes the name of the system as a string, and the number of 
    # iterations as an int, as arguments. The function LindIter contains
    # nested functions for each of the Lindenmayer system types, which in turn
    # calculate a single iteration according to the L-system types' individual
    # configurations. After running N iterations on the initial string 
    # (different for each L-system), the final string is returned.
    #
    # Author: Roneet V. Nagale, s204091@dtu.dk, 2020
    
    LindenmayerString = "Default."
    
    # Each of the following nested functions add one iteration of the
    # L-string to the input string and return it. They are called in a 
    # for loop and are passed the respective initial string for each their 
    # L-system type. They then 

    # Convert the intial string for Koch curves (S) to an L-string. 
    def KochConvert(String):
        #Split the string into an array.
        arrayString = list(String)
        outputString = ''
        
        #Replace characters according to L-system rules.
        for character in arrayString:
            if character == 'S':
                indexS = arrayString.index('S')
                arrayString[indexS] = 'SLSRSLS'
            elif character == 'L':
                  indexL = arrayString.index('L')
                  arrayString[indexL] = 'L'
            elif character == 'R':
                  indexR = arrayString.index('R')
                  arrayString[indexR] = 'R'
        
        # Join the array after the loop finishes, and return the string.
        outputString = outputString.join(arrayString)
        KochString = outputString
        return KochString
    
    # Convert the initial string for Sierpinski Triangles (A) to an L-string
    def SierpinskiConvert(String):
        #Split the string into an array.
        arrayString = list(String)
        outputString = ''
        #Replace characters according to L-system rules.
        for character in arrayString:
            if character == 'A':
                indexA = arrayString.index('A')
                arrayString[indexA] = 'BRARB'
                
            elif character == 'B':
                  indexB = arrayString.index('B')
                  arrayString[indexB] = 'ALBLA'
                  
            elif character == 'L':
                  indexL = arrayString.index('L')
                  arrayString[indexL] = 'L'
            
            elif character == 'R':
                  indexR = arrayString.index('R')
                  arrayString[indexR] = 'R'
        # Join the array after the loop finishes, and return the string.        
        outputString = outputString.join(arrayString)
        SierpinskiString = outputString
        return SierpinskiString
    
    # Convert the initial string for Dragon Curves (FX) to an L-string.
    def DragonCurveConvert(String):
        #Split the string into an array.
        arrayString = list(String)
        outputString = ''
        #Replace characters according to L-system rules.
        for character in arrayString:
            if character == 'X':
                indexA = arrayString.index('X')
                arrayString[indexA] = 'XRYFR'
                
            elif character == 'Y':
                  indexB = arrayString.index('Y')
                  arrayString[indexB] = 'LFXLY'
                  
            elif character == 'L':
                  indexL = arrayString.index('L')
                  arrayString[indexL] = 'L'
            
            elif character == 'R':
                  indexR = arrayString.index('R')
                  arrayString[indexR] = 'R'
        # Join the array after the loop finishes, and return the string.        
        outputString = outputString.join(arrayString)
        DragonCurveString = outputString
        return DragonCurveString
    
    
    # Check which L-system was received as an argument. 
    # If the argument is valid, set a variable to the initial string for the
    # L-system. Pass the variable to the relevant nested function N 
    # times, saving the output in itself each time.
    #
    # Assign the calculated L-string to the LindenmayerString variable,
    # which is returned at the end of the LindIter function.
    # If an invalid argument is revieved, print an error-message to the user
    # and exit the function, returning to the main menu. 
    
    if System == "Koch":
   
        KochString = 'S'
        for n in range(0,N):
            KochString = KochConvert(KochString)
            
      
        LindenmayerString = KochString
        
    elif System == "Sierpinski":
        
        SierpinskiString = 'A'
        for n in range(0,N):
            SierpinskiString = SierpinskiConvert(SierpinskiString)
            
            
        LindenmayerString = SierpinskiString
    elif System == "Dragon Curve":
        
        DragonCurveString = 'FX'
        for n in range(0, N):
            DragonCurveString = DragonCurveConvert(DragonCurveString)
            
        LindenmayerString = DragonCurveString
    else:
        print("Error! No valid system or number found.")
             
    return LindenmayerString

# Test code to check if the LindIter function behaves as expected and returns
# the correct string for each system.

assert LindIter("Koch", 2) == 'SLSRSLSLSLSRSLSRSLSRSLSLSLSRSLS'
assert LindIter("Sierpinski", 2) == 'ALBLARBRARBRALBLA'
