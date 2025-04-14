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
        #'isONclust2': 'tab:pink',
        'Rattle': 'tab:orange',
        'GeLuster': 'tab:red',
        'isONclust1': 'tab:green',
        'isONclust3_nc': 'tab:purple',
        'isONclust3_cm': 'tab:olive',
        'isONclust3_cm (1 core)': 'tab:olive',
        'isONclust2': 'tab:brown',
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
    ax.legend_.remove()
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', fontsize=17, color='black', xytext=(0, 30),
                    textcoords='offset points', rotation=90)
    #plt.title('Runtime for Each Tool and Dataset')  # Adjust title size if needed
    plt.xlabel('Dataset',fontsize=26)  # Set x-axis label font size to normal
    plt.ylabel('Runtime (hours)',fontsize=26)  # Set y-axis label font size to normal
    max_runtime = filtered_data['rt_hours'].max()
    #ax.set_ylim(0, max_runtime * 1.1) 
    ax.set_yscale('log')
    #ax.set_ylim(0, 70)
    #plt.legend(title='Tool', fontsize=20, title_fontsize=22)
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
        #'isONclust2': 'tab:pink',
        'Rattle': 'tab:orange',
        'GeLuster': 'tab:red',
        'isONclust1': 'tab:green',
        'isONclust3_nc': 'tab:purple',
        'isONclust3_cm': 'tab:olive',
        'isONclust3_cm (1 core)': 'tab:olive',
        'isONclust2': 'tab:brown',
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
    plt.figure(figsize=(15, 10))
    ax = sns.barplot(x='Dataset', y='Mem_usage(Gb)', hue='Tool', data=filtered_data, order=dataset_order, hue_order=tool_order, palette=palette, errorbar=None)
    ax.legend_.remove()
    ax.set_yscale('log')
    #sns.set(font_scale=2)
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.1f}', (p.get_x() + p.get_width() / 2.5, p.get_height()),
                    ha='center', va='center', fontsize=17, color='black', xytext=(0, 28),
                    textcoords='offset points', rotation=90)
    # Create legend handles and labels
    handles, labels = ax.get_legend_handles_labels()

    # Add a legend below the plot
    ax.legend(handles=handles, labels=labels, title="Tool", fontsize=20, title_fontsize=22, 
          loc='upper center', bbox_to_anchor=(0.4, -1.1), ncol=4)
    ax.set_ylim(0, 200)
    #plt.title('Memory Usage for Each Tool and Dataset')
    plt.xlabel('Dataset',fontsize=26)
    plt.ylabel('Memory Usage (GB)',fontsize=26)
    #plt.legend(title='Tool', bbox_to_anchor=(1.05, 1), loc='upper left')
    #plt.legend(title='Tool', fontsize=20, title_fontsize=22, loc= 'best')
    xtick_labels = ax.get_xticklabels()
    ytick_labels = ax.get_yticklabels()
    plt.setp(xtick_labels, fontfamily='serif', fontsize=26, weight='normal', color='black')
    plt.setp(ytick_labels, fontfamily='serif', fontsize=26, weight='normal', color='black')
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    #plt.subplots_adjust(bottom=0.6)
    plt.subplots_adjust(left=0.1, right=0.98, bottom=0.6)
    plt.savefig(os.path.join(outfolder, outfilename))
    plt.close()



