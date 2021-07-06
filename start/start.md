# start

## Description
Just a start. "nc chall.pwnable.tw 10000" start

## Solution

###### Throw start into gdb, find the entry function.
```
_start
```
###### Disassemble the function and add some comments(by myself).
```
0x08048060 <+0>:     push   esp
0x08048061 <+1>:     push   0x804809d	; return address
0x08048066 <+6>:     xor    eax,eax		; clear registers
0x08048068 <+8>:     xor    ebx,ebx
0x0804806a <+10>:    xor    ecx,ecx
0x0804806c <+12>:    xor    edx,edx

0x0804806e <+14>:    push   0x3a465443	; push string to stack
0x08048073 <+19>:    push   0x20656874
0x08048078 <+24>:    push   0x20747261
0x0804807d <+29>:    push   0x74732073
0x08048082 <+34>:    push   0x2774654c

0x08048087 <+39>:    mov    ecx,esp		; point esp to the string (stack)
0x08048089 <+41>:    mov    dl,0x14		; length of the string is 0x14
0x0804808b <+43>:    mov    bl,0x1		; stdout
0x0804808d <+45>:    mov    al,0x4		; write function
0x0804808f <+47>:    int    0x80		; call write

0x08048091 <+49>:    xor    ebx,ebx		; clear
0x08048093 <+51>:    mov    dl,0x3c		; can read 0x3c(bigger than 0x14), meanwhile ecx still points to the same address
										; therefore we can modify return address by sending a longer string
0x08048095 <+53>:    mov    al,0x3		; read function
0x08048097 <+55>:    int    0x80		; call read
0x08048099 <+57>:    add    esp,0x14	; pop stack
0x0804809c <+60>:    ret
```

If we can put our shellcode in and run it, we will have a shell.

###### Idea



