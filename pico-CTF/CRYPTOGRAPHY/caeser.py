# LEVEL- Medium



def ceaser_decrypted():
    s = input("Encrypted text: ")
    
    for shift in range(1,26):
        result = ""
        for i in range(len(s)):          
            op = ord(s[i])
            if s[i].islower():
                op -= 97
                np = chr((op - shift) % 26 + 97)
                result += np
            
            elif s[i].isupper():
                op -= 65
                np = chr((op - shift) % 26 + 65)
                result += np

            else:
                result += s[i]
        print(f"Decrypted text: {result}")
    
ceaser_decrypted() 

    



###
"""
LINUX OPERTATIONS - ShambhaviMishra-academy@webshell:~/picoCTF_WRITEUPS/CRYPTOGRAPHY$ cd ..
ShambhaviMishra-academy@webshell:~/picoCTF_WRITEUPS$ git pull origin main
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (4/4), 1022 bytes | 340.00 KiB/s, done.
From https://github.com/Shambhavi-Mishra-2026/picoCTF_WRITEUPS
 * branch            main       -> FETCH_HEAD
   7ffd01c..42ba6bc  main       -> origin/main
Updating 7ffd01c..42ba6bc
Fast-forward
 CRYPTOGRAPHY/caesar.py | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
ShambhaviMishra-academy@webshell:~/picoCTF_WRITEUPS$ cd CRYPTOGRAPHY/
ShambhaviMishra-academy@webshell:~/picoCTF_WRITEUPS/CRYPTOGRAPHY$ python3 caesar.py 
Encrypted text: bqnrrhmfsgdqtahbnmphkgrwqj
Decrypted text: apmqqglerfcpszgamlogjfqvpi
Decrypted text: zolppfkdqeboryfzlknfiepuoh
Decrypted text: ynkooejcpdanqxeykjmehdotng
Decrypted text: xmjnndiboczmpwdxjildgcnsmf
Decrypted text: wlimmchanbylovcwihkcfbmrle
Decrypted text: vkhllbgzmaxknubvhgjbealqkd
Decrypted text: ujgkkafylzwjmtaugfiadzkpjc
Decrypted text: tifjjzexkyvilsztfehzcyjoib
Decrypted text: sheiiydwjxuhkrysedgybxinha
Decrypted text: rgdhhxcviwtgjqxrdcfxawhmgz
Decrypted text: qfcggwbuhvsfipwqcbewzvglfy
Decrypted text: pebffvatgurehovpbadvyufkex
Decrypted text: odaeeuzsftqdgnuoazcuxtejdw
Decrypted text: nczddtyrespcfmtnzybtwsdicv
Decrypted text: mbyccsxqdrobelsmyxasvrchbu
Decrypted text: laxbbrwpcqnadkrlxwzruqbgat
Decrypted text: kzwaaqvobpmzcjqkwvyqtpafzs
Decrypted text: jyvzzpunaolybipjvuxpsozeyr
Decrypted text: ixuyyotmznkxahoiutwornydxq
Decrypted text: hwtxxnslymjwzgnhtsvnqmxcwp
Decrypted text: gvswwmrkxlivyfmgsrumplwbvo
Decrypted text: furvvlqjwkhuxelfrqtlokvaun
Decrypted text: etquukpivjgtwdkeqpsknjuztm
Decrypted text: dspttjohuifsvcjdporjmitysl
Decrypted text: crossingtherubiconqilhsxrk
"""
###