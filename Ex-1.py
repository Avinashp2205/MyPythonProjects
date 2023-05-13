'''Exercise: Array DataStructure
1. Let us say your expense for every month are listed below,
    (i) January - 2200
    (ii) February - 2350
    (iii) March - 2600
    (iv) April - 2130
    (v) May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this'''

expenses = [["January", 2200], ["February", 2350], ["March", 2600], ["April", 2130], ["May", 2190]]
exp = [2200, 2350, 2600, 2130, 2190]
ans1 = int(expenses[1][1])-int(expenses[0][1])
print("1. In Feb, we spent ", ans1, " dollars extra.")
ans2 = int(expenses[0][1])+int(expenses[1][1])+int(expenses[2][1])
print("2. First Quarter expenses- ",ans2)
# ans3 =
print("3. Did I spent 2000 in any month? ", 2000 in exp)
exp.append(1980)
print("4. Expenses at the end of June is- ",exp)
exp[-3] = exp[-3] - 200
print("5.",exp)