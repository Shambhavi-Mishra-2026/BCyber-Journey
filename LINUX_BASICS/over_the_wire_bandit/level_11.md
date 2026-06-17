 >ssh bandit11@bandit.labs.overthewire.org -p 2220

bandit11@bandit:~$ ls
data.txt
bandit11@bandit:~$ cat data.txt
Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4
bandit11@bandit:~$ cat data.txt | tr "A-Za-z" "N-ZA-Mn-za-m"
The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
bandit11@bandit:~$ exit

# ROT13 cypher could be decoded by translate command


### SYNTAX OF tr - tr "old trend" "new trend"


# The Alphabet is Linear, Not a LoopComputers do not automatically know that the alphabet loops around from Z back to A. To a computer, letters are just numbers in a straight line:text[A B C ... M N O ... Z] Use code with caution.Because it is a straight line, you cannot bridge the gap from Z to A with a single dash. You have to explicitly define both pieces of the broken line:N-Z: Grab the second half of the alphabet.A-M: Grab the first half of the alphabet and stick it to the end.If you tried to write N-M, the command would break. By writing N-ZA-M, you manually create the loop for the computer.