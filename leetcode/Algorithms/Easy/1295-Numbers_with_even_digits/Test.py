# read the string filename filename = input()
from collections import Counter

filename = input()
f = open(filename,'r')
hosts = [line.split()[0] for line in f.readlines()]
host_counter = Counter(hosts)
#op_file = f"records_{filename}"
with open(f'records_{filename}', 'w') as output_file:
    for key in sorted(host_counter):
        output_file.write(f'{key} {host_counter[key]}\n')
