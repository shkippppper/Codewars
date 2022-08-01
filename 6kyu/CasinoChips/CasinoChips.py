import time


#     can_play = True
#     days = 0
#     while can_play:
        
#         for i in range(len(arr)):
#             if (arr[i]) > 1 :
#                 arr[i] = arr[i]-1 
#                 days +=1




# solve([3,1,2])


#time.sleep(1)



def solve(arr):
    countable = 0
    while arr[0]*arr[1]!=0 or arr[1]*arr[2]!=0 or arr[0]*arr[2]!=0:
        countable += randomizer(arr,0,1)
        countable += randomizer(arr,0,2)
        countable += randomizer(arr,1,2)
    print(countable)


def randomizer(array,x,y):
    if array[x]>0 and array[y]>0:
        array[x] -= 1
        array[y] -= 1
        print(array)
        return 1
    else: return 0

solve([1,23,2])


def solve(xs):
    x, y, z = sorted(xs)
    return min(x + y, (x + y + z) // 2).






