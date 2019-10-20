"""
My cake shop is so popular, I'm adding some tables and hiring wait staff so folks can have a cute sit-down cake-eating experience.

I have two registers: one for take-out orders, and the other for the other folks eating inside the cafe. All the customer orders get combined into one list for the kitchen, where they should be handled first-come, first-served.

Recently, some customers have been complaining that people who placed orders after them are getting their food first. Yikes—that's not good for business!

To investigate their claims, one afternoon I sat behind the registers with my laptop and recorded:

The take-out orders as they were entered into the system and given to the kitchen. (take_out_orders)
The dine-in orders as they were entered into the system and given to the kitchen. (dine_in_orders)
Each customer order (from either register) as it was finished by the kitchen. (served_orders)
Given all three lists, write a function to check that my service is first-come, first-served. All food should come out in the same order customers requested it.

We'll represent each customer order as a unique integer.

As an example,

  Take Out Orders: [1, 3, 5]
 Dine In Orders: [2, 4, 6]
  Served Orders: [1, 2, 4, 6, 5, 3]
would not be first-come, first-served, since order 3 was requested before order 5 but order 5 was served first.

But,

  Take Out Orders: [1, 3, 5]
 Dine In Orders: [2, 4, 6]
  Served Orders: [1, 2, 3, 5, 4, 6]
would be first-come, first-served.
"""

def f(input1, input2, input3):
    idx1 = 0
    idx2 = 0
    length1 = len(input1)
    length2 = len(input2)

    for v in input3:
        if idx1 < length1 and input1[idx1] == v:
            idx1 += 1
        elif idx2 < length2 and input2[idx2] == v:
            idx2 += 1
        else:
            return False

    if idx1 != len(input1) or idx2 != len(input2):
        return False

    return True


print(f([1, 3, 5], [2, 4, 6], [1, 2, 4, 6, 5, 3]))
print(f([1, 3, 5], [2, 4, 6], [1, 2, 3, 5, 4, 6]))