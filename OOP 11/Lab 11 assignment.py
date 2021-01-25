

'''
For this your task is to enter at least 10 mobile numbers in a file of 
different companies based on list provided to you. 
Extract the mobile numers such as 0332 is for Ufone,then at the end of the 
list calculate each mobile network in total. The required output will be:
    
'''

import re


def track():
    f1 = open('numbers.txt', 'w')
    
    n = 0
    while n < 10:
        ask = int(input("Enter your number: "))
        f1.write(f"{ask} ")
        n += 1
    f1.close()
    
    f1 = open('numbers.txt', 'r')
    
    
    jazz = '^30'
    jnet = 0
    zong = '^31'
    znet = 0
    warid = '^32'
    wnet = 0
    ufone = '^33'
    unet = 0
    telenor = '^34'
    tnet= 0
    scom = '^35'
    scnet = 0
    insta = '^36'
    innet = 0
    
    num = []
    for i in f1:
        num.append(i)
    
    for j in num:
        f = re.split('\s', j)
        f.pop()
  
    for k in f:
        if re.search(jazz, k):
            jnet+=1
        if re.search(zong, k):
            znet+=1
        if re.search(warid, k):
            wnet+=1
        if re.search(ufone, k):
            unet +=1
        if re.search(telenor, k):
            tnet+=1
        if re.search(scom, k):
            scnet+=1
        if re.search(insta, k):
            innet+=1
    
    print("---------------------")
    if jnet>0:
        print(f"Moblink Users: {jnet}")
    if znet>0:
        print(f"Zong Users: {znet}")
    if wnet>0:
        print(f"Warid Users: {wnet}")
    if unet>0:
        print(f"Ufone Users: {unet}")
    if tnet>0:
        print(f"Telenor Users: {tnet}")
    if scnet>0:
        print(f"SCOM Users: {scnet}")
    if innet>0:
        print(f"Instaphone: {innet}")
    total = jnet+znet+wnet+unet+tnet+scnet+innet
    print(f"\nTotal Users: {total}")
    
        
    f1.close()
    
track()

