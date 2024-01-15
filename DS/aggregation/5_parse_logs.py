# Python 2/3

log_content = """192.168.2.20    [01/01/2020:10:10:10 -0300] "GET /foo/bar"     200     1234          2370
192.168.2.21    [01/01/2020:10:14:31 -0300] "GET /bar"         404     393           32
100.2.238.80    [01/01/2020:10:14:30 -0300] "GET /bar"         404     393           32
192.168.2.20    [01/01/2020:10:11:10 -0300] "GET /foo"         200     6000          1200
192.168.2.20    [01/01/2020:10:12:10 -0300] "GET /foo/bar/baz" 200     9999          1432
100.2.238.80    [01/01/2020:10:12:40 -0300] "GET /foo?q=baz"   400     393           32
100.2.238.80    [01/01/2020:10:13:10 -0300] "GET /foo/bar"     200     1234          300
62.8.38.27      [01/01/2020:10:14:10 -0300] "GET /foo/bar"     200     1234          400
62.8.38.27      [01/01/2020:10:14:20 -0300] "GET /foo/bar"     200     1234          420
62.8.38.27      [01/01/2020:10:14:30 -0300] "GET /foo/bar"     200     1234          423
192.168.2.20    [01/01/2020:10:14:30 -0300] "GET /bar"         404     393           32"""

# Read the file at /home/coderpad/data/input1.txt and answer the following questions:
#     Get the top 3 client IPs.
#     Get average page size.
#     Get the error rate (non 2xx codes) / all requests.

def parse_logs(log_content):
    logs =  log_content.split("\n")
    ips = []
    counter = 0
    page_sizes = []
    error_count = 0
    for log in logs:
        page_sizes.append(int(log.split()[6]))
        if counter < 3:
            ips.append(log.split()[0])
        counter += 1
        if int(log.split()[5]) != 200:
            error_count += 1
        error_rate = error_count/counter
    print ("top 3 ips:", ips)
    print ("page size:", sum(page_sizes)/counter)
    print ("error_rate:", error_rate)
    return " "
    # return "top 3 ips:", ips, "\n","page size:", sum(page_sizes)/counter,"\n","error_rate:", error_rate

print (parse_logs(log_content))

"""
To parse log lines from file: 

# Read log file and extract IPs
log_file_path = 'input.txt'
with open(log_file_path, 'r') as file:
    log_entries = file.readlines()

# Function to parse IP addresses from log entries
def extract_ips(log_entry):
    ip_pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')
    match = ip_pattern.search(log_entry)
    if match:
        return match.group()
    else:
        return None
"""