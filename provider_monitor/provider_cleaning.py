# format provider_list.txt to print the host and owner address
# python3 provider_cleaning.py >> cleaned_list.txt

file = open('provider_list.txt')
items = []
count = 0

for line in file:
	if 'host_uri' in line:
		line = line.replace('  host_uri: ', '').strip()
		items.append(line)
	if 'owner' in line:
		line = line.replace('  owner: ', '').strip()
		items.append(line)
		count = count + 1

print(count)

for item in items:
	print(f'{item}\n')
