import os
from os import path
from datetime import date

def available_years():
	# returns a tuple containing the years of the available data files in "data files" directory, starting from 2000
	year = 2000
	year_list = []
	
	while True:
		
		file_ = 'data files\Environmental_Data_Deep_Moor_{}.txt'.format(year)
		
		if path.exists( file_ ):
			year_list.append(year)
			year += 1
		elif year > date.today().year:
			break
		else:
			year += 1
	
	return tuple(year_list)
	
if __name__ == '__main__':
	available_years()
