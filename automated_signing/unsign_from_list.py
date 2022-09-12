# this file removes the audited attribute of any akash address you enter into the 
# python list "lst"

import os

lst = [
'akash_address_1',
'akash_address_2',
'akash_address_3',
'akash_address_4',
]
account_name = input('Please enter your local auditor account name: ')

for item in lst:
	os.system(f'''
	AKASH_NET="https://raw.githubusercontent.com/ovrclk/net/master/mainnet";
	AKASH_VERSION="$(curl -s "$AKASH_NET/version.txt")";
	export AKASH_CHAIN_ID="$(curl -s "$AKASH_NET/chain-id.txt")";
	export AKASH_NODE="$(curl -s "$AKASH_NET/rpc-nodes.txt" | shuf -n 1)";
	akash tx audit attr delete {item} --from {account_name} --fees 5000uakt -y;
''')
