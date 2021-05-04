#그리디
#모험가 길드

n = int(input())
person = list(map(int, input().split()))
person.sort()

count = sum = 0;

for p in person:
  sum += 1;
  if sum == p:
    count += 1 
    sum = 0

print(count)