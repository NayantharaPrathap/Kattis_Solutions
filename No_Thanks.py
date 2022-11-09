#no thanks problem
'''
inp = int(input())
cards = list(map(int, input().split()))
cards.sort()
sum1 = 0
for n in range(inp-1):
    if cards[n]+1 != cards[n+1]:
        sum1 += cards[n+1]
print(sum1)
'''
#final code

inp = input()
cards = sorted(map(int, input().split()))
prev, curr = None, None
sum = 0
while cards:
    prev, curr = curr, cards.pop()
    if prev is not None and curr == prev - 1:
        sum -= prev
    sum += curr
print(sum)
