def countChar(str, x):
    count = 0
    for i in range(len(str)):
        if (str[i] == x) :
            count += 1
    n = 10
     
    # atleast k repetition are required
    repetitions = n // len(str)
    count = count * repetitions
 
    # if n is not the multiple of the
    # string size check for the remaining
    # repeating character.
    l = n % len(str)
    for i in range(l):
        if (str[i] == x):
            count += 1
    return count