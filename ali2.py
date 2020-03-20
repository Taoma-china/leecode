import numpy as np
def longest(arr):
	new_arr =[]

	
	for i in range(len(arr)):
		result = True
		for j in range(1,len(arr[i])):
			if ord(arr[i][j])<ord(arr[i][j-1]):
				result = False
				break
		if re == True:
			new_arr.append(arr[i])
	new_arr.sort()
	opt = np.zeros(len(new_arr))
	
	opt[0]= len(new_arr[0])

	for i in range(1,len(new_arr)):
		x = org(new_arr[i][0])
		length = len(new_arr[i])
		for j in range(i):
			y = org(new_arr[j][-1])
			if x >= y:
				length = max(opt[j]+len(new_arr[i]),length)
		opt[i] = length
	return opt[len(new_arr)-1]
arr = [[a,a,a],[b,c,d],[b,c,d,e,f],[z,z,z]]
print(longest(arr))