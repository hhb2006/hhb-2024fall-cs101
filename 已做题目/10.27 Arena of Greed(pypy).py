def take(coins):
    if coins%2 == 1 :       # odd
        return 1
    else:                   # even
        if ((coins-2)//2)%2 == 1 and (coins-2)//2 != 1:
            return 1
        else:
            return coins//2

t = int(input())
for _ in range(t):
  n = int(input())
  turn,res = 1,0
  while n > 0:
      taken = take(n)
      if turn%2 == 1:      # my turn
          res += taken
      n -= taken
      turn += 1
  print(res)