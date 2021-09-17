#me
'''
문제를
각 좌표의 숫자는 왼쪽과 위 중에 작은 값을 택해 자신을 더하는 걸로 바꾼다,
(여기까지 왔을때 최소 에너지의 합 두개중 더 작은 것을 선택하면 그게 최선)
문제를 각 "대각선"을 마지막으로 하는 것으로 축소시킨다.
'''


#answer
'''
최단거리 이동이기때문에 꼭 n번만에가야한다.

도착점을 기준으로 보자.
도착점을 기준으로 보면 위에서오나 왼쪽에서온다.

nxn dy배열을 만든다.
dy[i][j] == 출발좌표 부터 i,j까지 가는데 드는 최소비용.
출발점인 (0.0)을 도착점으로 볼때의 dy[0][0]는 3이다.
dy[0][1] => 출발좌표부터 0,1까지 가는데 드는 최소비용: 자기 왼쪽인 3 + 자기자신 3 = 6
dy[0][2] => 자기 왼쪽인 6 + 자기자신 5 =11
.
.
.
열쪽 가장자리는 왼쪽부터 오른쪽으로만 누적되어 갈 수 있다.
행의 가장자리는 위에서부터 아래로만 누적되어 내려올 수있다.
=> 가장자리를 먼저 세팅한다!!

이제부터 가장자리가 아니므로 왼쪽이나 위중에 하나중에서 온다.
이제부터 실제 for문을 돌면서 dynamic programming을 한다.
dy[1][1]은 dy[0][1] 과 dy[1][0]중 작은 값(지금까지 누적되온 최소비용)을 택해 자신을 더한다.
'''


import sys
#sys.stdin = open("input.txt","r")

n = int(input())
arr = [ list(map(int,input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)]
dy[0][0] = arr[0][0]

#가장자리 세팅
for i in range(n):
    dy[0][i]= dy[0][i-1] + arr[0][i] #열
    dy[i][0] = dy[i-1][0] + arr[i][0] #행

#이제 실제 dp
for i in range(1,n):
    for j in range(1,n):
        dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + arr[i][j]

print(dy[n-1][n-1]) #도착지점
    
