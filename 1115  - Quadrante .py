entrada = []
x,y=1,1
while x != 0 and y != 0:
    entrada = input().split()
    x = int(entrada[0])
    y = int(entrada[1])
    if x == "" or y == "":
        break
        
    if x > 0 and y > 0:
        print("primeiro")
    elif x < 0 and y > 0:
        print("segundo")
    elif x < 0 and y < 0:
        print("terceiro")
    elif x > 0 and y < 0:
        print("quarto")