def plot_seaborn_catplot(df, n_threads, outfolder):
    """
    Plots a seaborn catplot with bar plots in a 3x2 grid layout.
    Adds a single ground truth line per dataset for the '%reads' plot.

    Parameters:
    df (pd.DataFrame): DataFrame containing dataset information.
    n_threads (int): The number of threads to filter the data by.
    outfolder (str): Folder to save the plot.

    Returns:
    None
    """

    # Define color palette
    palette = {
        'isONclust3': 'tab:blue',
        'isONclust3 (1 core)': 'tab:blue',
        #'isONclust2': 'tab:pink',
        'Rattle': 'tab:orange',
        'GeLuster': 'tab:red',
        'isONclust1': 'tab:green',
        'isONclust3_nc': 'tab:purple',
        'isONclust3_cm': 'tab:olive',
        'isONclust3_cm (1 core)': 'tab:olive',
        'isONclust2': 'tab:brown',
        'isONclust3_sync_nc_pc': 'tab:cyan'
        # "strobealign_mixed" : 'magenta'
    }


    # Filter for the specified number of threads
    df_filtered = df[df['threads'] == n_threads].copy()

    # Normalize %reads
    df_filtered["%reads"] = df_filtered["%reads"] / 100

    outfilename = f"Measures_t{n_threads}.pdf"

    # Extract unique ground truth values for each dataset
    ground_truth = df_filtered.groupby("Dataset")["Clustered_reads"].first().to_dict()

    # Melt the DataFrame for plotting
    melted_data = pd.melt(df_filtered, id_vars=['Dataset', 'Tool'], value_vars=['V', 'c', 'h', 'ARI', '%reads'],
                          var_name='Measure', value_name='Value')

    sns.set(style="whitegrid")
    g = sns.catplot(
        data=melted_data,
        x='Measure',
        y='Value',
        hue='Tool',
        col='Dataset',
        kind='bar',
        height=4,
        aspect=1.2,
        col_wrap=3,
        palette=palette,
        legend=False
    )

     
    # Iterate over axes and add ground truth lines where needed
    for ax in g.axes.flat:
        dataset_name = ax.get_title().split('=')[-1].strip()
        ax.set_title(dataset_name, fontsize=24)

        # Debug: Check if the correct dataset and measure are matched
        #print(f"Plotting for dataset: {dataset_name}")
        #print(f"Measure on axis: {ax.get_xlabel()}")

        # Ensure ground truth is plotted **only** for '%reads'
        # Check the "Measure" column in the melted data to match `%reads`
        if dataset_name in ground_truth:
            gt_value = ground_truth[dataset_name]
            if "%reads" in melted_data[melted_data['Dataset'] == dataset_name]['Measure'].values:
                # Get the x-axis limits (in case they are not automatically set to the data range)
                x_min, x_max = ax.get_xlim()

                # Calculate the point where the ground truth line should start (slightly less than 1/5)
                start_x = x_max - (x_max - x_min) * 0.19  # Change from 0.2 to 0.25 for a shorter line

                # Plot the ground truth line only for the last 1/5 (or slightly shorter) of the x-axis range
                ax.axhline(y=gt_value, color='red', linestyle='--', linewidth=3, label='Ground Truth', xmin = start_x/x_max)

                
                
                
                #ax.axhline(y=gt_value, color='red', linestyle='--', linewidth = 4, label='Ground Truth')


        if ax.get_legend() is not None:
            ax.get_legend().remove()


    # Adjust legend
    handles, labels = g.axes[0].get_legend_handles_labels()
    red_line = plt.Line2D([0], [0], color='red', linestyle='--', linewidth=2)
    
    # Add ground truth to legend if not already present
    if "Ground Truth" not in labels:
        handles.append(red_line)
        labels.append('Ground Truth')

    g.fig.legend(handles=handles, labels=labels, title="Tool", fontsize=20, title_fontsize=22, loc='upper center',
                 bbox_to_anchor=(0.5, -0.05), ncol=4)

    plt.savefig(os.path.join(outfolder, outfilename), bbox_inches="tight")
    plt.close()


    
def compute_clustered_rate(tot_nr_reads, unclassified, singletons):
#(tot_nr_reads - unclassified - singleton_classes)/tot_nr_reads
    clustered_frac = (tot_nr_reads - unclassified - singletons)/tot_nr_reads
    return clustered_frac
    
    
    
# Read data from the TSV file
file_path = "/home/alexanderpetri/isONclust_analysis/Additional_results/full_results_paper_after_review.tsv"
outfolder= "/home/alexanderpetri/isONclust_analysis/Additional_results/"
df = pd.read_csv(file_path, sep='\t')
plot_rt(df,1)
plot_rt(df,8)
alz_rate = compute_clustered_rate(4277293,7367,12731)
droso_rate = compute_clustered_rate(3764977,492252,2157)
hg002_rate = compute_clustered_rate(37200651,640,45198) #compute_clustered_rate(
ont_human_rate = compute_clustered_rate(1473632,403049,15299)
ont_old_rate = compute_clustered_rate(283300,17853,6660)
SIM_rate = compute_clustered_rate(500000,0,1881)
SIRV_rate = compute_clustered_rate(1409565,15785,0)
pb_rate = compute_clustered_rate(5000000,735,11658)
print("ALZ_RATE: {0}".format(alz_rate))
dataset_rates = {
    "SIRV" : SIRV_rate,
    "Droso" : droso_rate,
    "ONT_human" : ont_human_rate,
    "ONT_old" : ont_old_rate,
    "SIM" : SIM_rate,
    "ALZ" : alz_rate,
    "HG002" : hg002_rate,
    "PB_humanSIRV" : pb_rate
}
#Adds a new column %reads which contains the contents of the dataset_rates dict
df["Clustered_reads"] = df["Dataset"].map(dataset_rates)
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


print(df.groupby("Dataset")["Clustered_reads"].unique())
plot_seaborn_catplot(df,1,outfolder)
plot_seaborn_catplot(df,8,outfolder)
#measures = ['V', 'c', 'h', 'ARI']
#for measure in measures:
# Set the order of tools for plotting

#plt.savefig(os.path.join(outfolder, "Total_Errors.pdf"))
#plt.close()
plt.show()
