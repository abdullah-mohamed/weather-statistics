'''
used in Weather Data project
author: Abdullah Abunar
'''

def how_many_files_to_open(s_year, e_year):
	s_year = int(s_year)
	e_year = int(e_year)
	ret = 0					# return value
	if s_year == e_year:
		ret = 1
	elif s_year > e_year:
		ret = -1
	else:
		ret = e_year - s_year + 1
	return ret
	
def find_boundries(s_year, s_month, s_day, e_year, e_month, e_day):
	
	# find the start line
	start_line = -1
	with open('data files\Environmental_Data_Deep_Moor_{}.txt'.format(s_year), 'r') as file:		
		for line_num,line in enumerate(file.readlines()):
			words = line.split(' ')
			if words[0] == str( s_year + '_' + s_month + '_' + s_day ):
				start_line = line_num		# todo: increment by 1
				break
				
	# find the end line
	end_line = -1
	with open('data files\Environmental_Data_Deep_Moor_{}.txt'.format(e_year), 'r') as file:
		for line_num,line in enumerate(file.readlines()):
			words = line.split(' ')
			if words[0] == str( e_year + '_' + e_month + '_' + e_day):
				end_line = line_num
				break
	
	return (start_line, end_line)

def adjust_spaces(words):
	# discard the space in format of ' 6.30' 
	new_results = []
	if words[1][0] == ' ':
		new_results.append(words[1][1:])
	else:
		new_results.append(words[1])
	if words[2][0] == ' ':
		new_results.append(words[2][1:])
	else:
		new_results.append(words[2])
	if words[6][0] == ' ':
		new_results.append(words[6][1:])
	else:
		new_results.append(words[6])
	return new_results
	
def calculate(s_year, s_month, s_day, e_year, e_month, e_day):
	# s_year for start year, e_year for end year
	
	files_num = how_many_files_to_open(s_year, e_year)
	swap_flag = 0			# flag to tell the user that start year is bigger than end year and the program has swapped them
	
	if files_num < 0:
		s_year, e_year = e_year, s_year
		swap_flag = 1
		files_num = how_many_files_to_open(s_year, e_year)
		
	start_line, end_line = find_boundries(s_year, s_month, s_day, e_year, e_month, e_day)
	
	# variables related to data
	wind_values = 0
	wind_values_num = 0
	temp_values = 0
	temp_values_num = 0
	pressure_values = 0
	pressure_values_num = 0
	
	if files_num == 1:
		with open('data files\Environmental_Data_Deep_Moor_{}.txt'.format(s_year), 'r') as file:
			for line_num,line in enumerate(file.readlines()):
				if line_num >= start_line :
					words = line.split('\t')
					new_words = adjust_spaces(words)			# USELESS
					wind_values += float(new_words[2])
					wind_values_num += 1
					temp_values = float(new_words[0])
					temp_values_num += 1
					pressure_values = float(new_words[1])
					pressure_values_num += 1
				if line_num == end_line:
					break
	elif files_num == 2:
		# first file
		with open('data files\Environmental_Data_Deep_Moor_{}.txt'.format(s_year), 'r') as file:
			for line_num,line in enumerate(file.readlines()):
				if line_num >= start_line :
					words = line.split('\t')
					new_words = adjust_spaces(words)
					wind_values += float(new_words[2])
					wind_values_num += 1
					temp_values = float(new_words[0])
					temp_values_num += 1
					pressure_values = float(new_words[1])
					pressure_values_num += 1
		# second_file
		with open('data files\Environmental_Data_Deep_Moor_{}.txt'.format(e_year), 'r') as file:
			for line_num,line in enumerate(file.readlines()):
				if line_num == 0 : continue 	# first line has no data
				if line_num == end_line :
					break
				else:
					words = line.split('\t')
					new_words = adjust_spaces(words)			# USELESS
					wind_values += float(new_words[2])
					wind_values_num += 1
					temp_values = float(new_words[0])
					temp_values_num += 1
					pressure_values = float(new_words[1])
					pressure_values_num += 1
	else:
		# more than 2 files
		# first file
		with open('data files\Environmental_Data_Deep_Moor_{}.txt'.format(s_year), 'r') as file:
			for line_num,line in enumerate(file.readlines()):
				if line_num >= start_line :
					words = line.split('\t')
					new_words = adjust_spaces(words)			# USELESS
					wind_values += float(new_words[2])
					wind_values_num += 1
					temp_values = float(new_words[0])
					temp_values_num += 1
					pressure_values = float(new_words[1])
					pressure_values_num += 1
						
		# loop on all files in between except last file
		while (files_num - 1) > 1:
			next_year = int(s_year) + 1
			with open('data files\Environmental_Data_Deep_Moor_{}.txt'.format(next_year), 'r') as file:
				for line_num,line in enumerate(file.readlines()):
					if line_num == 0 : continue 	# first line has no data
					words = line.split('\t')
					new_words = adjust_spaces(words)			# USELESS
					wind_values += float(new_words[2])
					wind_values_num += 1
					temp_values = float(new_words[0])
					temp_values_num += 1
					pressure_values = float(new_words[1])
					pressure_values_num += 1
			next_year += 1
			files_num -= 1
		
		# last file
		with open('data files\Environmental_Data_Deep_Moor_{}.txt'.format(e_year), 'r') as file:
			for line_num,line in enumerate(file.readlines()):
				if line_num == 0 : continue 	# first line has no data				
				if line_num == end_line :
					break
				else:
					words = line.split('\t')
					new_words = adjust_spaces(words)			# USELESS
					wind_values += float(new_words[2])
					wind_values_num += 1
					temp_values = float(new_words[0])
					temp_values_num += 1
					pressure_values = float(new_words[1])
					pressure_values_num += 1
	print(wind_values/wind_values_num, temp_values/temp_values_num, pressure_values/pressure_values_num)				
	return(wind_values/wind_values_num, temp_values/temp_values_num, pressure_values/pressure_values_num)		