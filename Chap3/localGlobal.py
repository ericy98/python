# def spam():
#     eggs = 31337
# spam()
# print(eggs) #prints error 'eggs' not defined

# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)

# def bacon():
#     ham = 101
#     eggs = 0

# spam() #only prints 99 bc spam is only called

def spam():
    print(eggs)

eggs = 42
spam()
print(eggs) # prints 42 twice