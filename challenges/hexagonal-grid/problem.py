no_test_cases = int(input())

for test in range(no_test_cases):
	grid_length = int(input())
	# grid_length = int(input()) * 2
	r1 = list(input())
	r2 = list(input())
	rows = [r1, r2]
	grid = [item for sublist in rows for item in sublist]

	if grid.count('1') % 2 == 1:
		print('NO')
		continue

	if grid.count('1') == 0:
		print('YES')
		continue

	w1 = 0
	w2 = 0
	while w1 < grid_length and w2 < grid_length:
		print("{0}-{1}".format(r1[w1], r2[w2]))
		if r1[w1] == r2[w2]:
			w1 += 1
			w2 += 1
			continue

