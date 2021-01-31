#Having a look at null values
##Is there any emty column?? Let´s see the percentage of null values for each column.
attack.isnull().sum().apply(lambda x: x/attack.shape[0]).sort_values(ascending=False)
## See if any row has all null values
attack.isnull().sum(axis=1).apply(lambda x: x/attack.shape[1]).sort_values(ascending=False)

# Find duplicate columns
def getDuplicateColumns(df): 
  
    # Create an empty set 
    duplicateColumnNames = set() 
      
    # Iterate through all the columns  
    # of dataframe 
    for x in range(df.shape[1]): 
          
        # Take column at xth index. 
        col = df.iloc[:, x] 
          
        # Iterate through all the columns in 
        # DataFrame from (x + 1)th index to 
        # last index 
        for y in range(x + 1, df.shape[1]): 
              
            # Take column at yth index. 
            otherCol = df.iloc[:, y] 
              
            # Check if two columns at x & y 
            # index are equal or not, 
            # if equal then adding  
            # to the set 
            if col.equals(otherCol): 
                duplicateColumnNames.add(df.columns.values[y]) 
                  
    # Return list of unique column names  
    # whose contents are duplicates. 
    return list(duplicateColumnNames)


## Regroup years into decades
def decade (year):
    dec=0
    if np.isnan(year) == True:
        dec = 0
    
    elif year%10 !=0:
       dec += (year - year%10)
    
    else:
        dec = year
    return dec
    
    #The output is the first year of the decade (Example: for 1987 the output is 1980). For
    #NaN values it returns "0"