# FastGit Setup

This guide will help you set up a `fastgit` alias that allows you to quickly add, commit, and push changes to your git repository using a single command.

## What happen in Setup

1. **Create Alias and Source Bash Configuration**
   ```cd Git_Commands_shorter```
   should stand into repo (Git_Commands_shorter)

   ```sh
   python3 -u create_alias.py
   ```

   Run the past command to create the alias and add it to your `~/.bashrc`
2. **Source Bash Configuration**

   After running the Python script, source your `~/.bashrc` to apply the changes to your current session:

   ```sh
   source ~/.bashrc
   ```

## Usage

Once the alias is set up and sourced, you can use the `fastgit` command to add, commit, and push changes to your repository. Replace `"Your commit message"` with your actual commit message.

```sh
fastgit "Your commit message"
```

## Example

```sh
root@linux:/Git_Commands_shorter# python3 -u create_alias.py 
Alias created successfully.

root@linux:/Git_Commands_shorter# source ~/.bashrc
root@linux:/Git_Commands_shorter# alias 
alias egrep='egrep --color=auto'
alias fastgit='python3 -u /Git_Commands_shorter/gitacp.py'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'
alias l='ls -CF'
alias la='ls -A'
alias ll='ls -alF'
alias ls='ls --color=auto'     
root@linux:/Git_Commands_shorter# fastgit "first commit"

[master (root-commit) repo] first commit
 3 files changed, 49 insertions(+)
 create mode 100644 README.md
 create mode 100755 create_alias.py
 create mode 100755 gitacp.py


Done Push!
```

## Description

- `python3 -u create_alias.py`: This command runs the Python script that adds the alias to your `~/.bashrc`.
- `source ~/.bashrc`: This command applies the changes to your current shell session.
- `fastgit "first commit"`: This command stages all changes, commits them with the message "first commit", and pushes them to the master branch.

Enjoy using `fastgit` for quick and easy git operations!
