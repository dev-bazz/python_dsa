
# List for serialized data accessed by indexing

data_list = [1,2,3,4,5,6,7, 1]
# accessing data from it
print('number two: ', data_list[1])
# can use compresion with it
multiple_of_three = [x*3 for x in data_list]
print('multiple_of_three: ', multiple_of_three)
# You can splice data
spliced_list = multiple_of_three[:]
print('spliced_list: ', spliced_list)
# To modify alist use
data_list.append(8)
print('append eight: ', data_list)
data_list.pop()
print('removed last: ', data_list)
data_list.remove(5)
print('remove fistt five you see: ', data_list)

