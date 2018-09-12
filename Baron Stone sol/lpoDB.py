from datetime import date, timedelta, datetime
from tkinter import messagebox
#import lpoweb
import sqlite3

class lpoDB:
	"""
	A database class
	"""
	
	def __init__(self, **kwargs):
		
		self.filename = kwargs.get('filename', 'lpo.db')
		self.table = kwargs.get('table', 'Weather')
		
		self.db = sqlite3.connect(self.filename)
		self.db.row_factory = sqlite3.row
		self.db.execute('''CREATE TABLE IF NOT EXISTS {} 
							(Date TEXT,	Time TEXT, Status TEXT,
							Air_temp FLOAT, Barometric_pressure FLOAT,
							Wind_speed FLOAT)'''.format(self.table))		

	def __iter__(self):
		'''
		generator function to produce dicts out of each row
		'''
		cursor = self.db.execute('SELECT * FROM {} ORDER BY Date, Time'.format(self.table))
		for row in cursor:	yield dict(row)
		
	def get_data_for_range(self, start, end):
		'''
		returns data between 2 dates.
		'''
		
		dates_to_update = []
		
		# get available data for pre-2007
		for year in range(start.year, 2007):
			if list(self._get_status_for_range(date(year,1,12),date(year,1,12))) == []:
				dates_to_update.append(date(year,1,12))
				
	def _get_status_for_range(self, start, end):
		'''
		Checks if data between 2 dates is available.
		'''
		cursor = self.db.execute('''SELECT DISTINCT Date, Time FROM {}
									WHERE Date BETWEEN {} AND {}'''
									.format(self.table,
											start.strftime('%Y%m%d'),
											end.strftime('%Y%m%d')))
									
		for row in cursor:	yield dict(row)
if __name__ == '__main__': test()