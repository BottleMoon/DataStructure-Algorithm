import sys
IN = sys.stdin.readline

stack = list()
for _ in range(int(IN())):
    command = IN().strip('\n')
    if 'push' in command :
        command = command.split()
        stack.append(int(command[1]))

    elif command == 'pop':
        if len(stack) == 0 :
            print(-1)
        else : print(stack.pop())

    elif command == 'size':
        print(len(stack))

    elif command == 'empty':
        if len(stack) == 0 :
            print(1)
        else : print(0)

    elif command == 'top':
        if len(stack) == 0 :
            print(-1)
        else : print(stack[-1])