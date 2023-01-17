# -*- coding: utf-8 -*-
"""

Can be used after the matlab scripts that create the input .csv files, this script
makes the spm tables manuscript compatible for easy copy paste

@author: LdV2023
"""

# Libraries
import sys
import os
import glob
import pandas as pd
import numpy as np

# Settings
which_stats='cluster' # or 'peak'

# Get stat files
statspath="XXXX"
statfiles = glob.glob(os.path.join(statspath,'*.csv'))

replace_hdr=['setlevel_d',
 'setlevel_d_1',
 'clusterP_FWE',
 'clusterP_FDR',
 'voxnum',
 'clusterP_uncor',
 'peakP_FWE',
 'peakP_FDR',
 'T',
 'Z',
 'peakP_uncor',
 'x',
 'y',
 'z',
 'side']



# Loop over files anc create table for in the paper
for c_files in statfiles:
    
    # Read in csv file [SPM table]
    df = pd.read_csv(c_files)
    
    # Change header to remove symbols
    df.columns = replace_hdr
    
    # Cluster
    if which_stats=='cluster':
        
        # Final dataframe being saved
        table_hdr = ['Region', 'Side', 'X', 'Y', 'Z','mm3','ClusterP']
        row_names=['']*(len([val for val in df.clusterP_FWE if val<.05]))
        table_df = pd.DataFrame(index=row_names,columns = table_hdr)
        table_df.index.name=''
        
        # Loop over clusters
        a=0
        for c_cluster,n_cluster in enumerate(df.clusterP_FWE):
    
            # Only report clusters p<.05 FWE
            if n_cluster<.05:
                
                # Round to 3 decimals [or write <.001], other option is scientific notation: f'{n_cluster:.2e}'
                if df.clusterP_FWE[c_cluster]<.001:
                    clusterP_FWE='<0.001'
                elif np.isnan(df.clusterP_FWE[c_cluster]):
                    clusterP_FWE=''
                else:
                    clusterP_FWE=round(df.clusterP_FWE[c_cluster],3)
            
                # Add to table
                table_df.Region[a] = ''
                table_df.Side[a] = df.side[c_cluster]
                table_df.X[a] = df.x[c_cluster]
                table_df.Y[a] = df.y[c_cluster]
                table_df.Z[a] = df.z[c_cluster]
                table_df.mm3[a] = df.voxnum[c_cluster]*2*2*2
                table_df.ClusterP[a] = clusterP_FWE
                a = a+1
                
                # Save new table
                table_df.to_excel(c_files[:-4]+'_ManuscriptTable_Cluster.xlsx')
            
    # Peak
    if which_stats=='peak':
        
        # Final dataframe being saved
        table_hdr = ['Region', 'Side', 'X', 'Y', 'Z','PeakZ','PeakP']
        row_names=['']*(len([val for val in df.peakP_FWE if val<.05]))
        table_df = pd.DataFrame(index=row_names,columns = table_hdr)
        table_df.index.name=''
        
        # Loop over peaks       
        a=0
        for c_cluster,n_cluster in enumerate(df.peakP_FWE):
    
            # Only report clusters p<.05 FWE
            if n_cluster<.05:
                
                # Round to 3 decimals [or write <.001], other option is scientific notation: f'{n_cluster:.2e}'
                if df.peakP_FWE[c_cluster]<.001:
                    peakP_FWE='<0.001'
                else:
                    peakP_FWE=round(n_cluster,3)
            
            
                # Add to table
                table_df.Region[a] = ''
                table_df.Side[a] = df.side[c_cluster]
                table_df.X[a] = df.x[c_cluster]
                table_df.Y[a] = df.y[c_cluster]
                table_df.Z[a] = df.z[c_cluster]
                table_df.PeakZ[a] = df.Z[c_cluster]
                table_df.PeakP[a] = peakP_FWE
                a = a+1
                
                # Save new table
                table_df.to_excel(c_files[:-4]+'_ManuscriptTable_Peak.xlsx')     
