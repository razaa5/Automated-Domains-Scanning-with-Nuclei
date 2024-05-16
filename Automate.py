
#!/usr/bin/env python3

import subprocess

# Read domains from the file
with open("domains.txt", "r") as file:
    domains = file.readlines()

# Process each domain
for domain in domains:
    # Remove leading and trailing whitespaces
    domain = domain.strip()
    
    # Extract domain name from URL
    domain_name = domain.split("://")[1].split("/")[0]
    
    # Run nuclei command and redirect output to result file
    subprocess.run(f"nuclei -u {domain} > result_{domain_name}.txt", shell=True)
