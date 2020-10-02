#Initialize array     
arr = [5, 2, 8, 7, 1];     


#Displaying elements of original array    
print("Elements of original array: ");    
for i in range(0, len(arr)):     
    print(arr[i]),    

def descendingOrder( arr ):

    temp = 0;    
    newArr = arr[:]
    for i in range(0, len(newArr)):    
        for j in range(i+1, len(newArr)):    
            if(newArr[i] < newArr[j]):    
                temp = newArr[i];    
                newArr[i] = newArr[j];    
                newArr[j] = temp; 
            
    return newArr
            
def ascendingOrder( arr ):

    newArray = arr[:]
    newArray.sort()      
    
    return newArray

     
#Sort the array in descending order    
 
asc = ascendingOrder( arr ) 
desc = descendingOrder( arr )
     
#Displaying elements of array after sorting    
print("Elements of array sorted in ascending order: ");    
for i in range(0, len(asc)):     
    print(asc[i]),
    
#Displaying elements of array after sorting    
print("Elements of array sorted in descending order: ");    
for i in range(0, len(desc)):     
    print(desc[i]),    
