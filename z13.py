def get_list(file,n):
    f = open(file, 'r')
    lst=[]
    for i in range(n):
         tmp=f.readline()
         lst.append(int(tmp[0:50]))
    return lst
lst=get_list('test.txt',100)
print(str(sum(lst))[0:10])