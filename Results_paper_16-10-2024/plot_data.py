import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from datetime import timedelta

from numexpr import nthreads


# Define the function to parse time deltas
def parse_timedelta(time_str):
    # Convert 'd-h:m:s' format to timedelta
    parts = time_str.split('-')
    days = int(parts[0]) if len(parts) > 1 else 0
    h, m, s = map(int, parts[-1].split(':'))
    return timedelta(days=days, hours=h, minutes=m, seconds=s)


def plot_rt(data, n_threads):
    palette = {
        'isONclust3': 'tab:blue',
        'isONclust3 (1 core)': 'tab:blue',
        'Rattle': 'tab:orange',
        'GeLuster': 'tab:red',
        'isONclust1': 'tab:green',
        'isONclust3_nc': 'tab:purple',
        'isONclust3_min_nc_pc': 'tab:olive',
        'isONclust3_min_pc': 'tab:brown',
        'isONclust3_sync_nc_pc': 'tab:cyan'
        # "strobealign_mixed" : 'magenta'
    }

    # Filter data for the specified dataset or use all datasets if None
    filtered_data = data.loc[data['threads'] == n_threads].copy()
    print(filtered_data)
    # Convert 'rt(d-h:m:s)' to total seconds for easier plotting
    filtered_data['rt_timedelta'] = filtered_data['rt(d-h:m:s)'].apply(parse_timedelta)
    filtered_data['rt_hours'] = filtered_data['rt_timedelta'].dt.total_seconds() / 3600

    # Set the order of datasets and tools for plotting
    dataset_order = filtered_data['Dataset'].unique()
    tool_order = filtered_data['Tool'].unique()
    outfilename = "Runtimes_t"+str(n_threads)+".pdf"

    # Create a bar plot for runtime for each tool and dataset
    plt.figure(figsize=(15, 7))
    ax = sns.barplot(x='Dataset', y='rt_hours', hue='Tool', data=filtered_data, order=dataset_order, hue_order=tool_order,
                     palette=palette, errorbar=None)
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', fontsize=20, color='black', xytext=(0, 30),
                    textcoords='offset points', rotation=90)
    #plt.title('Runtime for Each Tool and Dataset')  # Adjust title size if needed
    plt.xlabel('Dataset',fontsize=26)  # Set x-axis label font size to normal
    plt.ylabel('Runtime (hours)',fontsize=26)  # Set y-axis label font size to normal

    ax.set_ylim(0, 70)
    plt.legend(title='Tool', fontsize=20, title_fontsize=22)
    xtick_labels = ax.get_xticklabels()
    ytick_labels = ax.get_yticklabels()
    plt.setp(xtick_labels, fontfamily='serif', fontsize=26, weight='normal', color='black')
    plt.setp(ytick_labels, fontfamily='serif', fontsize=26, weight='normal', color='black')
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(outfolder, outfilename))
    plt.close()


def plot_memory(data, n_threads):
    palette = {
        'isONclust3': 'tab:blue',
        'isONclust3 (1 core)': 'tab:blue',
        'Rattle': 'tab:orange',
        'GeLuster': 'tab:red',
        'isONclust1': 'tab:green',
        'isONclust3_nc': 'tab:purple',
        'isONclust3_min_nc_pc': 'tab:olive',
        'isONclust3_min_pc': 'tab:brown',
        'isONclust3_sync_nc_pc': 'tab:cyan'
        # "strobealign_mixed" : 'magenta'
    }
    # Filter data for the specified dataset or use all datasets if None
    filtered_data = data.loc[data['threads'] == n_threads].copy()
    outfilename="MemUsage_t"+str(n_threads)+".pdf"
    # Convert 'Mem_usage(Gb)' to numeric
    filtered_data['Mem_usage(Gb)'] = pd.to_numeric(filtered_data['Mem_usage(Gb)'], errors='coerce')

    # Set the order of datasets and tools for plotting
    dataset_order = filtered_data['Dataset'].unique()
    tool_order = filtered_data['Tool'].unique()

    # Create a bar plot for memory usage for each tool and dataset
    plt.figure(figsize=(15, 7))
    ax = sns.barplot(x='Dataset', y='Mem_usage(Gb)', hue='Tool', data=filtered_data, order=dataset_order, hue_order=tool_order, palette=palette, errorbar=None)
    #sns.set(font_scale=2)
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.1f}', (p.get_x() + p.get_width() / 2.5, p.get_height()),
                    ha='center', va='center', fontsize=20, color='black', xytext=(0, 28),
                    textcoords='offset points', rotation=90)
    ax.set_ylim(0, 200)
    #plt.title('Memory Usage for Each Tool and Dataset')
    plt.xlabel('Dataset',fontsize=26)
    plt.ylabel('Memory Usage (GB)',fontsize=26)
    #plt.legend(title='Tool', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.legend(title='Tool', fontsize=20, title_fontsize=22)
    xtick_labels = ax.get_xticklabels()
    ytick_labels = ax.get_yticklabels()
    plt.setp(xtick_labels, fontfamily='serif', fontsize=26, weight='normal', color='black')
    plt.setp(ytick_labels, fontfamily='serif', fontsize=26, weight='normal', color='black')
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(outfolder, outfilename))
    plt.close()


