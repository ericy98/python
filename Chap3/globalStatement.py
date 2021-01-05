def spam():
    global eggs #eggs declared global, no local variable created
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs) # 'spam'