l = ['apple','red','apple','red','red','pear']
dic = {}
for i in l:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
#print (dic)
# sort by key
#for i in sorted(dic.keys()):
    #print (i, dic[i])
# sort by value
sort_value = sorted(dic.items(), key= lambda kv: (kv[1], kv[0]), reverse=True)

print ("sort by value: ",sorted(dic.items(), key= lambda x: x[1], reverse=True))
# sort by key
print ("sort by key: ",sorted(dic.items(), key= lambda kv: (kv[0], kv[1]), reverse=True))

print (dict(sort_value))
# https://favtutor.com/blogs/python-sort-dictionary