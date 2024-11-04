for i in range(101):
    primo = True 
    if i <= 1:
        primo = False 
    else:
        for n in range(2, int(i**0.5) + 1):
            if i % n == 0:
                primo = False 
              
    if primo:
        print(i)