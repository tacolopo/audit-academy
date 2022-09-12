# this file creates an audited attribute on any akash address you enter into the 
import os
# Change items in list to provider addresses you wish to sign
lst = [
'akash1wxr49evm8hddnx9ujsdtd86gk46s7ejnccqfmy',
'akash19yyxp7la8pklaft3s0s2err85t8tyzlwqca0v3',
'akash1q7spv2cw06yszgfp4f9ed59lkka6ytn8g4tkjf',
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
