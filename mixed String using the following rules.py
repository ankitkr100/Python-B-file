def mixed_str():
    s1 = "Abc"
    s2 = "Xyz"
    s3 = []
    first_two = s1[0]+s2[int(len(s2)-1)]
    middle_two = s1[int(len(s1)/2)] + s2[int(len(s2)/2)]
    last_two = s1[len(s1)-1] + s2[0]
    s3 = first_two + middle_two + last_two
    print("The mixed string is:", s3)
s1 = "Abc"
s2 = "Xyz"
#print("The mixed string is:", s3)
mixed_str()



