import numpy as np
import matplotlib.pyplot as plt

Raga_name = "Mohana"

# set width of bar
barWidth = 0.15
# set height and width of figure
height = 8
width = 6
# yaxis limits -- set ylim to None for default values
ylim = None
# ylim = [0,1]

sym_list = [".","//","o","\\","*"]
color_list = ["gray","darkgray","dimgray","lightgray"]

def read_table(filename):
        with open(filename, 'r') as fid:
                file_data = fid.readlines()
        janaka_list = {}
        for i in range(len(file_data)):
                if i == 0:
                        pass
                else:
                        line = file_data[i].strip().split('\t')
                        janaka_list[line[0]] = [float(j) for j in line[1:]]
        return janaka_list

def plot_figure(barWidth, height, width, sym_list, color_list, janaka_list, Raga_name, ylim):

        fig = plt.subplots(figsize =(height, width))

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
                barlist = plt.bar(br_list[i], janaka_list[raga_label], color = color_list[i], width = barWidth, edgecolor ='black', label = raga_label)
                for j in range(0, len(barlist)):
                        barlist[j].set_hatch(sym_list[sym_counter])
                sym_counter += 1
        
        plt.title(f'Distance of Raga {Raga_name} with Parent Ragas', fontweight ='bold', fontsize = 15)
        # Adding Xticks
        plt.xlabel('Distance Metric', fontweight ='bold', fontsize = 15)
        plt.ylabel('Distance Value', fontweight ='bold', fontsize = 15)
        plt.xticks([r + barWidth for r in range(len(janaka_list[list(janaka_list.keys())[0]]))], ['D(e)', 'D(bh)', 'D(kld)', 'D(js)'], fontsize = 12)

        if ylim:
                plt.ylim(ylim[0], ylim[1])
        plt.legend(fontsize=12)
        plt.show()

if __name__ == '__main__':
        filename = 'tables/table5_mohana.txt'
        janaka_list = read_table(filename)
        plot_figure(barWidth, height, width, sym_list, color_list, janaka_list, Raga_name, ylim)
