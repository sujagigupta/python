#input section
m=int(input('enter the marks'))
g='o' if m>90 else 'A+' if m>80 else 'A' if m>70 else 'B+' if m>60 else 'B' if m>50 else 'C' if m>40 else 'Fail'
print(g)
