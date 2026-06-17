# Text vs Data
# Data couldn't be read by humans only text. "file <filename>" identifies the type of data on a file

>ssh bandit4@bandit.labs.overthewire.org -p 2220

bandit4@bandit:~$ ls
inhere
bandit4@bandit:~$ cd inhere
bandit4@bandit:~/inhere$ ls
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
bandit4@bandit:~/inhere$ file -file00
file: Cannot open `ile00' (No such file or directory)
bandit4@bandit:~/inhere$ file ./*
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: Non-ISO extended-ASCII text
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
bandit4@bandit:~/inhere$  cd ./"-file07"
-bash: cd: ./-file07: Not a directory
bandit4@bandit:~/inhere$ cat ./"-file07"
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

# Non-ISO extended-ASCII text means the file contains normal text mixed with weird formatting characters, system line breaks, or special symbols (like mathematical signs or currency symbols). It is not completely corrupted binary data, but it is not pure, clean human-readable text either.

# Tedious to scan files one b one so special character (*) is used after file command as it indicates to scan all files in the directory

### ./ before * because all filenames have special character