>ssh bandit8@bandit.labs.overthewire.org -p 2220

bandit8@bandit:~$ ls
data.txt
bandit8@bandit:~$ head -5 data.txt
P4PKvK5XYDD5Rtg44yy5hwkZm5oJHE3W
zMAwnir1RY4L0JHxe0HLSpaCQhLpdqp8
7x4B105wBEXpUrPqChVZO1o25zewgI1w
A0SeUqvFQZ36a8N4gLRYOAzvc74YAJ0S
LnHI7KumLifj05nwgdwIhGwTe80m4OGb
bandit8@bandit:~$ sort data.txt | uniq -c | sort
     10 1rC0NfoStvu5rpiu1ALxu8JvsEJZWCfh
     10 216ESs2cx3kpTs2fuH6Nv71w0uLlWbkn
     10 24tByG8lOiM5PGjJK7LwVlv9cyVERENt
     10 29T7qkB9abfmsEHTx9DIwBTBT39zMWch
     10 2SeGLxPtX0O00ZaaEG5Bi1mI3ZGrDSLx
     10 30LozUTwjRpN1B8cgz2K4lw172HWSCEf
     10 3AyAYXi6VH0vSxANxT9YE84usXlQrmap
     10 3PQWwHXXgUZQkbxExY2QIVGDEoB7iEda
      1 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
 bandit8@bandit:~$ exit


 # logic - through command piping sort data.txt alphanumerically then in output no of each repeated line is counted  through uniq -c whose output when sorted gives the only once occuring line at the bottom
 