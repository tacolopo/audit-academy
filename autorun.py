import os
from pathlib import Path
import time

password = ''
length = 0
number = 0
file = open('<text file of memos>')

for line in file:
	goose = len(line.split())
	length = length + 1
	if goose == 12:
		if line.startswith('relayed'):
			continue
		elif line.startswith('Relayed'):
			continue
		else:
			mnemonic = line
			os.system(f'''
				curl -OL https://golang.org/dl/go1.17.4.linux-amd64.tar.gz;
				echo {password} | sudo -S tar -C /usr/local -xvf go1.17.4.linux-amd64.tar.gz;
				export PATH=$PATH:/usr/local/go/bin;
				gaiad config node <rpc>;
				export PATH=$PATH:$(go env GOPATH)/bin && echo {password} | gaiad keys add {number} --recover;
				{mnemonic};
				gaiad tx bank send {number} <white hat address> uatom --fees uatom -y;
				''')
			number = number + 1
	elif goose == 24:
		mnemonic = line
		os.system(f'''
			curl -OL https://golang.org/dl/go1.17.4.linux-amd64.tar.gz;
			echo {password} | sudo -S tar -C /usr/local -xvf go1.17.4.linux-amd64.tar.gz;
			export PATH=$PATH:/usr/local/go/bin;
			gaiad config node <rpc>;
			export PATH=$PATH:$(go env GOPATH)/bin && echo {password} | gaiad keys add {number} --recover;
			{mnemonic};
			gaiad tx bank send {number} <white hat address> uatom --fees uatom -y;
			''')
\		number = number + 1





#Execute command to open session
# os.system('cmd /k "curl -OL https://golang.org/dl/go1.17.4.linux-amd64.tar.gz & sudo tar -C /usr/local -xvf go1.17.4.linux-amd64.tar.gz export PATH=$PATH:/usr/local/go/bin & export PATH=$PATH:$(go env GOPATH)/bin"')
# file = open('1.txt')
# for line in file:
#iterate through each line in file and import them into successive commands
	# os.system('cmd /k "gaiad keys add #iterating_number --recover & #each_line_in_file"')
