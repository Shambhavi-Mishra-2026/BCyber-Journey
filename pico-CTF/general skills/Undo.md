ShambhaviMishra-academy@webshell:~$ nc foggy-cliff.picoctf.net 60532
===Welcome to the Text Transformations Challenge!===

Your goal: step by step, recover the original flag.
At each step, you'll see the transformed flag and a hint.
Enter the correct Linux command to reverse the last transformation.

--- Step 1 ---
Current flag: KTJxNW85NjQ1LWZhMDFnQHplMHNmYTRlRy1nazNnLXRhMWZlcmlyRShTR1BicHZj
Hint: Base64 encoded the string.
Enter the Linux command to reverse it: base64
Incorrect. Try again.
Output: S1RKeE5XODVOalExTFdaaE1ERm5RSHBsTUhObVlUUmxSeTFuYXpObkxYUmhNV1psY21seVJTaFRS
MUJpY0haag==
Hint: Try reversing: base64

Enter the Linux command to reverse it: base64 -d
Correct!

--- Step 2 ---
Current flag: )2q5o9645-fa01g@ze0sfa4eG-gk3g-ta1ferirE(SGPbpvc
Hint: Reversed the text.
Enter the Linux command to reverse it: rev
Correct!

--- Step 3 ---
Current flag: cvpbPGS(Eriref1at-g3kg-Ge4afs0ez@g10af-5469o5q2)
Hint: Replaced underscores with dashes.
Enter the Linux command to reverse it: tr "_" "-"
Incorrect. Try again.
Output: cvpbPGS(Eriref1at-g3kg-Ge4afs0ez@g10af-5469o5q2)
Hint: Try reversing: tr '_' '-'

Enter the Linux command to reverse it: tr "-" "_"
Correct!

--- Step 4 ---
Current flag: cvpbPGS(Eriref1at_g3kg_Ge4afs0ez@g10af_5469o5q2)
Hint: Replaced curly braces with parentheses.
Enter the Linux command to reverse it: tr "{}" "()"
Incorrect. Try again.
Output: cvpbPGS(Eriref1at_g3kg_Ge4afs0ez@g10af_5469o5q2)
Hint: Try reversing: tr '{}' '()'

Enter the Linux command to reverse it: tr "()" "{}"
Correct!

--- Step 5 ---
Current flag: cvpbPGS{Eriref1at_g3kg_Ge4afs0ez@g10af_5469o5q2}
Hint: Applied ROT13 to letters.
Enter the Linux command to reverse it: tr "A-Za-z" "N-ZA-Mn-za-m"
Correct!

Congratulations! You've recovered the original flag:
>>> picoCTF{Revers1ng_t3xt_Tr4nsf0rm@t10ns_5469b5d2}


# they only asked about the command used not the exact command to type out
