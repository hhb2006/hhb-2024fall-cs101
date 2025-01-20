Haab = list(map(str,'pop、no、zip、zotz、tzec、xul、yoxkin、mol、chen、yax、zac、ceh、mac、kankin、muan、pax、koyab、cumhu、uayet'.split('、')))
Tzolkin = list(map(str,'imix、ik、akbal、kan、chicchan、cimi、manik、lamat、muluk、ok、chuen、eb、ben、ix、mem、cib、caban、eznab、canac、ahau'.split('、')))
n = int(input())
print(n)
for _ in range(n):
    s = input()
    index = s.find('.')
    hd = int(s[:index])
    hm,hy = s[index+1:].split()
    days = hd + 1 + Haab.index(hm)*20 + (int(hy))*365
    #print(days,end = ', ')
    ty = days//260 - (days%260 == 0)
    days = (days-1) % 260 + 1
    td = (days-1) % 13 + 1
    tm = Tzolkin[(days-1)%20]
    print(td,tm,ty)
