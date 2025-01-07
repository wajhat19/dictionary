lst=[10,10,20]
#
#for x in lst:
#    print(lst,'-->',lst.count(x))
a=[10,10,20,]
for x in set(a):
    print(x,'-->',a.count(x))
print([a.count(x) for x in set(a)])    