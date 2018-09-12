from tkinter import *
from tkinter import ttk, messagebox
from statistics import mean, median
from datetime import date
import lpoDB

class lpoApp:
	"""
	This is the top level module for the Lake
	Pond Orielle stastistics challenge.
	stastistics module is introduced in python 3.4
	"""
	
	def __init__(self, master):
	
		self.master = master
		self._createGUI()
		self.database = lpoDB.lpoDB()
		self.master.protocol("WM_DELETE_WINDOW", self._safe_close)
		
	def _createGUI(self):
	
		# create the style
		bgcolor = '#CCCCFF'
		self.master.configure(background = bgcolor)
		self.master.title('Lake Pond Orielle')
		self.master.resizable(False, False)
		self.style = ttk.Style()
		self.style.configure('TFrame', background = bgcolor)
		self.style.configure('TButton', background = bgcolor, font = ('Arial Black', 10))
		self.style.configure('TLabel', background = bgcolor, font = ('Arial Black', 10))
		self.style.configure('Status.TLabel', background = bgcolor, font = ('Arial', 10))
		self.style.configure('Result.TLabel', background = bgcolor, font = ('Courier', 10))
		
		# create a frame with the picture
		self.photo_frame = ttk.Frame(self.master)
		self.photo_frame.pack(side = TOP)
		self.logo = PhotoImage(file = 'lpo_logo.gif')
		ttk.Label(self.photo_frame, image = self.logo).pack()
		
		# create a frame for data input
		self.input_frame = ttk.Frame(self.master)
		self.input_frame.pack(side = TOP)
		
		ttk.Label(self.input_frame, text = 'Start Date:').grid(row = 0, column = 1, columnspan = 3, sticky = 'sw')
		ttk.Label(self.input_frame, text = 'End Date:').grid(row = 0, column = 5, columnspan = 3, sticky = 'sw')
		
		self.start_day = StringVar()
		self.start_month = StringVar()
		self.start_year = StringVar()
		self.end_day = StringVar()
		self.end_month = StringVar()
		self.end_year = StringVar()
		
		self.spinbox_months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
								'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
		
		# spinboxes for user input
		Spinbox(self.input_frame, from_ = 1 , to = 31
				, textvariable = self.start_day, width = 2
				, font = 'Courier 12').grid(row = 1, column = 1)
		Spinbox(self.input_frame, values = self.spinbox_months
				, textvariable = self.start_month, width = 3
				, font = 'Courier 12').grid(row = 1, column = 2)
		Spinbox(self.input_frame, from_ = 2001, to = date.today().year
				, textvariable = self.start_year, width = 4
				, font = 'Courier 12').grid(row = 1, column = 3)
		Spinbox(self.input_frame, from_ = 1 , to = 31
				, textvariable = self.end_day, width = 2
				, font = 'Courier 12').grid(row = 1, column = 5)
		Spinbox(self.input_frame, values = self.spinbox_months
				, textvariable = self.end_month, width = 3
				, font = 'Courier 12').grid(row = 1, column = 6)
		Spinbox(self.input_frame, from_ = 2001, to = date.today().year
				, textvariable = self.end_year, width = 4
				, font = 'Courier 12').grid(row = 1, column = 7)
				
		# set values of spinboxes to date of today
		self.start_day.set(date.today().day)
		self.start_month.set(self.spinbox_months[date.today().month - 1])
		self.start_year.set(date.today().year)
		self.end_day.set(date.today().day)
		self.end_month.set(self.spinbox_months[date.today().month - 1])
		self.end_year.set(date.today().year)
		
		# for padding
		ttk.Label(self.input_frame).grid(row = 1, column = 0, padx = 5)
		ttk.Label(self.input_frame).grid(row = 1, column = 4, padx = 5)
		ttk.Label(self.input_frame).grid(row = 1, column = 8, padx = 5)
		
		# button for submitting dates
		ttk.Button(self.input_frame, text = 'submit',
					command = self._submit_callback).grid(row = 3, column = 3, columnspan = 3, pady = 5)
					
		# result frame, doesn't show up until submit is clicked
		self.result_frame = ttk.Frame(self.master)
		
		ttk.Label(self.result_frame, text = 'wind\ngust',
					justify = CENTER).grid(row = 0, column = 1, padx = 3)
		ttk.Label(self.result_frame, text = 'Barometric\npressure',
					justify = CENTER).grid(row = 0, column = 2, padx = 3)
		ttk.Label(self.result_frame, text = 'Air\nTemperature',
					justify = CENTER).grid(row = 0, column = 3, padx = 3)
		
		ttk.Label(self.result_frame, text = 'Mean :').grid(row = 1, column = 0, padx = 3)
		ttk.Label(self.result_frame, text = 'Median :').grid(row = 2, column = 0, padx = 3)
		
		self.wind_gust_mean = StringVar()
		self.wind_gust_median = StringVar()
		self.barometric_pressure_mean = StringVar()
		self.barometric_pressure_median = StringVar()
		self.air_temperature_mean = StringVar()
		self.air_temperature_median = StringVar()
		
		ttk.Label(self.result_frame, textvariable = self.wind_gust_mean,
					style = 'Result.TLabel').grid(row = 1, column = 1, padx = 3)
		ttk.Label(self.result_frame, textvariable = self.barometric_pressure_mean,
					style = 'Result.TLabel').grid(row = 1, column = 2, padx = 3)
		ttk.Label(self.result_frame, textvariable = self.air_temperature_mean,
					style = 'Result.TLabel').grid(row = 1, column = 3, padx = 3)
		ttk.Label(self.result_frame, textvariable = self.wind_gust_median,
					style = 'Result.TLabel').grid(row = 2, column = 1, padx = 3)
		ttk.Label(self.result_frame, textvariable = self.barometric_pressure_median,
					style = 'Result.TLabel').grid(row = 2, column = 2, padx = 3)
		ttk.Label(self.result_frame, textvariable = self.air_temperature_median,
					style = 'Result.TLabel').grid(row = 2, column = 3, padx = 3)

	def _submit_callback(self):
		
		# check for dates validity
		try:
			self.start_date = date(int(self.start_year.get()),
									self.spinbox_months.index(self.start_month.get()) + 1,
									int(self.start_day.get()))
									
			self.end_date = date(int(self.end_year.get()),
									self.spinbox_months.index(self.end_month.get()) + 1,
									int(self.end_day.get()))
		except ValueError as e :
			messagebox.showerror(title = 'Error', message = 'wrong date format')
			
			# reset values of spinboxes to default
			self.start_day.set(date.today().day)
			self.start_month.set(date.today().month)
			self.start_year.set(date.today().year)
			self.end_day.set(date.today().day)
			self.end_month.set(date.today().month)
			self.end_year.set(date.today().year)
			return
			
		# check if start_date is after end_date
		if (self.start_date >= self.end_date) or (self.end_date > date.today()) or (self.start_date < date(2001,1,1)):
			messagebox.showerror(title = 'Error',
								message = ("End Date value must be greater than Start Date.\n"
											"Invalid date range.\n"
											"Do I look like a forcasting magic ball to you!!\n"
											)
			return
			
		data = list(self.database.get_data_for_range(self.start_date, self.end_date))
		
		if data != []:
		
			
			self.result_frame.pack(side = TOP)
		
	def _safe_close(self):
		'''
		This is invoked when the user closes the root window.
		It ensures the DB is closed and destroys the root.
		'''
		self.database.close()
		self.master.destroy()

def main():
	
	root = Tk()
	App = lpoApp(root)
	root.mainloop()
	
if __name__ == '__main__': main()
