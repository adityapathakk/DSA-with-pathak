# problem link: https://www.codechef.com/problems/GMGM?tab=statement

t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    li = list(map(int, input().split()))
        
    switchCount, gunSwitch = 0, 0 # 0 for close-range gun, 1 for long-range gun
    
    for i in li:
        if i > d and gunSwitch == 0: # need to switch from close-range to long-range
            switchCount += 1
            gunSwitch = 1
        elif i <= d and gunSwitch == 1: # need to switch from long-range to close-range
            switchCount += 1
            gunSwitch = 0
    
    print(switchCount)