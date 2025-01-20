s=input()
chat='NO'
for i in range(len(s)):
    if s[i]=='h':
        for j in range(i+1,len(s)):
            if s[j]=='e':
                for k in range(j+1,len(s)):
                    if s[k]=='l':
                        for l in range(k+1,len(s)):
                            if s[l]=='l':
                                for m in range(l+1,len(s)):
                                    if s[m]=='o':
                                        chat='YES'
print(chat)