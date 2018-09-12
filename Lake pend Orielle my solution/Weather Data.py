'''
 Weather program that calculates mean and median for wind speed, temp, and preasure
 based on text files of specific syntax.
 
 written by: Abdullah abunar
 version: 1.0
'''
try:
	from tkinter import *
	from tkinter import ttk
	import Data_checker						# in same directory
	import Calculator_temp
except Missing_Files :
	pass	

def calculate(s_year, s_month, s_day, e_year, e_month, e_day):
	Calculator_temp.calculate(s_year, s_month, s_day, e_year, e_month, e_day)
	
def main():

	root = Tk()
	
	# Three main frames and a button
	info_frame = ttk.Frame(root, height = 100, width = 300, relief = SOLID)
	info_frame.pack()
	
	date_frame = ttk.Frame(root, height = 100, width = 300, relief = SOLID)
	date_frame.pack()
	
	weather_frame = ttk.LabelFrame(root, height = 150, width = 300, text = 'Data')
	weather_frame.pack()
	
	# info_frame widgets
	
	inf_msg = '''This is a mean/median calculator for Wind, Temperature, Pressure using SPECIAL-SYNTAX data files from the Internet.\nPlease check README.txt file in the program Directory.'''
	ttk.Label(info_frame, justify = CENTER, wraplength = 450, text = inf_msg).pack()
	
	# date_frame widgets
	
	# labels above comboboxes
	ttk.Label(date_frame, text = 'Start Year',
				background = 'blue').grid(row = 0, column = 0, padx = 20, pady = 5)
				
	ttk.Label(date_frame, text = 'Start Month',
				background = 'blue').grid(row = 0, column = 1, padx = 20, pady = 5)
				
	ttk.Label(date_frame, text = 'Start Day',
				background = 'blue').grid(row = 0, column = 2, padx = 20, pady = 5)
	
	# variables to hold start values of comboboxes
	s_year = StringVar()
	s_month = StringVar()
	s_day = StringVar()
	
	# comboboxes
	year_combo = ttk.Combobox(date_frame, textvariable = s_year)
	year_combo.grid(row = 1, column = 0, padx = 20, pady = 5)
	year_combo.configure(values = Data_checker.available_years())			# see Data_checker file in same directory
	
	month_combo = ttk.Combobox(date_frame, textvariable = s_month)
	month_combo.grid(row = 1, column = 1, padx = 20, pady = 5)
	month_combo.configure(values = ('01','02','03','04','05','06','07','08','09','10','11','12'))
	
	day_combo = ttk.Combobox(date_frame, textvariable = s_day)
	day_combo.grid(row = 1, column = 2, padx = 20, pady = 5)
	day_combo.configure(values = ('01','02','03','04','05','06','07','08','09','10','11','12',
									'13','14','15','16','17','18','19','20','21','22','23','24',
									'25','26','27','28','29','30','31'))
	
	# End-labels above comboboxes
	ttk.Label(date_frame, text = 'End Year',
				background = 'blue').grid(row = 2, column = 0, padx = 20, pady = 5)
				
	ttk.Label(date_frame, text = 'End Month',
				background = 'blue').grid(row = 2, column = 1, padx = 20, pady = 5)
				
	ttk.Label(date_frame, text = 'End Day',
				background = 'blue').grid(row = 2, column = 2, padx = 20, pady = 5)
	
	# variables to hold start values of comboboxes
	e_year = StringVar()
	e_month = StringVar()
	e_day = StringVar()
	
	# comboboxes
	year_combo = ttk.Combobox(date_frame, textvariable = e_year)
	year_combo.grid(row = 3, column = 0, padx = 20, pady = 5)
	year_combo.configure(values = Data_checker.available_years())			# see Data_checker file in same directory
	
	month_combo = ttk.Combobox(date_frame, textvariable = e_month)
	month_combo.grid(row = 3, column = 1, padx = 20, pady = 5)
	month_combo.configure(values = ('01','02','03','04','05','06','07','08','09','10','11','12'))
	
	day_combo = ttk.Combobox(date_frame, textvariable = e_day)
	day_combo.grid(row = 3, column = 2, padx = 20, pady = 5)
	day_combo.configure(values = ('01','02','03','04','05','06','07','08','09','10','11','12',
									'13','14','15','16','17','18','19','20','21','22','23','24',
									'25','26','27','28','29','30','31'))
	
	# weather_frame widgets
	
	# 3 rows * 4 columns widget
	# first row
	ttk.Label(weather_frame, text = 'Wind',
				background = 'blue').grid(row = 0, column = 1, padx = 20, pady = 5)
	
	ttk.Label(weather_frame, text = 'Temp',
				background = 'blue').grid(row = 0, column = 2, padx = 20, pady = 5)
				
	ttk.Label(weather_frame, text = 'Press',
				background = 'blue').grid(row = 0, column = 3, padx = 20, pady = 5)
	
	# second row
	ttk.Label(weather_frame, text = 'Mean',
				background = 'blue').grid(row = 1, column = 0, padx = 20, pady = 5)
				
	wind_mean = ttk.Label(weather_frame, text = 'Null0')
	wind_mean.grid(row = 1, column = 1, padx = 20, pady = 5)

	temp_mean = ttk.Label(weather_frame, text = 'Null1')
	temp_mean.grid(row = 1, column = 2, padx = 20, pady = 5)

	pressure_mean = ttk.Label(weather_frame, text = 'Null2')
	pressure_mean.grid(row = 1, column = 3, padx = 20, pady = 5)
	
	# third row
	ttk.Label(weather_frame, text = 'Median',
				background = 'blue').grid(row = 2, column = 0, padx = 20, pady = 5)
				
	wind_median = ttk.Label(weather_frame, text = 'Null3')
	wind_median.grid(row = 2, column = 1, padx = 20, pady = 5)
		
	temp_median = ttk.Label(weather_frame, text = 'Null4')
	temp_median.grid(row = 2, column = 2, padx = 20, pady = 5)
	
	preasure_median = ttk.Label(weather_frame, text = 'Null5')
	preasure_median.grid(row = 2, column = 3, padx = 20, pady = 5)
	
	# Button
	calc_button = ttk.Button(root, text = 'Calculate')
	calc_button.pack()
	calc_button.config(command = lambda: calculate(s_year.get(), s_month.get(), s_day.get(), e_year.get(), e_month.get(), e_day.get()))
	root.mainloop()
	
	
if __name__ == '__main__':
	main()