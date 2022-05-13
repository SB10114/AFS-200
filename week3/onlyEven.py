prompt = input('Please enter a positive number: ')

if prompt.isdigit():
    a = int(prompt)
    for i in range(0, a+1, 2):
        print(i) 