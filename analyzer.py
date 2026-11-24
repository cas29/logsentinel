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

def detect_bruteforce(attempts, threshold = 3):
    """Return only the IPs with at least `threshold` failed logins."""
    return {ip: count for ip, count in attempts.items() if count >= threshold}

if __name__ == "__main__":
    lines = read_lines("samples/auth.log")
    attempts = count_failed_logins(lines)
    suspects = detect_bruteforce(attempts, threshold=3)

    if not suspects:
        print('No brute-force attacks detected.')

    for ip, count in sorted(suspects.items(), key=lambda x : -x[1]):
        print(f'[ALERT] Possible brute force from {ip}: {count} failed logins')
    

