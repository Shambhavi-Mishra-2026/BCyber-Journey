
>ssh bandit6@bandit.labs.overthewire.org -p 2220

bandit6@bandit:~$ ls
bandit6@bandit:~$ find / -type f -user bandit7 -group bandit6 -size 33c
find: ‘/etc/polkit-1/rules.d’: Permission denied
find: ‘/etc/xinetd.d’: Permission denied
/var/lib/dpkg/info/bandit7.password
find: ‘/var/lib/amazon’: Permission denied
find: ‘/var/lib/apt/lists/partial’: Permission denied
bandit6@bandit:~$ find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
bandit6@bandit:~$ exit

# 2 - all the error messages
# /dev/null is a blackhole like folder that eats up anything inserted into it
# we use 2>/dev/null to remove all the error messages from the terminal and get clean password