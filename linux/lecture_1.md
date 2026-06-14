# Lecture- 1

# 1- echo
repeats whatevever is comanded 
General form - echo "whatever you want to say"
:- spaces matter example spaces between the double quotes
:- linux is case sensitive
:- the double quotes tell linux precisely what string of text to repeat

# 2- whoami
*Purpose:* 
The name stands for "who am i." It asks the operating system to identify the name of the user currently logged into the terminal
*The Logic:* 
When you type whoami and press Enter, the system looks up the current user account information and prints the username directly to your screen.
*Why use it?*
In Linux, you might often switch between different user accounts (like your standard user or a root/administrator account) or work across multiple servers. Since the terminal interface doesn't always show your username by default, whoami serves as a quick way to double-check which account you are using before you run commands that might affect files or system settings.

# 3- id
:- Way to see what groups we belong to.In Linux, users are organized into groups. These groups determine the permissions and access rights a user has.
*The result shows:-*
**uid**: Your User ID (a unique numerical identifier).
**gid**: Your primary Group ID.
**groups**: All the groups you are a member of.

:-We can also use id to look up other users

### root is the superuser – like the administrator of the system!

# 4- id -un
:- Sometimes id prints more detail than you need. A practical skill is learning how to ask for a specific piece of information.

:- id -un prints only your username (the name for our current UID)