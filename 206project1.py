import os
import filecmp
import csv
import re
import pandas

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys will come from the first row in the data.

#Note: The column headings will not change from the
#test cases below, but the the data itself will
#change (contents and size) in the different test
#cases.

	#Your code here:
	data = open(file, "r")
	reader = csv.reader(data)
	datalist = []
	for row in reader:
		datadict = {}
		datadict['First'] = row[0]
		datadict['Last'] = row[1]
		datadict['Email'] = row[2]
		datadict['Class'] = row[3]
		datadict['DOB'] = row[4]
		if datadict['First'] != 'First':
			datalist.append(datadict)
	return(datalist)


#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	a = sorted(data, key = lambda x: x[col])
	return [x['First'] + ' ' + x['Last'] for x in a][0]


#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	csize = {}
	for x in data:
		if x['Class'] not in csize:
			csize[x['Class']] = 1
		else:
			csize[x['Class']] += 1
	csize_sort = sorted(csize.items(), key = lambda x: x[1], reverse = True)
	return csize_sort


# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	days = []
	for x in a:
		dates = x['DOB'].split('/')
		days.append(dates[1])
	daycount = {}
	for count in days:
		daycount[count] = daycount.get(count, 0) + 1
	daymax = sorted(daycount.items(), key = lambda x: x[1], reverse = True)
	return int(daymax[0][0])

# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	years = []
	for x in a:
		date = x['DOB'].split('/')
		years.append(date[2])
	agecounter = 0
	for y in years:
		age = 2017 - int(y)
		agecounter += age
	avgage = agecounter//int(len(years))
	return avgage


#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	data = sorted(a, key = lambda x: x[col])

	with open(fileName, 'w') as newfile:
		for x in range(len(data)):
			newfile.write(data[x]['First'] + ',' + data[x]['Last'] + ',' + data[x]['Email'] + '\n')


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),35)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)

	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
