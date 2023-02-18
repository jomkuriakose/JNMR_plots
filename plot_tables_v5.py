"""
Code to plot tables to normalized bar plot
JNMR paper tables

Histogram plots of single parent ragas

Author: Jom Kuriakose
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# ----------------------------------------------------------------

# filename = 'tables/Table0_Test.txt'
# Raga_name = None
# parent_lab = "(*)"

filename = 'tables/Table3and4.txt'
Raga_name = None
parent_lab = "(*)"

# filename = 'tables/Table3_Aarabhi.txt'
# Raga_name = "Aarabhi"
# parent_lab = "(*)"

# filename = 'tables/Table3_Khamboji.txt'
# Raga_name = "Khamboji"
# parent_lab = "(*)"

# filename = 'tables/Table3_Anandabhairavi.txt'
# Raga_name = "Anandabhairavi"
# parent_lab = "(*)"

# filename = 'tables/Table3_Begada.txt'
# Raga_name = "Begada"
# parent_lab = "(*)"

# filename = 'tables/Table3_Khamas.txt'
# Raga_name = "Khamas"
# parent_lab = "(*)"

# ----------------------------------------------------------------

# filename = 'tables/Table4_Sriranjani.txt'
# Raga_name = "Sriranjani"
# parent_lab = "(*)"

# filename = 'tables/Table4_Chandrajyoti.txt'
# Raga_name = "Chandrajyoti"
# parent_lab = "(*)"

# filename = 'tables/Table4_Malahari.txt'
# Raga_name = "Malahari"
# parent_lab = "(*)"

# ----------------------------------------------------------------

# filename = 'tables/Table5_Hindola.txt'
# Raga_name = "Hindola"
# parent_lab = "(*)"

# filename = 'tables/Table5_Sunadavinodini.txt'
# Raga_name = "Sunadavinodini"
# parent_lab = "(*)"

# filename = 'tables/Table5_Madhyamavati.txt'
# Raga_name = "Madhyamavati"
# parent_lab = "(*)"

# filename = 'tables/Table5_Mohana.txt'
# Raga_name = "Mohana"
# parent_lab = "(*)"

# ----------------------------------------------------------------

# filename = 'tables/Table6_Revati.txt'
# Raga_name = "Revati"
# parent_lab = "(*)"

# filename = 'tables/Table6_Hamsadwani.txt'
# Raga_name = "Hamsadwani"
# parent_lab = "(*)"

# ----------------------------------------------------------------

# filename = 'tables/Table7_Gambhiranata.txt'
# Raga_name = "Gambhiranata"
# parent_lab = "(**)"

# filename = 'tables/Table7_Amritavarshini.txt'
# Raga_name = "Amritavarshini"
# parent_lab = "(*)"

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
width = 12
# width = 8
# width = 10
# width = 12

# ----------------------------------------------------------------

sym_list = [".","//","o","\\","x","..","xx",".O","++"]
color_list = ["gainsboro","gray","darkgray","dimgray","lightgray","grey","darkgrey","dimgrey","lightgrey"]
color_list_new = list(mcolors.TABLEAU_COLORS.values())

# ----------------------------------------------------------------

def read_table(filename):
        with open(filename, 'r') as fid:
                file_data = fid.readlines()
        janaka_list = {}
        norm_janaka_list = {}
        janaka_arr = []
        for i in range(len(file_data)):
                if i == 0:
                        pass
                else:
                        line = file_data[i].strip().split('\t')
                        janaka_list[line[0].strip()] = [float(j) for j in line[1:]]
                        janaka_arr.append([float(j) for j in line[1:]])
        janaka_arr = np.array(janaka_arr)
        # normalize by the max value in each column
        janaka_arr = janaka_arr / janaka_arr.max(axis=0)
        janaka_list_keys = list(janaka_list.keys())
        for i in range(0,len(janaka_list_keys)):
                norm_janaka_list[janaka_list_keys[i]] = list(janaka_arr[i])
        return janaka_list, norm_janaka_list

# ----------------------------------------------------------------

def plot_figure(barWidth, height, width, sym_list, color_list, color_flag, janaka_list, Raga_name, ylim, legend_size, legend_position, bbox_shift, plot_hline, file_name):

        fig, ax = plt.subplots(figsize =(width, height))

        # Set position of bar on X axis
        br_list = []
        for i in range(0,len(janaka_list)):
                if i == 0:
                        br_list.append(np.arange(len(janaka_list[list(janaka_list.keys())[0]])))
                else:
                        br_list.append([x + barWidth for x in br_list[i-1]])
        
        sym_counter = 0

        if plot_hline:
                # hline_loc = [1.0, 0.8, 0.6, 0.4, 0.2]
                # hline_loc = [1.0, 0.7, 0.4]
                hline_loc = [1.0, 0.6, 0.2]
                for i in range(0,len(hline_loc)):
                        plt.axhline(y=hline_loc[i], color='grey', linestyle='--')

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
        
        if not Raga_name == None:
                plt.title(f'Distance of Raga {Raga_name} with Parent Ragas', fontweight ='bold', fontsize = 12)
        else:
                plt.title(f'Janya Ragas with only one possible Parent Raga', fontweight ='bold', fontsize = 12)
        # Adding Xticks
        
        plt.xlabel('Janya Raga', fontweight ='bold', fontsize = 12)
        plt.ylabel('Distance Value', fontweight ='bold', fontsize = 12)
        # plt.xticks([r + barWidth*(len(janaka_list)-1)/2 for r in range(len(janaka_list[list(janaka_list.keys())[0]]))], [f"D(e)\nEuclidean\nDistance", f"D(bh)\nBhattacharya-Hellinger\nDistance", f"D(kld)\nKullback-Leiber\nDivergence", f"D(js)\nJensen-Shannon\nDistance"], fontsize = 8)
        # plt.xticks([r + barWidth*(len(janaka_list)-1)/2 for r in range(len(janaka_list[list(janaka_list.keys())[0]]))], [f"Janya: Aarabhi\nJanaka: 29. Shankarabharana", f"Janya: Khamboji\nJanaka: 28. Harikambhoji", f"Janya: Begada\nJanaka: 29. Shankarabharana", f"Janya: Khamas\nJanaka: 28. Harikambhoji", f"Janya: Sriranjani\nJanaka: 22. Kharaharapriya"], fontsize = 10)
        # plt.xticks([r + barWidth*(len(janaka_list)-1)/2 for r in range(len(janaka_list[list(janaka_list.keys())[0]]))], [f"Janya:\nAarabhi\nJanaka:\n29. Shankarabharana", f"Janya:\nKhamboji\nJanaka:\n28. Harikambhoji", f"Janya:\nBegada\nJanaka:\n29. Shankarabharana", f"Janya:\nKhamas\nJanaka:\n28. Harikambhoji", f"Janya:\nSriranjani\nJanaka:\n22. Kharaharapriya"], fontsize = 12)
        plt.xticks([r + barWidth*(len(janaka_list)-1)/2 for r in range(len(janaka_list[list(janaka_list.keys())[0]]))], [f"Aarabhi", f"Khamboji", f"Begada", f"Khamas", f"Sriranjani"], fontsize = 12)

        textstr_list = [f"29. Shankarabharana", f"28. Harikambhoji", f"29. Shankarabharana", f"28. Harikambhoji", f"22. Kharaharapriya"]
        props = dict(boxstyle='square', facecolor='white', alpha=0.5)
        # box_locs = [r + barWidth*(len(janaka_list)-1)/2 for r in range(len(janaka_list[list(janaka_list.keys())[0]]))]
        box_locs = [0.01, 0.2, 0.4, 0.62, 0.8]
        v_locs = [0.65, 0.47, 0.4, 0.36, 0.42]
        for idx in range(0,len(box_locs)):
                plt.text(box_locs[idx], v_locs[idx], textstr_list[idx], transform=ax.transAxes, fontsize=12, verticalalignment='top', bbox=props)

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
        janaka_list, norm_janaka_list = read_table(filename)
        print(janaka_list.keys())
        file_name = os.path.splitext(os.path.basename(filename))
        print(file_name[0])

        # not normalized
        color_flag = False
        plot_figure(barWidth, height, width, sym_list, color_list, color_flag, janaka_list, Raga_name, ylim, legend_size, legend_position, bbox_shift, plot_hline, 'plots/'+file_name[0])
        color_flag = True
        plot_figure(barWidth, height, width, sym_list, color_list_new, color_flag, janaka_list, Raga_name, ylim, legend_size, legend_position, bbox_shift, plot_hline, 'plots/'+file_name[0]+'_color')

        # normalized plots
        ylim = [0.0,1.0]
        # ylim = None
        legend_size = 12
        # legend_position = 'upper center'
        legend_position = 'upper right'
        # bbox_shift = [1.003, 1.01]
        bbox_shift = [1.0, 1.0]
        color_flag = False
        plot_hline = True

        plot_figure(barWidth, height, width, sym_list, color_list, color_flag, norm_janaka_list, Raga_name, ylim, legend_size, legend_position, bbox_shift, plot_hline, 'plots/'+file_name[0]+'_norm')
        color_flag = True
        plot_figure(barWidth, height, width, sym_list, color_list_new, color_flag, norm_janaka_list, Raga_name, ylim, legend_size, legend_position, bbox_shift, plot_hline, 'plots/'+file_name[0]+'_norm_color')

        # normalized plots
        ylim = [0.0,1.0]
        # ylim = None
        legend_size = 12
        # legend_position = 'upper center'
        legend_position = 'upper right'
        # bbox_shift = [1.003, 1.01]
        bbox_shift = [1.0, 1.0]
        color_flag = False
        plot_hline = True

        plot_figure(barWidth, height, width, sym_list, color_list, color_flag, janaka_list, Raga_name, ylim, legend_size, legend_position, bbox_shift, plot_hline, 'plots/'+file_name[0]+'_nonorm')
        color_flag = True
        plot_figure(barWidth, height, width, sym_list, color_list_new, color_flag, janaka_list, Raga_name, ylim, legend_size, legend_position, bbox_shift, plot_hline, 'plots/'+file_name[0]+'_nonorm_color')
