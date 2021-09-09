#Tow Numbers Sum
#function that takes in non-empty list
#find the two numbers that adds up to the target
'''solution'''
def twoNumberSum(array, targetSum):
    sum_list = []
    for i in range(len(array)):
        for j in array[i+1:]:
            if array[i] + j == targetSum:
                sum_list.extend([array[i], j])
    return sum_list



#Validate Subsequence
#given two array
#determine if the second array is the sub-array of the first
'''solution'''
def isValidSubsequence(array, sequence):
    if len(array) == len(sequence):
        for i in range(len(array)):
            if array[i] != sequence[i]:
                return False
        return True
    if len(array) < len(sequence):
        return False
        
    for i in sequence:
        for j in sequence[:sequence.index(i)+1]:
			if j not in array:
                return False
            if i in array:
                if array.index(i) < array.index(j):
                    return False
				if sequence.count(i) > array.count(i):
					return False
            else:
                return False
            
    return True

