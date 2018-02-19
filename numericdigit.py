s=raw_input()
m=len(s)
count=0
for i in range(0,m):
 if(s[i]>='0' and s[i]<='9'):
  count+=1
print(count) 
