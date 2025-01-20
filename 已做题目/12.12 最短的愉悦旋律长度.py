n,m = map(int,input().split())
melody = list(map(int,input().split()))
notes = set()
cnt = 1

for i in range(n):
    notes.add(melody[i])
    if len(notes) == m:
        cnt += 1
        notes.clear()
print(cnt)
