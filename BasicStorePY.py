
# coding: utf-8

# In[5]:


items = {"apples":100, "banana":200, "mango":300}
#This is the quantity of the items in the store
value = {"apple":30, "banana":20, "mango":40}
#This is the price of each item in store
print('***********************Welcome To Shop***********************\n')
print("Items in Shop :\n")
for i in items:
    print(f"{i}: ${items[i]}")
    bill = 0
    
while True:
    order = input("Enter your Order :: ")
    order=order.lower()
    if order == "cancel":
        print("Thank you for visiting :)")
        break
        
    elif order in items:
        quantity = int(input("Enter quantities :"))
        bill = bill+(items[order]*quantity)
print(f"Your Total bill is : ${bill}")

