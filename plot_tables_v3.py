"""
Code to plot tables to bar plot
JNMR paper tables

Author: Jom Kuriakose
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# filename = 'tables/Table5_Mohana.txt'
# Raga_name = "Mohana"
# parent_lab = "(*)"

# filename = 'tables/Table5_Madhyamavati.txt'
# Raga_name = "Madhyamavati"
# parent_lab = "(*)"

filename = 'tables/Table7_Gambhiranata.txt'
Raga_name = "Gambhiranata"
parent_lab = "(**)"

# filename = 'tables/Table7_Amritavarshini.txt'
# Raga_name = "Amritavarshini"
# parent_lab = "(*)"

# yaxis limits -- set ylim to None for default values
# ylim = None
ylim = [0,0.6]
# ylim = [0,1]

# set width of bar
# barWidth = 0.15
# barWidth = 0.10
barWidth = 0.08

# set height and width of figure
height = 6
# width = 8
width = 12

sym_list = [".","//","o","\\","*","xx","..",".O","++"]
color_list = ["gray","darkgray","dimgray","lightgray","slategrey","grey","darkgrey","dimgrey","lightgrey"]
color_list_new = list(mcolors.TABLEAU_COLORS.values())

def read_table(filename):
        with open(filename, 'r') as fid:
                file_data = fid.readlines()
        janaka_list = {}
        for i in range(len(file_data)):
                if i == 0:
                        pass
                else:
                        line = file_data[i].strip().split('\t')
                        janaka_list[line[0].strip()] = [float(j) for j in line[1:]]
        return janaka_list

def plot_figure(barWidth, height, width, sym_list, color_list, janaka_list, Raga_name, ylim, file_name):

        fig = plt.subplots(figsize =(width, height))

        # Set position of bar on X axis
        br_list = []
        for i in range(0,len(janaka_list)):
                if i == 0:
                        br_list.append(np.arange(len(janaka_list[list(janaka_list.keys())[0]])))
                else:
                        br_list.append([x + barWidth for x in br_list[i-1]])
        
        sym_counter = 0
        # Make the plot
        for i in range(0,len(janaka_list)):
                raga_label = list(janaka_list.keys())[i]
                print(raga_label)
                if parent_lab in raga_label:
                        barlist = plt.bar(br_list[i], janaka_list[raga_label], color = 'black', width = barWidth, edgecolor ='gray', label = raga_label)
                else:
                        barlist = plt.bar(br_list[i], janaka_list[raga_label], color = color_list[i], width = barWidth, edgecolor ='black', label = raga_label)
                        for j in range(0, len(barlist)):
                                barlist[j].set_hatch(sym_list[sym_counter])
                sym_counter += 1
        
        plt.title(f'Distance of Raga {Raga_name} with Parent Ragas', fontweight ='bold', fontsize = 10)
        # Adding Xticks
        plt.xlabel('Distance Metric', fontweight ='bold', fontsize = 10)
        plt.ylabel('Distance Value', fontweight ='bold', fontsize = 10)
        plt.xticks([r + barWidth*(len(janaka_list)-1)/2 for r in range(len(janaka_list[list(janaka_list.keys())[0]]))], [f"D(e)\nEuclidean\nDistance", f"D(bh)\nBhattacharya-Hellinger\nDistance", f"D(kld)\nKullback-Leiber\nDivergence", f"D(js)\nJensen-Shannon\nDistance"], fontsize = 8)

        if ylim:
                plt.ylim(ylim[0], ylim[1])
        plt.legend(fontsize=10)
        final_fig = plt.gcf()
        plt.show()
        plt.draw()
        print(f"Plot saved to {file_name}.png")
        final_fig.savefig(file_name+".png", bbox_inches="tight", dpi=300)
        plt.close()

if __name__ == '__main__':
        janaka_list = read_table(filename)
        file_name = os.path.splitext(os.path.basename(filename))
        plot_figure(barWidth, height, width, sym_list, color_list, janaka_list, Raga_name, ylim, 'plots/'+file_name[0])
        plot_figure(barWidth, height, width, sym_list, color_list_new, janaka_list, Raga_name, ylim, 'plots/'+file_name[0]+'_color')
