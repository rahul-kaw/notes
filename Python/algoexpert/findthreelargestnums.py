'''

  Write a function that takes in an array of at least three integers and,
  without sorting the input array, returns a sorted array of the three largest
  integers in the input array.


  The function should return duplicate integers if necessary; for example, it
  should return [10, 10, 12]  for an input array of [10, 5, 9, 10, 12]

'''

#Solution 1
def findThreeLargestNumbers(array):
    # Write your code here.
	maxvaluesarray = array[:3]
	maxvaluesarray.sort()
		
	for num in array[3:]:
		print(num)
		if num > maxvaluesarray[0]:
			maxvaluesarray[0] = num
			maxvaluesarray.sort()
		print(maxvaluesarray)
	
	return maxvaluesarray

#Alternate solution
def findThreeLargestNums(array):
    three_largest_number = [None, None, None]
    for num in array:
        update_largest(num, three_largest_number)
    return three_largest_number


def update_largest(number, three_largest_number):
    if three_largest_number[2] is None or number > three_largest_number[2]:
        shift_and_update(three_largest_number, number, 2)
    elif three_largest_number[1] is None or number > three_largest_number[1]:
        shift_and_update(three_largest_number, number, 1)
    elif three_largest_number[0] is None or number > three_largest_number[0]:
        shift_and_update(three_largest_number, number, 0)
        

def shift_and_update(three_largest_number, number, index):
    print(len(three_largest_number))
    for i in range(index + 1):
        if i == index:
            three_largest_number[index] = number
        else:
            three_largest_number[i] = three_largest_number[i + 1]
