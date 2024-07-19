import subprocess
import sys
import os


def code_subfuntion_run(line):
    """subprocess function"""
    result = subprocess.run(line, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing: {line}")
        print(result.stderr)
        exit(1)
    return result


if __name__ == '__main__':
    alias_command, line = "", sys.argv[1]
    if len(sys.argv) == 2:
        if line.startswith('./'):
            line = sys.argv[1][2:]
        alias_command = f'alias quickpush=\'python3 -u "{os.getcwd()}/{line}"\''
    else:
        alias_command = f'alias quickpush=\'python3 -u "{os.getcwd()}/gitacp.py"\''
    command = f'echo "{alias_command}" >> ~/.bashrc'
    result = code_subfuntion_run(command)
    print("Alias created successfully.")
    print(result.stdout)
