from typing import List

def equilibrium_index(arr: List[int]) -> int:
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]
        if right_sum == left_sum:
            return i
        left_sum += arr[i]
    return -1

if __name__ == "__main__":

   arr = [1, 3, 5, 2, 2]
   print("Array:", arr)
   print("Equilibrium Index:", equilibrium_index(arr))