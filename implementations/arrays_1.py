my_expenses = [2200, 2350, 2600, 2130, 2190]
# 1. In Feb, how many dollars you spent extra compare to January?
print(f"In Feb, I spent {my_expenses[1] - my_expenses[0]}$ extra dollars compared to January")

# 2. Find out your total expense in first quarter (first three months) of the year.
print(f"My total expense in the first quarter of the year is {sum(my_expenses[:3]):,}$")

# 3. Find out if you spent exactly 2000 dollars in any month
print(f"Did I spend exactly 200$? {2000 in my_expenses}")

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
my_expenses.append(1980)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
my_expenses[3] -= 200

print(f"My expenses as of June this year {my_expenses}")