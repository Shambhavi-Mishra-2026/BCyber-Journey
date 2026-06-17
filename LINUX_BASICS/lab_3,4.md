# Lab 3,4

### Working environment in linux
In Linux, each user typically has a "home directory," represented by ~.

# 1- pwd
:-pwd stands for "print working directory."

*:-What it does:*
 In Linux, your "working directory" is simply the folder you are currently "inside" as you interact with the command line. When you run pwd, the system looks at your current location and prints the full path to that folder on your screen.

*:-Why it is useful:*
 Because the Linux file system can be very deep, it is easy to "get lost" while moving between folders. Running pwd acts like a "You Are Here" marker on a map, telling you exactly where you are in the file system hierarchy.

*How to use it:*
just type pwd into the terminal and press Enter
General form: **pwd**

# 2- echo ~
*:- echo:*
 This is a command used to display text or information on your screen. Think of it like a "print" command that tells the computer, "Show me what this is."

*:- "~" (The Tilde):*
 In Linux, the tilde is a special symbol that acts as a shortcut for your home directory. No matter where you are in the file system, the system always knows that ~ points to your personal home folder.

*:-How the overall logic works:*
When you run echo ~, you are essentially asking the computer: "Can you tell me the full path of my home directory?"

The computer interprets the ~ symbol, converts it into the actual path (like /home/labex), and then echo displays that path on your screen so you can see exactly where your home folder is located. 

# Difference between pwd and echo ~ 
I was confused about this command since everywhere it was mentioned that its basicaaly the path to the home directory but actual definition could be :

---Your Home directory (~) is your permanent home address. It never changes, no matter where you travel inside the computer, so using echo we just print that home address .pwd is like opening Google Maps on your phone to check your current GPS coordinates. It tells you exactly where you are standing right this second.
 
 ---- although everywhere the definition of **echo ~** is path to home directory in reality it just tells us about the home address no relative path from where you are to home address

# 3- ls
:-It stands for "list."
*:-The Command (ls):*
 This tells the system to look inside a specific directory.

*:-The Logic:*
 When you simply type ls and press Enter, the system automatically points to your current working directory.
 General form: **ls**

*:-The Action:*
 It scans the directory and presents a list of all the files and folders contained within it.

*Analogy:*
Imagine you are standing in a room. Using ls is like taking a quick look around and listing everything you see in that room. It doesn't move you to a different room; it just gives you a report of what is currently around you.

*Pro-tip:*
If you want to see what's in a different directory without actually moving there, you can add the path after the command, This allows you to "peek" into other folders while staying exactly where you are.
General form: **ls /location1/location2**

# 4- ls ~
*:-How the logic works:*
When you type ls ~ and press Enter, you are giving the system two pieces of information: what you want to do (list files) and where to do it (in your home directory).

Even if you are currently working inside different folder, running ls ~ tells the system to temporarily look "back" at your home directory and display the contents found there.

*Analogy*
It is a way to look into your home folder from anywhere in the system without having to change your current location.

### Navigating the File System
Linux uses what we call a "hierarchical file system". Think of it like a big tree with branches. The main trunk is called the "root directory", represented by a single forward slash /. All other directories and files branch out from this root.

# 5- cd 
*:- cd:*
 This stands for "change directory." It is the command used to move from one folder to another.
General form: **cd target directory**

*:-How the logic works:*
When you run this command, the system looks inside your current directory to see if there is a folder named "td". If it finds one, it updates your location to that folder.

*:-The Logic:*
 It follows the path: [Current Location] + / + [td].
Example: If you are currently in your home directory (/home/labex), running **cd td** will move you into the folder located at /home/labex/project.

*:-Key Point:*
This command uses a relative path. This means it assumes the "td" folder is located right inside the folder where you are currently standing. If "td" wasn't in your current directory, the system would let you know there is "no such file or directory."

# 6- cd ..
It stands for "change directory to the parent."

*:- How this works:*
**cd:** This stands for "change directory." It is the command used to move from one folder to another.
**..**: In Linux, the two dots represent a special "shortcut" that always points to the parent directory (the folder directly "above" your current one in the file hierarchy).

*:-How the logic works:*
Think of your computer's folders as a tree structure. You are currently in /home/labex/project. The folder that "contains" your project folder is /home/labex.

When you type cd .., you are telling the computer: "Move me out of my current folder and into the one that contains it."

*Analogy*
It is essentially the same as clicking the "Back" or "Up" button in a typical graphical file explorer. It's a quick way to climb up the directory tree without having to type out long file paths!

# 7- cd /home/labex/project
The command cd /home/labex/project is a way to move to a specific folder by telling the computer the exact, complete address of that folder. This is known as an absolute path.

*:- How this works:*
**cd:** The command to "change directory."
**/:** The first slash represents the root directory, which is the very top of the Linux file system (the "trunk of the tree").
**/home/labex/project:** This is the full path. It tells the computer exactly which branches to follow from the root:
Start at the root (/).
Go into the home folder.
Go into the labex user folder.
Go into the project folder.

*:-How the logic works:*
Because this command starts with a / (representing the root), it is an absolute path. This means it is "unambiguous"—it works exactly the same way no matter where you are currently located in the file system.

If you are already in the project folder: Nothing happens.
If you are anywhere else on the system: The computer ignores your current location and jumps directly to that specific full path.

*Analogy*
 If cd project is like saying "go to the room next door," cd /home/labex/project is like giving someone the full street address of your house. It doesn't matter where they are starting from; they will always end up at the same destination.

# 8- cd ~
The command cd ~ is a quick way to jump back to your starting point.

*:- How this works:*
**cd:** This is the command to "change directory."
**~:** This symbol (the tilde) is a special Linux shortcut for "Home Directory." In your lab environment, this translates to /home/labex.

*:-How the logic works:*
When you run cd ~, you are giving the shell a shortcut to your personal user folder.

*:-The Logic:*
Instead of typing the full path (like cd /home/labex), which can be long and easy to mistype, the shell recognizes the ~ symbol and automatically expands it to your full home directory path.

*:-The Result:*
No matter where you are in the file system (or how many folders deep you've traveled), running **cd ~** will instantly take you back to your home base.

*Analogy*
It is exactly like a "Home" button in a web browser—it provides a single, reliable way to return to the beginning regardless of where you currently are.

### Creating Files and Listing Directory Contents
