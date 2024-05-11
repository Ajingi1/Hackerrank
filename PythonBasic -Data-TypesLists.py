def main():
    N = int(input())
    arr = []
    for i in range(N):
        command = input().strip()
        if not command:
            break
        operation, *rest = command.split(" ")
        j, k = convert_int(rest)
        execute_command(arr, operation, j, k)
    
def convert_int(rest):
    if len(rest)  == 2:
        return int(rest[0]), int(rest[1])
    elif len(rest) == 1:
        return int(rest[0]), None
    else:
        return None, None
    
def execute_command(arr, operation, j=None, k=None):
    if (j is None and k is None) and operation != "print":
        execute = getattr(arr, operation)
        execute()
    elif (j is None and k is None) and operation == "print":
        print(arr)
    elif (j is not None and k is not None):
        value = [j, k]
        getattr(arr, operation)(*map(int, value))
    elif (j is not None and k is None):
        if isinstance(j, int):
            getattr(arr, operation)(j)
    elif (j is None and k is not None):
        getattr(arr, operation)(k)
        

if __name__ == '__main__':
    main()
