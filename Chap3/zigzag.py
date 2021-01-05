import time, sys
indent = 0 #how many spaces to indent
indentIncreasing = True #whether the indentation is increasing or not

try:
    while True: #the main program loop
        print('' *indent, end='')
        print('********')
        time.sleep(0.1) #pauses for 1/10th of a second

    if indentIncreasing:
        #increase num of spaces
        indent = indent + 1
        if indent == 20:
            #change direction:
            indentIncreasing = False

    else:
        #decrease num of spaces
        indent = indent - 1
        if indent == 0:
            #change direction
            indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()