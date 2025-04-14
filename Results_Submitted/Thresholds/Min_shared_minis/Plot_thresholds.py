import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from datetime import timedelta
def plot_dataset_new(dataset_name, data, outfolder):
    print(data)
    outfilename = dataset_name + "_T.pdf"
    
    # Melt the dataframe to have a separate row for each measure, making it easier to plot
    melted_data = pd.melt(data, id_vars=['Threshold'], value_vars=['V', 'c', 'h', 'ARI'], var_name='Measure', value_name='Value')
    
    # Convert 'Value' column to float
    melted_data['Value'] = melted_data['Value'].astype(float)
    
    # Create the plot
    plt.figure(figsize=(15, 8))
    g = sns.lineplot(x='Threshold', y='Value', hue='Measure', data=melted_data, linewidth=3, marker='o', markersize=12)
    
    # Set title with larger font size
    plt.title(dataset_name, fontsize=32)
    
    # Set axis labels with larger font sizes
    plt.xlabel('$T_2$', fontsize=30)
    plt.ylabel('Cluster measures', fontsize=30)
    
    # Customize tick label font size
    plt.xticks(fontsize=28, rotation=45, ha='right')
    plt.yticks(fontsize=28)
    
    # Customize the legend font size and title font size
    plt.legend(title='Measure', loc='upper left', fontsize=28, title_fontsize=30)
    
    # Adjust layout to prevent overlap of elements
    plt.tight_layout()
    
    # Save the plot as a PDF in the specified output folder
    plt.savefig(os.path.join(outfolder, outfilename))
    
    # Close the plot to free up memory
    plt.close()
    
def plot_dataset(dataset_name,data,outfolder):
    print(data)
    outfilename = dataset_name + ".pdf"
    #tool_order = data['Tool'].unique()
    # Melt the dataframe to have a separate row for each measure, making it easier to plot
    # Melt the dataframe to have a separate row for each measure, making it easier to plot
    melted_data = pd.melt(data, id_vars=['Threshold'], value_vars=['V', 'c', 'h', 'ARI'], var_name='Measure',
                               value_name='Value')
    # Convert 'Value' column to float
    melted_data['Value'] = melted_data['Value'].astype(float)
    # Create a grouped bar plot for each measure with colored bars for each tool
    plt.figure(figsize=(15, 8))
    sns.lineplot(x='Threshold', y='Value', hue='Measure', data=melted_data)#,
                #order=['V', 'c', 'h', 'ARI'] )
    plt.title(dataset_name)
    # Set y-axis limits
    # plt.ylim(0, 1)
    plt.xlabel('Measure')
    plt.ylabel('Value')
    plt.legend(title='Dataset', loc='upper left')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    #plt.show()
    plt.savefig(os.path.join(outfolder, outfilename))
    plt.close()

# Read data from the TSV file
file_path = "~/isONclust_analysis/Results_paper_16-10-2024/Thresholds/Thresholds.txt"
outfolder= "/home/alexanderpetri/isONclust_analysis/Additional_results/Thresholds/Min_shared_minis/"
df = pd.read_csv(file_path, sep='\t')
#plot_rt(df)
# Remove quotes and spaces from the 'rt(d-h:m:s)' column
#df['rt(d-h:m:s)'] = df['rt(d-h:m:s)'].str.strip().str.strip('"')

# Convert 'rt(d-h:m:s)' to total seconds for easier plotting
#df['rt_seconds'] = pd.to_timedelta(df['rt(d-h:m:s)']).dt.total_seconds()
print(df)
#plot_memory(df)

# Create separate plots for each dataset and tool
datasets = df['Dataset'].unique()

# Identify unique tools in the dataset
#tools = df['Tool'].unique()

# Filter data for the 'SIRV' dataset
#sirv_data = df[df['Dataset'] == 'SIRV']
alz_data = df[df['Dataset'] == 'ALZ']
#sim_data = df[df['Dataset'] == 'SIM-500k']
#ont_data = df[df['Dataset'] == 'ONT_Orig']
onth_data =df[df['Dataset'] == 'ONTh']
dro_data = df[df['Dataset'] == 'Droso']
#plot_dataset("SIRV", sirv_data,outfolder)
plot_dataset_new("ALZ", alz_data,outfolder)
plot_dataset_new("ONTh", onth_data,outfolder)
#plot_dataset("SIM-500k", sim_data,outfolder)
#plot_dataset("ONT",ont_data,outfolder)
plot_dataset_new("Drosophila", dro_data,outfolder)
#measures = ['V', 'c', 'h', 'ARI']
#for measure in measures:
# Set the order of tools for plotting

#plt.savefig(os.path.join(outfolder, "Total_Errors.pdf"))
#plt.close()
plt.show()
