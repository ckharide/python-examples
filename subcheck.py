#!/usr/bin/env python3

import subprocess
import os

class NmapPy():
    def __init__(self, command=[]):
        self.command=command

    def scan(self):
        try:
            p=subprocess.Popen(self.command, shell=False,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out,err=p.communicate()
            print("\n Nmap scan is complete : ")
            print(str(out))
            print(str(err))
        except Exception as ex:
            print("Exception caught : "+str(ex))
    
    def call(self,mycommand=[]):
        try:
            pr = subprocess.run(mycommand,check =True , stdout=subprocess.PIPE, universal_newlines=True)
            print("\n command excecution is complete \n")
            print(pr.stdout)
        
        except Exception as e :
            print("Exception caught " +str(e))

nmap=NmapPy(["cat", "test.py"])
nmap.scan()
nmap.call(["ls", "-ah"])