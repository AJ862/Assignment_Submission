# -*- coding: utf-8 -*-
"""Day_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wvpujo9X3RtCwXJfYw9T8nwBSQ7R1cGk

ANSWER - 1
"""

list1 = ["RANIBOW",'RAINBOW','BOWRANI','ROBWANI']
a = "RAINBOW"
for i in list1:
  if i == a:
    print("CORRECT")
  else:
    print("WRONG")

"""ANSWER 2"""

print("LETS UPGRADE")

"""ANSWER 3"""

CP = int(input())
SP = int(input())
Result = SP - CP
if Result>0:
  print("profit")
elif Result<0:
  print("Loss")
else:
  print("Neither")

"""ANSWER 4"""

Euro = int(input())
print(Euro*80)