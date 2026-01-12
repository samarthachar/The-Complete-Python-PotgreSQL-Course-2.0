import matplotlib.pyplot as plt


plt.figure()

plt.xlabel("Categories")
plt.ylabel("Amounts")
plt.title("Categories vs Amounts")


lines = plt.plot(["Men", "Women", "Children"],
         [3,5,9],
           # 'ko' - k for black, o makes circles instead of a joined line
           ) 
# plt.setp(lines, color="ff5566") - sets the line to a hexadecimal color
plt.show()