

ShambhaviMishra-academy@webshell:~$ git clone ssh://git@foggy-cliff.picoctf.net:51594/git/challenge.git
Cloning into 'challenge'...
The authenticity of host '[foggy-cliff.picoctf.net]:51594 (:51594)' can't be established.
ED25519 key fingerprint is SHA256:Grm7IvZgdCDbXv3DtQ70/6WKHA2q3XhT+sfva8nLT38.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[foggy-cliff.picoctf.net]:51594' (ED25519) to the list of known hosts.
git@foggy-cliff.picoctf.net's password: 
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (3/3), done.
ShambhaviMishra-academy@webshell:~$ cd challenge
ShambhaviMishra-academy@webshell:~/challenge$ 
ShambhaviMishra-academy@webshell:~/challenge$ ls
README.md
ShambhaviMishra-academy@webshell:~/challenge$ cat README.md
MyGit
If you want the flag, make sure to push the flag! 
Only flag.txt pushed by `root:root@picoctf` will be updated with the flag. 
GOOD LUCK!

ShambhaviMishra-academy@webshell:~/challenge$ git config user.name "root"
ShambhaviMishra-academy@webshell:~/challenge$ git config user.email "root@picoctf"
ShambhaviMishra-academy@webshell:~/challenge$ git config --list
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
remote.origin.url=ssh://git@foggy-cliff.picoctf.net:51594/git/challenge.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.master.remote=origin
branch.master.merge=refs/heads/master
user.name=root
user.email=root@picoctf

ShambhaviMishra-academy@webshell:~/challenge$ touch flag.txt
ShambhaviMishra-academy@webshell:~/challenge$ git add flag.txt
ShambhaviMishra-academy@webshell:~/challenge$ git commit -m "add flag"
[master 2d3f4b1] add flag
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 flag.txt
ShambhaviMishra-academy@webshell:~/challenge$ git push origin master
ssh: connect to host foggy-cliff.picoctf.net port 51594: Connection refused
fatal: Could not read from remote repository.
# Updating target link to the freshly launched server instance port 49907
ShambhaviMishra-academy@webshell:~/challenge$ git remote set-url origin ssh://git@foggy-cliff.picoctf.net:49907/git/challenge.git
ShambhaviMishra-academy@webshell:~/challenge$ git push origin master
git@foggy-cliff.picoctf.net's password: 
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 284 bytes | 284.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
remote: 
remote: Congratulations! Here is your flag:
remote: picoCTF{g1t_g00d_w1th_m3t4d4t4_b76fa19e}
remote: 
To ssh://foggy-cliff.picoctf.net:49907/git/challenge.git
   d8e31a2..2d3f4b1  master -> master



# --------------------------------------------
#             COMMANDS SUMMARY
# --------------------------------------------
#  Commands Used:
 # cd challenge:
 What it does: Changes your current working directory to move you inside the cloned project folder.
 Key Insight: Git commands will error out completely unless you are physically standing inside a tracked repository folder.
 # ls:
 What it does: Lists all visible files and folders inside your current directory path.
# cat README.md:
 What it does: Displays the entire content of the README.md file directly on your terminal screen without opening an external text editor.
# git config user.name "root" / git config user.email "root@picoctf":
 What it does: Sets the local author name and email attached to your upcoming project saves.
 Key Insight: Security or automation platforms often read this configuration data (metadata) to verify who is submitting the code before accepting it.
# git config --list:
 What it does: Dumps your entire current Git environment layout onto the screen. If it fills up your window, pressing q safely exits the viewer back to your command prompt.
# touch flag.txt:
 What it does: Instantly creates a brand new, empty file named flag.txt inside your current directory.
 Key Insight: Unless a challenge specifies content requirements, an empty file works perfectly fine to satisfy basic file-existence automated checks.
# git add flag.txt:
 What it does: Moves the file into the Git Staging Area. It explicitly flags this specific file to be included in your next permanent save point.
# git commit -m "add flag":
 What it does: Permanently takes a snapshot of your staged changes locally. The -m flag stands for Message, which allows you to type a quick description in quotes for human tracking. This text message is independent of your filenames.
# git remote set-url origin ssh://...:
 What it does: Redirects the target path for your project's upload location.
 Key Insight: When remote target boxes time out, restart, or shift to a new network port number, this command allows you to fix the pointing address without resetting your terminal workspace or deleting your local folder progress.
# git push origin master:
 What it does: Uploads all your locally committed snapshots from your local machine's master branch straight to the remote cloud hosting system.