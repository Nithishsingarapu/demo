from datetime import datetime

name=input("enter your name:")

lists='''
Rice Rs 20/kg
Sugar Rs 30/kg
Salt Rs 20/kg
4Oil Rs 80/liter
5Paneer Rs 110/kg
Maggi Rs 50/kg
Boost Rs 90/kg
Colgate Rs 85/each


'''


#declaration

price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'Rice':20,
'Sugar':30,
'Salt':20,
'Oil':80,
'Paneer':110,
'Maggi':50,
'Boost':90,
'Colgate':85
}

# hari==int(input("for list of items press 1:"))
# if hari==1:
#     print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items:")
        quantity=int(input("enter quantity"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((items,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")    
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
    if finalamount!=0:
            print(25*"=","nithish supermarket",25*"=")
            print(28*" ","hyderabad")
            print("name:",name,30*" ","Date:",datetime.now())
            print(75*" ")
            print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*' ' ,plist[i])
            print(75*"-")
            print(50*" ",'totalamount:','Rs',totalprice)
            print("gst amount,50*" ),'Rs',gst
            print(75*"-")    