def plot_seaborn_catplot(df,n_threads):
    """
    This function takes a DataFrame `df` and plots a seaborn catplot with bar plots
    in a 3x2 grid layout.

    Parameters:
    df (pd.DataFrame): DataFrame containing the dataset information, including columns for
                       'Dataset', 'Tool', 'V', 'c', 'h', 'ARI'.

    Returns:
    None: This function only plots the graph.
    """
    palette = {
        'isONclust3': 'tab:blue',
        'isONclust3 (1 core)': 'tab:blue',
        'Rattle': 'tab:orange',
        'GeLuster': 'tab:red',
        'isONclust1': 'tab:green',
        'isONclust3_nc': 'tab:purple',
        'isONclust3_min_nc_pc': 'tab:olive',
        'isONclust3_min_pc': 'tab:brown',
        'isONclust3_sync_nc_pc': 'tab:cyan'
        # "strobealign_mixed" : 'magenta'
    }
    df_filtered = df[df['threads'] == n_threads]
    outfilename = "Measures_t"+str(n_threads)+".pdf"
    # Melt the DataFrame to have 'Dataset' and 'Tool' as id_vars, and the rest as value_vars
    melted_data = pd.melt(df_filtered,
                          id_vars=['Dataset', 'Tool'],
                          value_vars=['V', 'c', 'h', 'ARI'],
                          var_name='Measure',
                          value_name='Value')

    # Plot using seaborn catplot
    sns.set(style="whitegrid")  # Set the style of seaborn plots
    g = sns.catplot(
        data=melted_data,
        x='Measure',
        y='Value',
        hue='Tool',  # Use 'Tool' for coloring
        col='Dataset',  # Separate plots for each 'Dataset'
        kind='bar',
        height=4,
        aspect=1.2,
        col_wrap=3,
        palette=palette,# Set the number of columns to 3 for a 3x2 layout

    )

    # Set axis labels and plot title
    g.set_axis_labels("Measure", "Value",fontsize=20)

    for ax in g.axes.flat:
        # Modify the title text
        title = ax.get_title()
        # Assuming the prefix 'Dataset=' should be removed
        new_title = title.split('Dataset =')[-1]  # Remove prefix
        ax.set_title(new_title, fontsize=24)
        #g.fig.suptitle("Bar Plots of Measures by Tool and Dataset", y=1.03)

    for ax in g.axes.flatten():
        ax.tick_params(axis='x', labelsize=20)  # Adjust x-axis label size
        ax.tick_params(axis='y', labelsize=20)  # Adjust y-axis label size
        ax.set_ylabel("Value", fontsize=20)

        # Rotate x-axis labels for better readability

    # Adjust the legend
    # Ensure the legend is displayed
    #g.legend(fontsize=14)
    plt.setp(g.legend.get_texts(), fontsize='20')  # for legend text
    plt.setp(g.legend.get_title(), fontsize='22')
    g.legend.set_title("Tool")
    g.legend.set_bbox_to_anchor((1., 0.45))  # Adjust legend position
    g.legend.set_frame_on(True)
    #plt.show()
    plt.savefig(os.path.join(outfolder, outfilename))
    plt.close()

