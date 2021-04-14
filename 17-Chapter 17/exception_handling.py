# Exception handling
# Try except else finally

while True:
    try:
        age=int(input('Enter your age : '))
        break
    except ValueError:
        print('May you enter sting instead of number, Try again...')
    except:
        ('Invalid Input....')    

if age>18:
    print ('You can play this game') 
else:
    print('You can\'t play this game')           