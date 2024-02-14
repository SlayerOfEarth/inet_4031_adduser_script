## Python User Creation Script

## Description Section

This Python script `create-users.py` is designed to read input from stdin, parse the input, and create user accounts based on the provided information. It utilizes regular expressions and system commands to handle user creation tasks. The script is intended to be run with elevated privileges (sudo) due to its operations on system files like `/etc/passwd` and `/etc/group`.

## Operation Section

The Script operates as follows:

1. It reads input from stdin, typically provided via a file or piped input.
2. For each line of input, it checks if the line starts with a `#` character, indicating a comment line, and skips such lines.
3. It splits each non-comment line into fields using the `:` delimiter.
4. If a line doesn't have exactly 5 fields or starts with `#`, it skips processing that line.
5. It extracts the username, password, gecos (comment), and groups from the line.
6. It creates a user account using the `adduser` command with appropriate options and parameters.
7. It sets the user's password using the `passwd` command.
8. It assigns the user to specified groups using the `adduser` command.

The script should be executed with elevated privileges using `sudo` to ensure it has the necessary permissions to perform user management operations on the system files.
