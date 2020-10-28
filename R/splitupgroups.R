splitupgroups <- function (var,nsplits) { 

# Split a vector up in equal groups [for example to perform a split-half analysis]
  
  if (nsplits==1) {
    
    print("You should have more than 1 group") 
    
  } else if (nsplits>NROW(var)){
    
    print("You cannot make more groups than the length of your data")
    
  } else{
  
    newvar=var
    
    #sort
    sort_var=sort(var)
    
    #split up in chunks
    spltvar=split(sort_var, cut(seq_along(sort_var), nsplits, labels = FALSE))
    
    #get crucial values to split up with
    vec <- vector()
    for (i in 1:NROW(spltvar)){
      
      vec[i]=tail(as.vector(unlist(spltvar[i])), n=1)
      
    }
    
    #n-1 groups
    for (i in 1:(NROW(vec)-1)){
      
      newvar[newvar<vec[i]]=paste(c("Gr", i), collapse = "")
      
    }
    
    #last group
    newvar[newvar<=vec[i+1]]=paste(c("Gr", i+1), collapse = "")
    
    return(newvar)
    
  } 
  
}
