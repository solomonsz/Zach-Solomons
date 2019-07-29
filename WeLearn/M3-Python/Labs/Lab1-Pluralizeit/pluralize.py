#my_name = "Zach"
#friend1 = "Alice"
#friend2 = "John"
#friend3 = "Bob"

#print(
#    "My name is %s and my friends are %s, %s, and %s"%
#    (my_name, friend1, friend2, friend3)
#)
num1 =  (raw_input("Number: "))
word1 = str(raw_input("Object: "))

if num1 == '1':
    print(num1 + " " + word1)
elif num1 == 0 or num1 > 1 and word1[-2:] == "oy":
    print(num1 + " " + word1[:-2] + "oys")
elif num1 == 0 or num1 > 1 and word1[-2:] == "uy":
    print(num1 + " " + word1[:-2] + "uys")
elif num1 == 0 or num1 > 1 and word1[-2:] == "ay":
    print(num1 + " " + word1[:-2] + "ays")
elif num1 == 0 or num1 > 1 and word1[-2:] == "ey":
    print(num1 + " " + word1[:-2] + "eys")
elif num1 == 0 or num1 > 1 and word1[-1:] == "y":
    print(num1 + " " + word1[:2] + "ies")
elif num1 == 0 or num1 > 1 and word1[-2:] == "us":
    print(num1 + " " + word1[:4] + "i")
elif num1 == 0 or num1 > 1 and word1[-2:] == "ch":
    print(num1 + " " + word1 + "es")
elif num1 == 0 or num1 > 1 and word1[-3:] == "ife":
    print(num1 + " " + word1[:1] + "ives")
elif num1 == 0 or num1 > 1 and word1[-2:] == "sh":
    print(num1 + " " + word1 + "es")
elif num1 == 0 or num1 > 1:
    print(num1 + " " + word1 + "s")
else:
    print(word1)
