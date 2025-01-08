p = int(input())
c = int(input())
ans = 50 * p - c * 10
if p > c:
    ans += 500
print(ans)