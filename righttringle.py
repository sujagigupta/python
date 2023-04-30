s1=int(input('a'))
s2=int(input('b'))
s3=int(input('c'))
m=max(s1,s2,s3)
if (m)**2==s1**2+s2**2+s3**2-(m)**2:
    print('it is right angle tringle')
else:
    print('it is not a right angle tringle')
