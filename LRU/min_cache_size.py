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

def main():
	req = ['item1', 'item2', 'item3', 'item1', 'item2']
	k = 1

	print(get_min_size(req, k))

if __name__ == "__main__":
	main()