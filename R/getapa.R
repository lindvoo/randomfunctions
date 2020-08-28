#apa format for afex:mixed model

getapa <- function (model) { 
  sum=summary(model)
  coef=sum$coefficients
  names_rows=labels(coef[,1])
  names_col=labels(coef[1,])
  nrows=length(names_rows)
  ncols=length(coef)/nrows
  
  for (i in 1:nrows){
    print(paste(names_rows[i],": ",
                "Estimate=",round(coef[i,1],3),
                ", SE=",round(coef[i,2],3),
                ", t(",round(coef[i,3],3),")=",round(coef[i,4],3),
                ", p=",round(coef[i,5],3)),sep="")
  }
}
