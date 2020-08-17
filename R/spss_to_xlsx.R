#-----------------------------------------------------------------------------------------
#
# Converts spss file to an excel file
#
#LdV2020
#-----------------------------------------------------------------------------------------

# Clear
rm(list = ls())

# Load SPSS file
library(foreign)
library("writexl")

# Select file
datafile = file.choose()
datapath = dirname(datafile)
datafilename = basename(datafile)

# Read in data
dataset = read.spss(datafile, to.data.frame=TRUE)

# Save to Excel
origstr=tools::file_path_sans_ext(datafilename)
write_xlsx(dataset,file.path(datapath, paste(origstr,"spssfile_in_excel.xlsx",sep="_")))
