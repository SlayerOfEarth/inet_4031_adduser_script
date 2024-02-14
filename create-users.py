#!/usr/bin/env python3
import os
import re
import sys

def main():
    for line in sys.stdin:
        # Using regular expression to check for lines starting with a #
        match = re.match(r'^\s*#', line)
        fields = line.strip().split(':')  # Strip whitespace and split into an array

        # Check if the line starts with # or doesn't have 5 fields
        if match or len(fields) != 5:
            continue  # Skip the line if it starts with # or doesn't have 5 fields

        # Extracting fields from the line
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')  # Splitting groups separated by comma

        print("==> Creating account for %s..." % username)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        os.system(cmd)  # Execute the command to create the user account
        print("==> Setting the password for %s..." % username)
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        os.system(cmd)  # Execute the command to set the password

        # Looping through groups and adding user to each group
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                os.system(cmd)  # Execute the command to add user to the group

if __name__ == '__main__':
    main()
