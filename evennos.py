n = int(input('enter n : '))

'''
i = 0

while i <= n:
  if not i % 2:
    print(i)
  i = i + 1'''

# for loop
'''
for <some var> in <sequence of elements>:
  set of statements that we want to repeat in the for block
'''

# 0 to n (including n)
# sequence from 0 to n (range(0, n + 1))
# range(n + 1) => 0 to n

for i in range(n + 1):
  if not i % 2:
    print(i)