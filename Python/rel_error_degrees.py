def rel_error_degrees(orig_degree, target_degree):
    
    # Get max and min
    max_val=np.maximum(orig_degree, target_degree)
    min_val=np.minimum(orig_degree, target_degree)
    
    # Get error both sides
    err1 = max_val - min_val
    err2 = (360 - max_val) + min_val
    
    rel_error=np.minimum(err1,err2)
    
    # Make relative degree
    if rel_error==err2: # Check if 360 was crossed
        
        # If it crossed 360 then make neg when target position is bigger
        if target_degree>orig_degree:
            rel_error = -rel_error
        
    else:
       
        # If it did not cross 360 then make neg when target position is smaller
        if target_degree<orig_degree:
            rel_error = -rel_error
        

    # Output
    return rel_error
