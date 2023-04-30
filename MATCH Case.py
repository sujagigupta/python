marks=int(input('enter the marks'))
match marks:
    case marks if marks>90:
        print('0')
    case marks if marks>80:
        print('A+')
    case marks if marks>70:
        print('A')
    case marks if marks>60:
        print('FAIL')
