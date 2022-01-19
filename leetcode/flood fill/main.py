def floodFill(arr,sr,sc,color,row,col):
    while sr != row-1 and sc != col-1:
      data = arr[sr][sc]
      arr[sr][sc] = color
      if arr[sr-1][sc] == data:
          floodFill(arr,sr-1,sc,color,row,col)
      if arr[sr+1][sc] == data:
          floodFill(arr,sr+1,sc,color,row,col)
      if arr[sr][sc-1] == data:
          floodFill(arr,sr,sc-1,color,row,col)
      if arr[sr][sc+1] == data:
          floodFill(arr,sr,sc+1,color,row,col)
      print(arr)    
      return 
     
floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2,3,3)          
