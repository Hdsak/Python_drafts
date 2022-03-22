#Task 2
s1=input()
s2=input()
s3=input()
g=''
if s1=='<' and s2=='<':
    if s3=='>':
        t='acb'
    else:
        t='abc'
elif s1=='>' and s2=='>':
    if s3=='>':
        t='cba'
    else:
        t='bca'
elif s1=='<' and s2=='>':
    t='cab'
elif s1=='>' and s2=='<':
    t='bac'
elif s1=='=':
    if s2=='>':
        t='cba'
        g = 'cab'
    else:
        t='abc'
if g:
    print(g)
    print(t)
else:
    print(t)