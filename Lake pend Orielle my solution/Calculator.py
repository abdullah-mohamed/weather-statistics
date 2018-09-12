'''
used in Weather Data project
author: Abdullah Abunar
'''

def how_many_files_to_open(s_year, e_year):
	
	ret = 0					# return value
	if s_year == e_year:
		ret = 1
	elif s_year > e_year:
		ret = -1
	else:
		ret = e_year - s_year
	return ret
	
def find_boundries(s_year, s_month, s_day, e_year, e_month, e_day):
	
	# find the start line, start file position
	start_line = -1
	start_ptr = -1		# current file position
	with open('data files\Environmental_Data_Deep_Moor_{}.txt'.format(s_year), 'r') as file:		
		for line_num,line in enumerate(file.readlines()):
			words = line.split(' ')
			if words[0] == str( s_year + '_' + s_month + '_' + s_day ):
				start_line = line_num		# todo: increment by 1
				start_ptr = file.tell()
				break
				
	# find the end line, end file position
	end_line = -1
	end_ptr = -1
	with open('data files\Environmental_Data_Deep_Moor_{}.txt'.format(e_year), 'r') as file:
		for line_num,line in enumerate(file.readlines()):
			words = line.split(' ')
			if words[0] == str( e_year + '_' + e_month + '_' + e_day):
				end_line = line_num
				end_ptr = file.tell()
				break
	
	with open('data files\Environmental_Data_Deep_Moor_{}.txt'.format(e_year), 'r') as file:
		file.seek(end_ptr)
		print(file.readline())
		print(file.readline())
		print('For Debugging')
	
	print(start_line, end_line, start_ptr, end_ptr)
	return (start_line, end_line, start_ptr, end_ptr)
	
def calculate(s_year, s_month, s_day, e_year, e_month, e_day):
	# s_year for start year, e_year for end year
	
	files_num = how_many_files_to_open(s_year, e_year)
	swap_flag = 0			# flag to tell the user that start year is bigger than end year and the program has swapped them
	
	if files_num < 0:
		s_year, e_year = e_year, s_year
		swap_flag = 1
		files_num = how_many_files_to_open(s_year, e_year)
		
	start_line, end_line, start_ptr, end_ptr = find_boundries(s_year, s_month, s_day, e_year, e_month, e_day)
	
	# variables related to data
	wind_values = 0
	wind_values_num = 0
	temp_values = 0
	temp_values_num = 0
	pressure_values = 0
	pressure_values_num = 0
	
	if files_num == 1:
	
		
		
		
		
		
		
		
		# sweep in next year
		s_year = int(s_year) + 1
		s_year = str(s_year)
		files_num -= 1