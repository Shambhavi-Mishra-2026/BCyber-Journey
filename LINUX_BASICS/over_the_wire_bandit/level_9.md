>ssh bandit9@bandit.labs.overthewire.org -p 2220

bandit9@bandit:~$ ls
data.txt
bandit9@bandit:~$ strings data.txt | grep "===="
/========== the
========== password
========== is
========== FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
bandit9@bandit:~$

# strings brings out human readable scripts and grep finds lines with === from it
