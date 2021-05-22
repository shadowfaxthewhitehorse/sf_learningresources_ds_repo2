# using nested for loops to generate binary
# 
# binary
#
# 0000
# 0001
# 0010
# 0011

def create_4_bit_binary():

    bin_list = []

    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    bin_list.append([i, j, k, l])

    return bin_list

# print(create_4_bit_binary())

ret_val = create_4_bit_binary()

for lst1 in ret_val:
    print(lst1)
