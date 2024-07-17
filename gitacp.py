import subprocess
from os.path import exists
from sys import argv


def git_linux(commit_message):
    """window git command function"""
    commit_files = []
    commit_groups = []
    current_message  = []

    for i in commit_message:
        if exists(i):
            if commit_files and current_message:
                commit_groups.append([' '.join(commit_files), ' '.join(current_message)])
                commit_files = []
                current_message = []
            commit_files.append(i)
        else:
            current_message.append(i)

    if commit_files or current_message:
        commit_files = commit_files if commit_files else ['.']
        commit_groups.append([' '.join(commit_files), ' '.join(current_message)])

    for files, message in commit_groups:
        commands = [
            f'git add {files}',
            f'git commit -m "{message}"',
            'git push origin master'
        ]

        print("Adding files:")
        for file_name in files.split(' '):
            print(f"\t{file_name}")
        print(f"\nCommit message: {message}")

        for command in commands:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Error executing: {command}")
                print(result.stderr)
                return
            print(result.stdout)
        print('-------------------------------------\n')
    return 'Done Push!'


if __name__ == '__main__':
    if len(argv) < 2:
        print("Usage: python script.py <commit_message>")
        exit(1)

    commit_text = argv[1:]
    print(git_linux(commit_text))
