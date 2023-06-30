#Where is my internet - Nov Demos

islands, bridges = map(int, input().split())



connected_dict = {}
connected_dict['Connected'] = list(map(int, input().split()))





for i in range(bridges-1):
	
	i_1, i_2 = map(int, input().split())

	if i_1 in connected_dict['Connected'] or i_2 in connected_dict['Connected']:
		
		connected_dict['Connected'] = connected_dict['Connected'] + [i_1, i_2]

	else:
		connected_dict['Disconnected'] = [i_1, i_2]



if len(connected_dict) == 1:
        print("YES")
elif len(connected_dict) == 2:
        print("NO")

#print(connected_dict)
