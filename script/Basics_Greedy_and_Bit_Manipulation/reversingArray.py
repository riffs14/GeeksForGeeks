# code to reverse array or string

#def swap():

def reverse(array):
    #print(array[5])
    #n=len(array)
    start=0
    end=len(array)-1
    while(end>start):
        temp=array[start]
        array[start]=array[end]
        array[end]=temp
        start=start+1
        end=end-1


a=[1,2,3,4,5,6,7]
b="rahul Kumar Chaudhary"
#reverse(b)
#print(b)


## reversing array using python list slicing 
def reverseList(A):
  print( A[::-1])

reverseList(a)
print(a)

# for string, assigment is not supported. 
#  array[start]=array[end] is not allowd.

