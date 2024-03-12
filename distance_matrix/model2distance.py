import argparse
import pandas as pd
from scipy.spatial import distance_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Parsing command line arguments for input and output file paths
parser = argparse.ArgumentParser(description='Process 3D genome data.')
parser.add_argument('-i', '--input', required=True, help='Base input file path for .dim 
files')
parser.add_argument('-o', '--output', required=True, help='Base output file path for .txt 
files')
args = parser.parse_args()

chromosomes = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7',
               'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14',
               'chr15', 'chr16', 'chr17', 'chr18', 'chr19']

dist_maps = []  # This will store the cis distance maps for every chromosome

for chromosome in chromosomes:
    input_file = f"{args.input}/{chromosome}.dim"  # Input .dim files
    
    # Load the .dim file into a pandas dataframe and name the columns
    df_3dg = pd.read_csv(input_file, header=None, delimiter="\t", names=['chr', 'locus', 'x', 
'y', 'z'])
    
    # Extract only those 3d coordinates for the particular chromosome
    df_mat = df_3dg[df_3dg['chr'] == chromosome + '(mat)']
    df_pat = df_3dg[df_3dg['chr'] == chromosome + '(pat)']
    
    # Merge the mat and pat files on common locus values
    df = pd.merge(df_mat, df_pat, how='inner', on=['locus'])
    
    # Get only the x, y, z coordinates
    df_coords_mat = df.iloc[:, 2:5].values
    df_coords_pat = df.iloc[:, 6:9].values
    
    # Use the distance_matrix function to get the distance matrix for the chromosome
    dist_matrix = distance_matrix(df_coords_mat, df_coords_pat)
    
    # Append the distance matrices from all chromosomes
    dist_maps.append(dist_matrix)
    
    # Save each distance matrix with a prefix indicating the chromosome number, as a 
tab-separated .txt file
    output_filename = f"{args.output}_chromosome_{chromosome}_distance_matrix.txt"
    pd.DataFrame(dist_matrix).to_csv(output_filename, sep='\t', index=False, header=False)

# Plotting the cis distance maps for all chromosomes
fig_size = [20, 4]
plt.rcParams["figure.figsize"] = fig_size
plt.rcParams.update({'font.size': 10})

fig = plt.figure()
for i, dist_map in enumerate(dist_maps, start=1):
    ax = fig.add_subplot(2, 10, i)
    sns.heatmap(dist_map, cmap="coolwarm", cbar=False, xticklabels=False, yticklabels=False)
    ax.xaxis.set_ticklabels([])
    ax.yaxis.set_ticklabels([])

plt.show()

