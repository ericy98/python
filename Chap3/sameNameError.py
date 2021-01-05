def spam():
    print(eggs) #ERROR, considers eggs to be local
    eggs = 'spam local'

eggs = 'global'
spam()