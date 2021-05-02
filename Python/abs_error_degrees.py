def abs_error_degrees(orig_degree, target_degree):
    
    # Get max and min
    max_val=np.maximum(orig_degree, target_degree)
    min_val=np.minimum(orig_degree, target_degree)
    
    # Get error both sides
    err1 = max_val - min_val
    err2 = (360 - max_val) + min_val
    
    abs_error=np.minimum(err1,err2)
    
    return abs_error