def plot_all_data(df):
    palette = {
        'isONclust3': 'tab:blue',
        'isONclust3 (1 core)': 'tab:blue',
        'Rattle': 'tab:orange',
        'GeLuster': 'tab:red',
        'isONclust1': 'tab:green',
        'isONclust3_nc': 'tab:purple',
        'isONclust3_min_nc_pc': 'tab:olive',
        'isONclust3_min_pc': 'tab:brown',
        'isONclust3_sync_nc_pc': 'tab:cyan'
        # "strobealign_mixed" : 'magenta'
    }

    melted_data = pd.melt(df, id_vars=['Dataset', 'Tool'], value_vars=['V', 'c', 'h', 'ARI'], var_name= 'Measure',
                          value_name='Value')
    # Convert 'Value' column to float
    melted_data['Value'] = melted_data['Value'].astype(float)
    tool_order = df['Tool'].unique()
    g = sns.catplot(
         x='Measure', y="Value", col='Dataset',data=melted_data, hue_order= tool_order,
                order=['V', 'c', 'h', 'ARI'],
        kind="bar", height=4, aspect=.8,)
    plt.xlabel('Measure')
    plt.ylabel('Value')
    plt.legend(title='Tool', loc='lower left')
    plt.tight_layout()
    # plt.show()

    plt.close()
def plot_dataset(dataset_name,data,outfolder):
    palette = {
        'isONclust3': 'tab:blue',
        'isONclust3 (1 core)': 'tab:blue',
        'Rattle': 'tab:orange',
        'GeLuster': 'tab:red',
        'isONclust1': 'tab:green',
        'isONclust3_nc': 'tab:purple',
        'isONclust3_min_nc_pc': 'tab:olive',
        'isONclust3_min_pc': 'tab:brown',
        'isONclust3_sync_nc_pc': 'tab:cyan'
        # "strobealign_mixed" : 'magenta'
    }

    outfilename = dataset_name + ".pdf"
    tool_order = data['Tool'].unique()
    # Melt the dataframe to have a separate row for each measure, making it easier to plot
    # Melt the dataframe to have a separate row for each measure, making it easier to plot
    melted_data = pd.melt(data, id_vars=['Tool'], value_vars=['V', 'c', 'h', 'ARI'], var_name='Measure',
                               value_name='Value')
    # Convert 'Value' column to float
    melted_data['Value'] = melted_data['Value'].astype(float)
    # Create a grouped bar plot for each measure with colored bars for each tool
    plt.figure(figsize=(17, 10))
    sns.barplot(x='Measure', y='Value', hue='Tool', data=melted_data, hue_order=tool_order,
                order=['V', 'c', 'h', 'ARI'], palette=palette, errorbar=None )
    #sns.set(font_scale=3)
    plt.title(dataset_name)
    # Set y-axis limits
    # plt.ylim(0, 1)
    plt.xlabel('Measure')
    plt.ylabel('Value')
    plt.legend(title='Tool', loc='lower left', fontsize=20)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    #plt.show()
    plt.savefig(os.path.join(outfolder, outfilename))
    plt.close()

# Read data from the TSV file
file_path = "~/isONclust_analysis/Results_not_pushed/full_results_paper_reduced_new.tsv"
outfolder= "/home/alexanderpetri/isONclust_analysis/Results_not_pushed/"
df = pd.read_csv(file_path, sep='\t')
plot_rt(df,1)
plot_rt(df,8)
# Remove quotes and spaces from the 'rt(d-h:m:s)' column
#df['rt(d-h:m:s)'] = df['rt(d-h:m:s)'].str.strip().str.strip('"')

# Convert 'rt(d-h:m:s)' to total seconds for easier plotting
#df['rt_seconds'] = pd.to_timedelta(df['rt(d-h:m:s)']).dt.total_seconds()
print(df)
plot_memory(df,1)
plot_memory(df,8)
# Create separate plots for each dataset and tool
datasets = df['Dataset'].unique()

# Identify unique tools in the dataset
tools = df['Tool'].unique()

# Filter data for the 'SIRV' dataset
#sirv_data = df[df['Dataset'] == 'SIRV']
#alz_data = df[df['Dataset'] == 'ALZ']
#sim_data = df[df['Dataset'] == 'SIM']
#ont_data = df[df['Dataset'] == 'ONT_human']
#dro_data = df[df['Dataset'] == 'Droso']
#hg_data = df[df['Dataset'] == 'HG002']
#plot_dataset("SIRV", sirv_data,outfolder)
#plot_dataset("ALZ", alz_data,outfolder)
#plot_dataset("SIM-500k", sim_data,outfolder)
#plot_dataset("ONT",ont_data,outfolder)
#plot_dataset("Drosophila", dro_data,outfolder)
#plot_dataset("HG002", hg_data,outfolder)

#plot_all_data(df)
plot_seaborn_catplot(df,1)
plot_seaborn_catplot(df,8)
#measures = ['V', 'c', 'h', 'ARI']
#for measure in measures:
# Set the order of tools for plotting

#plt.savefig(os.path.join(outfolder, "Total_Errors.pdf"))
#plt.close()
plt.show()
