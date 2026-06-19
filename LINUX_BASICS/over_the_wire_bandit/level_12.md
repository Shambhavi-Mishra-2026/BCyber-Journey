>ssh bandit12@bandit.labs.overthewire.org -p 2220

bandit12@bandit:~$ ls
data.txt
bandit12@bandit:~$ file data.txt
data.txt: ASCII text
bandit12@bandit:~$ cat data.txt
00000000: 1f8b 0808 b5ea 2e6a 0203 6461 7461 322e  .......j..data2.
00000010: 6269 6e00 0144 02bb fd42 5a68 3931 4159  bin..D...BZh91AY
00000020: 2653 5974 2e33 e700 0019 7fff dbe2 bfbf  &SYt.3..........
00000030: e7df de3f b4ff ffaf f77f f6ec 9ffa fcaf  ...?............
00000040: ffb1 bffb ff2f e3ff fedf f5ef b001 39ac  ...../........9.
00000050: 0800 0d00 680d 0031 320d 001a 01a0 01a3  ....h..12.......
00000060: 2000 681a 0000 0000 0006 9a1a 1b48 d064   .h..........H.d
00000070: 347a 8326 9e9a 8c80 6f54 2034 34d0 1901  4z.&....oT 44...
00000080: a341 a064 00c4 3464 d068 034c 40d0 1901  .A.d..4d.h.L@...
00000090: a1a1 a310 001a 0064 0061 1804 068d 190d  .......d.a......
000000a0: 0000 0065 34d0 1a00 068d 1a34 341e a340  ...e4......44..@
000000b0: 01a3 27a8 341e a01e a326 8000 f503 4680  ..'.4....&....F.
000000c0: 7a80 0000 1a1e a686 8006 868d 0034 1a00  z............4..
000000d0: d010 2001 a200 2a8e 3e31 e5b6 2542 9bab  .. ...*.>1..%B..
000000e0: 4233 3410 665a 517e 6089 12de 9443 c46f  B34.fZQ~`....C.o
000000f0: 1ccf 951d 3122 b875 41c2 fef4 961d 7df0  ....1".uA.....}.
00000100: e401 c72b f6dd a1a3 5169 6819 600e 58c3  ...+....Qih.`.X.
00000110: 2a81 88f0 db94 9963 f281 5228 409a 41a3  *......c..R(@.A.
00000120: 7b29 8a49 4727 dd71 716e 4152 41a3 fb1b  {).IG'.qqnARA...
00000130: 20ea ff77 2ccf c5e6 fa50 35e9 9309 e2ee   ..w,....P5.....
00000140: 6cf9 d6ec beb9 0756 abf3 f35c 127e 8bae  l......V...\.~..
00000150: 4cb2 41d4 c1f9 bf5f 4b91 73da 0c2c 095c  L.A...._K.s..,.\
00000160: e07b 9222 1d22 f005 0b27 364f 5499 8613  .{."."...'6OT...
00000170: a991 a592 df3b bc5c 2901 1093 0b25 6620  .....;.\)....%f
00000180: 28bb bf6f 18c6 c4fb 08cc 169e 24b8 9247  (..o........$..G
00000190: 78d0 c0e7 c21f b672 34fa 5a6a 6387 432c  x......r4.Zjc.C,
000001a0: 6850 b4e5 5510 ab66 1c36 32d7 8b55 950b  hP..U..f.62..U..
000001b0: a86d 822a 488d 41e2 a2bd dc85 72a6 c959  .m.*H.A.....r..Y
000001c0: df82 a03e 60bb 0213 7645 1fd8 bd7d 22ed  ...>`...vE...}".
000001d0: 064c d539 9322 9b13 b4a2 2f68 482e af05  .L.9."..../hH...
000001e0: 3eee e2e3 ddf6 df09 0c18 74b8 5d69 28cc  >.........t.]i(.
000001f0: 53a8 f84e fc81 f151 2a94 eebe 0c0d b102  S..N...Q*.......
00000200: 103f f781 ab4a 27ce a68f e224 7029 76ec  .?...J'....$p)v.
00000210: 45d7 1e28 3fa6 c9a9 cdfd e91a 85a4 2674  E..(?.........&t
00000220: ade4 874f 2b2b 7000 57dc 6937 0403 9a1f  ...O++p.W.i7....
00000230: 7386 7941 4f07 92ad 6cca 794b 0cd0 02aa  s.yAO...l.yK....
00000240: c08a 01d6 e25e 4196 ae9d 01b7 dc44 c78e  .....^A......D..
00000250: 97fe ff17 7245 3850 9074 2e33 e723 d2aa  ....rE8P.t.3.#..
00000260: 5444 0200 00                             TD...
bandit12@bandit:~$ mkdir /tmp/temppp/
bandit12@bandit:~$ cd /tmp/temppp/
bandit12@bandit:/tmp/temppp$ ls
bandit12@bandit:/tmp/temppp$ cd ~
bandit12@bandit:~$ cp data /tmp/temppp/data.txt
cp: cannot stat 'data': No such file or directory
bandit12@bandit:~$ cp data.txt /tmp/temppp/data.txt
bandit12@bandit:~$ cd /tmp/temppp/
bandit12@bandit:/tmp/temppp$ ls
data.txt
bandit12@bandit:/tmp/temppp$ file data.txt
data.txt: ASCII text
bandit12@bandit:/tmp/temppp$ xxd -r data.txt > data
bandit12@bandit:/tmp/temppp$ ls
data  data.txt
bandit12@bandit:/tmp/temppp$ file data
data: gzip compressed data, was "data2.bin", last modified: Sun Jun 14 17:53:57 2026, max compression, from Unix, original size modulo 2^32 580
bandit12@bandit:/tmp/temppp$ mv data data.gz
bandit12@bandit:/tmp/temppp$ gunzip data.gz
bandit12@bandit:/tmp/temppp$ ls
data  data.txt
bandit12@bandit:/tmp/temppp$ file data
data: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/temppp$ mv data data.bz2
bandit12@bandit:/tmp/temppp$ bzip2 -d data.bz2
bandit12@bandit:/tmp/temppp$ ls
data  data.txt
bandit12@bandit:/tmp/temppp$ file data
data: gzip compressed data, was "data4.bin", last modified: Sun Jun 14 17:53:57 2026, max compression, from Unix, original size modulo 2^32 20480
bandit12@bandit:/tmp/temppp$ mv data data.gz
bandit12@bandit:/tmp/temppp$ gunzip data.gz
bandit12@bandit:/tmp/temppp$ ls
data  data.txt
bandit12@bandit:/tmp/temppp$ file data
data: POSIX tar archive (GNU)
bandit12@bandit:/tmp/temppp$ mv data data.tar
bandit12@bandit:/tmp/temppp$ tar -xf data.tar
bandit12@bandit:/tmp/temppp$ ls
data5.bin  data.tar  data.txt
bandit12@bandit:/tmp/temppp$ file data5.bin
data5.bin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/temppp$ mv data5.bin data5.tar
bandit12@bandit:/tmp/temppp$ tar -xf data5.tar
bandit12@bandit:/tmp/temppp$ ls
data5.tar  data6.bin  data.tar  data.txt
bandit12@bandit:/tmp/temppp$ file data6.bin
data6.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/temppp$ mv data6.bin data6.bz2
bandit12@bandit:/tmp/temppp$ bzip2 -d data6.bz2
bandit12@bandit:/tmp/temppp$ ls
data5.tar  data6  data.tar  data.txt
bandit12@bandit:/tmp/temppp$ file data6
data6: POSIX tar archive (GNU)
bandit12@bandit:/tmp/temppp$ mv data6 data6.tar
bandit12@bandit:/tmp/temppp$ tar -xf data6.tar
bandit12@bandit:/tmp/temppp$ ls
data5.tar  data6.tar  data8.bin  data.tar  data.txt
bandit12@bandit:/tmp/temppp$ file data8.bin
data8.bin: gzip compressed data, was "data9.bin", last modified: Sun Jun 14 17:53:57 2026, max compression, from Unix, original size modulo 2^32 49
bandit12@bandit:/tmp/temppp$ mv data8.bin data8.gz
bandit12@bandit:/tmp/temppp$ gunzip data8.gz
bandit12@bandit:/tmp/temppp$ ls
data5.tar  data6.tar  data8  data.tar  data.txt
bandit12@bandit:/tmp/temppp$ file data8
data8: ASCII text
bandit12@bandit:/tmp/temppp$ cat data8
The password is FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
bandit12@bandit:/tmp/temppp$ exit

