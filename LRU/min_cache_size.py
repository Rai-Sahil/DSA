def get_min_size(requests, k):
	dict = {}

	for i in range(len(requests)):
		if requests[i] in dict:
			dict[requests[i]].append(i)
		else:
			dict[requests[i]] = [i]

	final = []

	for key, val in dict.items():
		for i in val:
			if i - min(val) >0:
				final.append(i - min(val))

	final.sort()

	return final[k-1]

def get_min_size2(requests, k):
	if k == 0:
		return 0

	distinct_request = set()
	min_sizes = []

	for req in requests:
		distinct_request.add(req)
		if len(distinct_request) >= k:
			min_sizes.append(len(distinct_request))
			break

	return min_sizes[-1] if min_sizes else -1

def main():
	req = ['item1', 'item2', 'item3', 'item1', 'item2']
	k = 1

	print(get_min_size2(req, k))

if __name__ == "__main__":
	main()