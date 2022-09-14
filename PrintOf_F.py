 # nums = [5,2,5,2,2]
# for x in nums:
#         print("X"*x)

# Another solution using nested loops

nums = [5, 2, 5, 2, 2]
for x in  nums:
    output = ""
    for count in range(x):
        output+="X"
    print(output)