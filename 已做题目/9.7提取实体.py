tcount=0
fcount=0
count=input()
for x in range(int(count)):
    s=input()
    s+='  '
    for i in range(len(s)-3):
        if s[i]=='#'and s[i+1]=='#' and s[i+2]=='#'and s[i+3]==' 'and s[i+4]=='#'and s[i+5]=='#' and s[i+6]=='#':
            fcount+=1
        if s[i]=='#'and s[i+1]=='#' and s[i+2]=='#':
            tcount+=1
print(int(tcount/2-fcount))
'''
###Shelley### ###Berkley### , a Democratic representative of Nevada
Mrs. ###Babbitt### 's daughter lives in ###Las### ###Vegas### testified about the case in July at a Congressional hearing into the recovery of art stolen during World War II .
'''