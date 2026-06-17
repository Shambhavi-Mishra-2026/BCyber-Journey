
ShambhaviMishra-academy@webshell:~$ ls
README.txt  challenge  ende.py  flag.txt.en  password.txt
ShambhaviMishra-academy@webshell:~$ cat password.txt
720b6ad346f84cd483c60c7464dd95d4
ShambhaviMishra-academy@webshell:~$ python3 ende.py -d flag.txt.en
Please enter the password:720b6ad346f84cd483c60c7464dd95d4
picoCTF{4p0110_1n_7h3_h0us3_9c5f9bcf}
ShambhaviMishra-academy@webshell:~$     

# python3 (with file flags)
 Invokes the Python 3 runtime interpreter binary to execute scripts directly through the text terminal.General form - python3 script_name.py -flag target_file
Flag Breakdowns:
 -d: A custom command-line flag programmed by the script's developer that stands for "Decrypt" (unscramble). It tells the code to activate its file-unlocking logic.
 -e (Alternative): The opposite operational flag, standing for "Encrypt" (scramble).
 *The Logic:* Instead of clicking graphics, you pass "arguments" (the text after the script name) into the terminal. The Python tool reads these options sequentially using its internal argument system (sys.argv), matches the -d switch to a specific code block, reads the scrambled data inside flag.txt.en, and prompts the user to input an authentication key to unlock the data array. 
 *Why use it here?* In cybersecurity, you will regularly deal with proprietary software or helper tools (ende.py) written by team members or targets. To use them without a graphical user interface, you must pass structural execution flags (-d) to force the code into the exact functional loop you want to trigger.

# wgetThe name stands for "Web Get." 
 It is a non-interactive, network-based file downloader that pulls assets directly from internet servers into your local folder path.
 General form - wget URL_OF_THE_FILE
 *The Logic:* wget works behind the scenes by establishing an automated network connection (HTTP/HTTPS/FTP) to the remote server IP address. It requests the specific file bytes listed at the end of the URL path, streams those bytes across your network interface card, and writes them down onto your terminal storage path under its exact original name.
 *Why use it here?* When working inside professional command-line workspaces (like the picoCTF webshell or secure enterprise environments) [picoctf.org], you do not have a web browser or a mouse cursor to click a "Download File" graphic. wget is the industry standard utility used to fetch exploit payloads, scripts, patches, and network captures straight into your current directory using strings of text alone.
# File Extensions (.en)
 A custom configuration marker added to the end of a filename to signal how the underlying data is formatted.
 General form - filename.txt.en
 *The Logic:* Linux does not fundamentally care about file extensions; it treats every file as a raw block of bytes. However, developers use compound extensions like .txt.en as a human-readable tag to indicate that this text file (.txt) has been run through an encryption engine and is currently saved as "encrypted ciphertext" (.en).
 *Why use it here?* If you try to view the raw contents of flag.txt.en using a reading tool like cat, it will dump illegible binary characters and gibberish onto your terminal. Recognizing the .en suffix alerts you that the file cannot be processed as a standard text layer until you pass it through an matching decryption pipeline.