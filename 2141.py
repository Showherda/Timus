import sys
LI=lambda:list(map(int, sys.stdin.readline().split()))
MI=lambda:map(int, sys.stdin.readline().split())
SI=lambda:sys.stdin.readline().strip('\n')
II=lambda:int(sys.stdin.readline())
# sys.stdin=open('input.txt')
# sys.stdout=open('output.txt', 'w')
n, a=II(), LI()
dp=[[-int(1e10) for i in range(2)] for j in range(n)]
dp[0][0]=a[0]
ans=max(0, a[0])
for i in range(1, n):
	dp[i][0]=max(dp[i-1][1]+a[i], a[i])
	dp[i][1]=dp[i-1][0]-a[i]
	ans=max(ans, *dp[i])
print(ans)
