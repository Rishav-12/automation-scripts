import sys
import subprocess

servers = sys.argv[1:]
print(servers)

for server in servers:
    print(server)
    output = subprocess.run(["ping", "-n", "2", "-w", "2", server], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Return Code: {output.returncode}")
    if output.returncode == 0:
        print(f"{server} is up")
    else:
        print(f"{server} is down")
