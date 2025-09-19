#!/usr/bin/env python3

import subprocess
import sys
import shutil

ping_command = shutil.which("ping")
if ping_command is None:
    print("Ping command not found")
    sys.exit(1)

host = sys.argv[1]
timeout = 5  # Timeout in seconds

try:
    result = subprocess.run([ping_command, "-c", "1", host], stdout=subprocess.DEVNULL, timeout=timeout)
    if result.returncode == 0:
        print("Host alive: {}".format(host))
    else:
        print("Host not reachable: {}".format(host))
except subprocess.TimeoutExpired:
    print("Host not reachable: {}".format(host))
