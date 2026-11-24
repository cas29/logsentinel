import re
from collections import Counter

FAILED_LOGIN = re.compile(
    r"Failed password for (?:invalid user )?(\S+) from (\d+\.\d+\.\d+\.\d+)"
)


def read_lines(path):
    with open (path, encoding='utf-8') as f:
        return f.readlines()


def count_failed_logins(lines):
    """Return a Counter: IP address -> number of failed logins."""
    attemps = Counter()

    for line in lines:
        match = FAILED_LOGIN.search(line)
        if match:
            ip = match.group(2)
            attemps[ip] +=1
    return attemps

if __name__ == "__main__":
    lines = read_lines("samples/auth.log")
    for ip, count in count_failed_logins(lines).most_common():
        print(f"{ip}: {count} failed logins")
    

