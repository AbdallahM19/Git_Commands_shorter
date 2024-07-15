import subprocess
from sys import argv


def git_linux(commit_message):
    """window git command function"""
    commands = [
        'git add .',
        f'git commit -m "{commit_message}"',
        'git push origin master'
    ]

    for command in commands:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error executing: {command}")
            print(result.stderr)
            return
        print(result.stdout)
    return 'Done Push!'


if __name__ == '__main__':
    if len(argv) < 2:
        print("Usage: python script.py <commit_message>")
        exit(1)

    commit_text = " ".join(argv[1:])
    print(git_linux(commit_text))
