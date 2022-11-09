#PS5 - A - Running Race

#function to convert the time into seconds
def convert_sec(time):
    t_in_sec = 0
    str_time = str(time)
    mm,ss = map(int, str_time.split('.'))
    t_in_sec = (60*mm)+ss
    return t_in_sec

# Main Function
runner_time = {}
runner_laps = {}
l,k,s = map(int, input().split())
for i in range(l):
    key, time = map(str, input().split())
    key = int(key)
    
    sec = convert_sec(time)
    runner_time[key] = runner_time.get(key, 0) + sec
    runner_laps[key] = runner_laps.get(key, 0) + 1
    

runners = [(V1,K1) for K1,V1 in runner_time.items() if runner_laps[K1] == k]
runners.sort()

for r in runners:
  print(int(r[1]))
