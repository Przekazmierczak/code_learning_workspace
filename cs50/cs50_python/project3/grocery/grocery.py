dic = {}
while True:
    try:
        item = input().upper()
    # brak after user click ctr + d
    except EOFError:
        print("")
        # Create a list of dictionary keys
        list = list(dic.keys())
        # Sort the list
        list.sort()
        for element in list:
            print(f"{dic[element]} {element}")
        break
    else:
        # Create the new key
        if item not in dic:
            dic[item] = 1
        # Add the new number to the existed key
        else:
            dic[item] += 1