def downsample2bins(timecoursedata,windowlength,nbins):
   
    """
    This function splits up timecourse data into average bins
   
    Input:
        -timecoursedata: your timecourse data
        -windowlength: length of the bin you want an average off [must be in the
        same frequency as the timecourse]
        -nbins: number of bins you want to average the data to
    Output:
        -list with the averages of each bin
   
    """
   
    # Check if lengths match up
    if len(timecoursedata)==windowlength*nbins:
   
        # Make an empty vector
        list_bins=[]
       
        # Window settings for the first bin
        start_pos=0
        end_pos=windowlength
       
        # Loop over the number of bins
        for c in range(0,nbins):
           
            if c==0:
               
                # For the firts bin take the average
                list_bins.append(np.average(timecoursedata[start_pos:end_pos]))
               
               
            else:
               
                # For all but first bin, use the updated window
                list_bins.append(np.average(timecoursedata[start_pos:end_pos]))
               
            # Update the window for the next round
            start_pos=end_pos+1
            end_pos=end_pos+windowlength
           
        return list_bins
   
    else:
       
        print('The length of your timecourse does not match the windowlength and nBins')
