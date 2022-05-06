#create an application that asks the user to input a number from 0-100
#90-100:A
#80-89:B
#70-79:C
#60-69:D
#0-59:F

grade = int(input('Enter your numerical grade '))

if 90 <= grade <= 100:
    print("A")
elif 80 <= grade <=89:
    print("B")
elif 70 <= grade <=79:
    print("C")
elif 60 <= grade <=69:
    print("D")
elif 0 <= grade <=59:
    print("F")
else:
    print('not a number 0 to 100')


