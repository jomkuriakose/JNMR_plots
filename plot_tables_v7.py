"""
Code to plot tables to normalized bar plot
JNMR paper tables

Histogram plots of LCSS tables

Author: Jom Kuriakose
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# ----------------------------------------------------------------

filename = 'tables_lcss/Table1_LCSS.txt'
parent_lab = "(*)"

# ----------------------------------------------------------------

# yaxis limits -- set ylim to None for default values
ylim = None
# ylim = [0,0.6]
# ylim = [0,1]

legend_size = 12
legend_position = 'best'
# legend_position = 'upper right'
bbox_shift = None
plot_hline = False

# set width of bar
# barWidth = 0.18
# barWidth = 0.15
barWidth = 0.12
# barWidth = 0.10
# barWidth = 0.08
# bbox_shift = [1, 1]

# set height and width of figure
height = 4
# height = 6
# width = 6
width = 8
# width = 10
# width = 12

# ----------------------------------------------------------------

sym_list = [".","//","o","\\","x","..","xx",".O","++"]
color_list = ["gainsboro","gray","darkgray","dimgray","lightgray","grey","darkgrey","dimgrey","lightgrey"]
color_list_new = list(mcolors.TABLEAU_COLORS.values())

# ----------------------------------------------------------------

def read_table_lcss(filename):
        with open(filename, 'r') as fid:
                file_data = fid.readlines()
        janaka_list = {}
        for i in range(len(file_data)):
                line = file_data[i].strip().split('\t')
                janya_name = line[0].strip()
                janaka_list[janya_name] = {}
                for j in range(0, int(line[1])):
                        if "Janaka_list" in janaka_list[janya_name].keys():
                                janaka_list[janya_name]["Janaka_list"].append(line[(j+1)*2])
                                janaka_list[janya_name]["LCSS_dist"].append(float(line[((j+1)*2)+1]))
                        else:
                                janaka_list[janya_name]["Janaka_list"] = [line[(j+1)*2]]
                                janaka_list[janya_name]["LCSS_dist"] = [float(line[((j+1)*2)+1])]
        return janaka_list

# ----------------------------------------------------------------

def plot_figure(barWidth, height, width, sym_list, color_list, color_flag, janaka_list, ylim, legend_size, legend_position, bbox_shift, plot_hline, file_name):

        fig = plt.subplots(figsize =(width, height))

        if plot_hline:
                # hline_loc = [1.0, 0.8, 0.6, 0.4, 0.2]
                # hline_loc = [1.0, 0.7, 0.4]
                hline_loc = [1.0, 0.6, 0.2]
                for i in range(0,len(hline_loc)):
                        plt.axhline(y=hline_loc[i], color='grey', linestyle='--')

        # Set position of bar on X axis
        xaxis_list = []
        for i in range(0,len(janaka_list)):
                for j in range():
                        # 
        
        sym_counter = 0

        # Make the plot
        for i in range(0,len(janaka_list)):
                raga_label = list(janaka_list.keys())[i]
                # print(raga_label)
                if parent_lab in raga_label:
                        barlist = plt.bar(br_list[i], janaka_list[raga_label], color = 'black', width = barWidth, edgecolor ='gray', label = raga_label)
                else:
                        barlist = plt.bar(br_list[i], janaka_list[raga_label], color = color_list[i], width = barWidth, edgecolor ='black', label = raga_label)
                        if not color_flag:
                                for j in range(0, len(barlist)):
                                        barlist[j].set_hatch(sym_list[sym_counter])
                sym_counter += 1
        
        plt.title(f'LCSS Distance of Janya Ragas with Janaka Ragas', fontweight ='bold', fontsize = 12)
        # Adding Xticks
        
        plt.xlabel('Distance Metric', fontweight ='bold', fontsize = 12)
        plt.ylabel('Distance Value', fontweight ='bold', fontsize = 12)
        plt.xticks([r + barWidth*(len(janaka_list)-1)/2 for r in range(len(janaka_list[list(janaka_list.keys())[0]]))], [f"D(e)\nEuclidean\nDistance", f"D(bh)\nBhattacharya\nHellinger", f"D(kld)\nKullback-Leiber\nDivergence", f"D(js)\nJensen-Shannon\nDistance"], fontsize = 12)

        if ylim:
                plt.ylim(ylim[0], ylim[1])
        if bbox_shift == None:
                plt.legend(fontsize=legend_size, loc=legend_position)
        else:
                plt.legend(fontsize=legend_size, loc=legend_position, bbox_to_anchor=bbox_shift)
        final_fig = plt.gcf()
        plt.show()
        plt.draw()
        print(f"Plot saved to {file_name}.png")
        final_fig.savefig(file_name+".png", bbox_inches="tight", dpi=300)
        plt.close()

# ----------------------------------------------------------------

if __name__ == '__main__':
        print(filename)
        janaka_list = read_table_lcss(filename)
        print(janaka_list.keys())
        file_name = os.path.splitext(os.path.basename(filename))
        print(file_name[0])

        # not normalized
        color_flag = False
        plot_figure(barWidth, height, width, sym_list, color_list, color_flag, janaka_list, ylim, legend_size, legend_position, bbox_shift, plot_hline, 'plots/'+file_name[0])
        color_flag = True
        plot_figure(barWidth, height, width, sym_list, color_list_new, color_flag, janaka_list, ylim, legend_size, legend_position, bbox_shift, plot_hline, 'plots/'+file_name[0]+'_color')

        # normalized plots
        ylim = [0.0,1.0]
        # ylim = None
        legend_size = 12
        # legend_position = 'upper center'
        legend_position = 'upper right'
        # bbox_shift = [1.003, 1.01]
        bbox_shift = [1.0, 1.0]
        # bbox_shift = [1.22, 1.0]
        color_flag = False
        plot_hline = True

        plot_figure(barWidth, height, width, sym_list, color_list, color_flag, janaka_list, ylim, legend_size, legend_position, bbox_shift, plot_hline, 'plots/'+file_name[0]+'_nonorm')
        color_flag = True
        plot_figure(barWidth, height, width, sym_list, color_list_new, color_flag, janaka_list, ylim, legend_size, legend_position, bbox_shift, plot_hline, 'plots/'+file_name[0]+'_nonorm_color')

