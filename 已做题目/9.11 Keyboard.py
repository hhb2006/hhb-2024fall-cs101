s='qwertyuiopasdfghjkl;zxcvbnm,./'
direc=input()
if direc=='R':
    move=-1
elif direc=='L':
    move=1
f_writing=input()
t_writing=''
for i in f_writing:
    n=s.index(i)
    t_writing+=s[n+move]
print(t_writing)





