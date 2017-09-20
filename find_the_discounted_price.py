'''
Bhagyaraj Chitoth
20-09-2017

Problem:-
Your friend Cody has to sell a lot of jam, so he applied a good 25% discount to all his merchandise.

Trouble is that he mixed all the prices (initial and discounted), so now he needs your cool coding skills to filter out only the discounted prices.

For example, consider this inputs:

"15 20 60 75 80 100"
"9 9 12 12 12 15 16 20"
They should output:

"15 60 75"
"9 9 12 15"
Every input will always have all the prices in pairs (initial and discounted) sorted from smaller to bigger.

You might have noticed that the second sample input can be tricky already; also, try to have an eye for performances, as huge inputs could be tested too.

Solution:-

'''

def find_discounted(prices):
    #your code here
    priceList=prices.split(' ')
    lst=""
    priceList1=priceList[:]
    
    for i in priceList1:
        if priceList=='':
            break
        if i in priceList:
            if priceList=='':
                break
            else:
                try:
                    if str((int(i)/3)*4) in priceList:
                        if len(lst)==0:
                            lst=str(i)
                            priceList.remove(str(i))
                            priceList.remove(str((int(i)/3)*4))
                            
                        else:
                            lst=lst+" "+str(i) 
                            priceList.remove(str(i))
                            priceList.remove(str((int(i)/3)*4))
                except ValueError:
                    pass
                
    
    return lst

