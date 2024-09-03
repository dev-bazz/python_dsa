months = [2200, 2350,2600,2130,2190, 2000]

print("Extra cost feb - jan",(months[0] - months[1]* 1))
print("Sum first quater", sum(months[:3]))

spent_2000k = [ (index, x) if x == 2000 else (index, "Not 2000") for index, x in enumerate(months)  ]
print('spent_2000k: ', spent_2000k)


months.append(1980)
print(months)
months[3] = months[3] - 200
print('months: ', months)

print ("2000 in any month", 2000 in months)
