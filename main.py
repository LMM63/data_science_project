print("hello Data Science Project")
#filt = lambda X,Y: [x for x in X if x in Y] # lambda function
#R= filt ([2,4,6,8,10], [1,2,3,4,5,6]) 
#print(f"Result: {R}")
X= [1,2,3, "Hi", 4, 5, 6, "Hello"]
print ([x for x in X if type(x) == str])