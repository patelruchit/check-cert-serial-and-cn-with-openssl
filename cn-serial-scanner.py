import subprocess

# Store all entries, including duplicates, as a list of tuples
entries = []

# Reading the input file 
with open('input.txt', 'r', encoding='utf-8') as inputfile:
    for line in inputfile:
        hostname, port = line.strip().split(':')
        entries.append((hostname, port))

# Cycle through the list and use OpenSSL for each host:port combination
for hostname, port in entries:
    # Send 3 pings to the hostname
    ping_command = ['ping', '-c', '3', hostname]
    ping_result = subprocess.run(ping_command, capture_output=True, text=True)
    if ping_result.returncode == 0:
        # If the ping is successful, proceed with OpenSSL
        command = f"openssl s_client -connect {hostname}:{port} </dev/null 2>&1 | openssl x509 -noout -serial -subject"
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        output = result.stdout
        print('For the Hostname:', hostname, 'Port:', port)
        print('The Serial and CN are \n:', output)
    else:
        print(f"Ping failed for {hostname}. Skipping OpenSSL check.")
