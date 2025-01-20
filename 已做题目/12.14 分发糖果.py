n = int(input())
ratings = list(map(int,input().split()))
candies = [1 for _ in range(n)]
for i in range(1,n):
    if ratings[i] > ratings[i-1]:
        candies[i] = max(candies[i-1]+1,candies[i])
for i in range(-1,-n,-1):
    if ratings[i-1] > ratings[i]:
        candies[i-1] = max(candies[i]+1,candies[i-1])
print(sum(candies))