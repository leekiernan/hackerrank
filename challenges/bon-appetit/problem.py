from functools import reduce

def getCharge(n,k,costs,charge):
	skipped = costs.pop(k)
	total = int(reduce(lambda x,y: x+y, costs) / 2)
	if total == charge:
		return "Bon Appetit"
	else:
		return charge - total


n, k = list(map(int, input().split(' ')))
costs = list(map(int, input().strip().split(' ')))
charge = int(input())
print(getCharge(n,k,costs,charge))
