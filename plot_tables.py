import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.20
fig = plt.subplots(figsize =(8, 6))

# set height of bar
Harikambhoji = [0.325, 0.276, 0.068, 0.083]
Shankarabharana = [0.29, 0.294, 0.078, 0.094]
Vachaspathi = [0.379, 0.355, 0.115, 0.136]
Kalyani = [0.216, 0.259, 0.061, 0.072]

# Set position of bar on X axis
br1 = np.arange(len(Harikambhoji))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]

sym_list = [".","//","o","\\","*"]
sym_counter = 0

# Make the plot
barlist = plt.bar(br1, Harikambhoji, color ='gray', width = barWidth,
        edgecolor ='black', label ='28. Harikambhoji (*)')
for i in range(0, len(barlist)):
        barlist[i].set_hatch(sym_list[sym_counter])
sym_counter += 1

barlist = plt.bar(br2, Shankarabharana, color ='darkgray', width = barWidth,
        edgecolor ='black', label ='29. Shankarabharana')
for i in range(0, len(barlist)):
        barlist[i].set_hatch(sym_list[sym_counter])
sym_counter += 1

barlist = plt.bar(br3, Vachaspathi, color ='dimgray', width = barWidth,
        edgecolor ='black', label ='64. Vachaspathi')
for i in range(0, len(barlist)):
        barlist[i].set_hatch(sym_list[sym_counter])
sym_counter += 1

barlist = plt.bar(br4, Kalyani, color ='lightgray', width = barWidth,
        edgecolor ='black', label ='65. Kalyani')
for i in range(0, len(barlist)):
        barlist[i].set_hatch(sym_list[sym_counter])
sym_counter += 1

plt.title('Distance of Raga Mohana with Parent Ragas', fontweight ='bold', fontsize = 15)
# Adding Xticks
plt.xlabel('Distance Metric', fontweight ='bold', fontsize = 15)
plt.ylabel('Distance Value', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Harikambhoji))],
        ['D(e)', 'D(bh)', 'D(kld)', 'D(js)'], fontsize = 12)

plt.legend()
plt.show()