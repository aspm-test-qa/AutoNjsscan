"""
INTENTIONALLY VULNERABLE FILE
For NJS SAST scanner testing only
DO NOT use in production
"""

import subprocess
import os

# -----------------------------
# Vulnerability 1: Hardcoded Secret
# -----------------------------
DB_PASSWORD = "P@ssw0rd123!"   # NJS SAST should flag hardcoded credential
API_TOKEN = "njs_secret_token_abcdef"

# -----------------------------
# Vulnerability 2: Command Injection
# -----------------------------
def run_system_command(user_input):
    """
    Vulnerable: user input is directly concatenated
    into a shell command.
    """
    command = "ls " + user_input
    result = subprocess.check_output(
        command,
        shell=True,          # critical flag for command injection
        stderr=subprocess.STDOUT
    )
    return result.decode()

# -----------------------------
# Entry Point
# -----------------------------
if __name__ == "__main__":
    print("Running vulnerable command...")
    user_supplied_value = input("Enter directory name: ")
    output = run_system_command(user_supplied_value)
    print(output)
