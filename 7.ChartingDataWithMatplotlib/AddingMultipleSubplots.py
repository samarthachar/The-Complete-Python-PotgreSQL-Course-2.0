import matplotlib.pyplot as plt

# figure = plt.figure()
# ax1 = figure.add_subplot(1,2,1)
# ax2 = figure.add_subplot(1,2,2)

# Same as

figure, (ax1, ax2) = plt.subplots(1,2)

ax1.plot([1,2,3,4], [3,5,9,25])
ax2.plot([1,2,3,4], [5,7,11,17])
