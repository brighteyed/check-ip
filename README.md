# IP Range Checker

Check if your public IP is within specified IP ranges. Supports command-line options and `pipx` for easy installation.

---

## Features

- Check if your IP is in a list of IP ranges.
- Optional IP display (`--show-ip`).
- Exit codes: `0` (covered) or `1` (not covered/error).

---

## Installation

1. Install `pipx` (if not already installed):
   ```bash
   python -m pip install --user pipx
   python -m pipx ensurepath
   ```

2. Install the script:
   ```bash
   pipx install .
   ```

---

## Usage

1. Run the script:
   ```bash
   check_ip
   ```

2. Options:
   - Specify IP ranges file: `-f ip_ranges.txt`
   - Show IP and status: `--show-ip`

Example:
```bash
check_ip --show-ip
```
Output:
```
Current IP: 89.109.225.10 - Status: Covered
```

---

## IP Ranges File

Add IP ranges in CIDR notation (one per line):
```
213.239.192.0/18
2.16.0.0/13
```
