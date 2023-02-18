"""
Code to plot tables to normalized bar plot
JNMR paper tables

Histogram plots of LCSS table 2

Author: Jom Kuriakose
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# ----------------------------------------------------------------

filename = 'tables_lcss/Table2_LCSS.txt'
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

between_bar_width = 0.5

# set width of bar
# barWidth = 0.18
# barWidth = 0.15
# barWidth = 0.12
# barWidth = 0.10
# barWidth = 0.08
# barWidth = 0.06
barWidth = 0.04
# bbox_shift = [1, 1]

# set height and width of figure
height = 4
# height = 6
# width = 6
# width = 8
width = 10
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

        fig, axes = plt.subplots(figsize =(width, height))

        if plot_hline:
                # hline_loc = [1.0, 0.8, 0.6, 0.4, 0.2]
                # hline_loc = [1.0, 0.7, 0.4]
                hline_loc = [1.0, 0.6, 0.2]
                for i in range(0,len(hline_loc)):
                        plt.axhline(y=hline_loc[i], color='grey', linestyle='--')

        # Set position of bar on X axis
        janya_keys = list(janaka_list.keys())
        xaxis_list = []
        janya_label_list = []
        prev_end_position = 0
        curr_end_position = 0
        full_bar_list = []
        full_legend_lab_list = []
        for i in range(0, len(janya_keys)):
                sym_counter = 0
                prev_end_position = curr_end_position
                bar_list = []
                for j in range(0, len(janaka_list[janya_keys[i]]["LCSS_dist"])):
                        # print()
                        janaka_name = janaka_list[janya_keys[i]]["Janaka_list"][j]
                        if parent_lab in janaka_name:
                                barobj = axes.bar(curr_end_position, janaka_list[janya_keys[i]]["LCSS_dist"][j], color = 'black', width = barWidth, edgecolor ='gray', label = janaka_name)
                                bar_list.append(barobj)
                        else:
                                barobj = axes.bar(curr_end_position, janaka_list[janya_keys[i]]["LCSS_dist"][j], color = color_list[j], width = barWidth, edgecolor ='black', label = janaka_name)
                                bar_list.append(barobj)
                                # print(f"barobj: {barobj}")
                                if not color_flag:
                                        for k in range(0, len(barobj)):
                                                barobj[k].set_hatch(sym_list[sym_counter])
                        curr_end_position += barWidth
                        sym_counter += 1
                full_bar_list.append(bar_list)
                full_legend_lab_list.append(janaka_list[janya_keys[i]]["Janaka_list"])
                xaxis_list.append(prev_end_position+((curr_end_position-prev_end_position)/2)-(barWidth/2))
                curr_end_position += between_bar_width
                janya_label_list.append(janya_keys[i])
        
        # plt.title(f'LCSS Score of Janya Ragas with Janaka Ragas', fontweight ='bold', fontsize = 12)
        # Adding Xticks
        
        plt.xlabel('Janya Raga', fontweight ='bold', fontsize = 12)
        plt.ylabel('LCSS Score', fontweight ='bold', fontsize = 12)
        plt.xticks(xaxis_list, janya_label_list, fontsize = 12)

        if ylim:
                plt.ylim(ylim[0], ylim[1])
        
        # if bbox_shift == None:
        #         plt.legend(fontsize=legend_size, loc=legend_position)
        # else:
        #         plt.legend(fontsize=legend_size, loc=legend_position, bbox_to_anchor=bbox_shift)

        # print(f"full_bar_list: {full_bar_list}")
        # Table1
        x_axis_loc = [0.38, 0.62, 0.9]
        y_axis_loc = [0.4, 0.4, 0.5]
        for i in range(0,len(full_bar_list)):
                # print(f"full_bar_list[i]: {full_bar_list[i]}, full_legend_lab_list[i]: {full_legend_lab_list[i]}")
                # print(f"(i+1)*(1/len(full_bar_list)): {(i+1)*(1/len(full_bar_list))}")
                fig.legend(full_bar_list[i], full_legend_lab_list[i], fontsize=12, loc=7, bbox_to_anchor=(x_axis_loc[i], y_axis_loc[i]))

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

