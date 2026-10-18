# Problem 19: Company Logo
# https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter

s = input()
counts = Counter(s)

for character, count in sorted(
    counts.items(),
    key=lambda item: (-item[1], item[0])
)[:3]:
    print(character, count)