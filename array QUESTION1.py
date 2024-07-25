# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr, n):
        
        if n == 1 :
            return 0
        
        low = 0 
        high = n -1 
        
        while low <= high:
            mid = (low + high) // 2 

            if mid == 0 and arr[mid] >= arr[mid+1 ]:
                return mid
                
            elif mid == n-1 and arr[mid] >= arr[mid-1]:
                return mid 
                
            elif arr[mid] >= arr[mid-1 ] and arr[mid] >= arr[mid+1]:
                return mid 
            
            if arr[mid] < arr[mid + 1] :
                low = mid + 1 
            
            else:
                high = mid 
                
        return -1 