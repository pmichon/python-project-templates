#!/usr/bin/env python3.4

import json 	# import/export to local json
import datetime	# reporting timestamps
#from pprint import pprint #pprint for debug and tests
import gspread	# connect to google spreadsheet
from oauth2client.service_account import ServiceAccountCredentials #required for google spreadsheet auth


class processAndPushToGspread:
	def __init__(self):
		self.data = {}
		self._initialize_gspread()

	def _initialize_gspread(self):
		scope = ['https://spreadsheets.google.com/feeds']
		#TODO: creds file to google api
		credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json',scope)  
		gc = gspread.authorize(credentials)
		#TODO: spreadsheet key below
		sht1 = gc.open_by_key('')
		#TODO: worksheet name
		self.worksheet = sht1.worksheet("Sheet 1")
	
	def import_json(self,fn):
		with open(fn) as fp:
			self.seed = json.load(fp)
	
	def _process_data(self, count=3):
		print('Processing', end="", flush=True)
		generated=0
		while generated < count:
			#TODO: do some stuff
			print('.', end="", flush=True)
			generated += 1
		print("done")

	def export_gdocs(self):
		print('Exporting', end="", flush=True)

		#clean the sheet:
#		cell_list = self.answers_worksheet.range('A1:D10')
#		for cell in cell_list:
#			cell.value = ''
#		self.answers_worksheet.update_cells(cell_list)

		#iterate and update:
#		for response in self.answers:
#			print('.', end="", flush=True)
		
		#leave timestamp
#		self.worksheet.update_acell('A1', now.strftime("%Y-%m-%d %H:%M"))
		print("done")

	def import_gdocs(self):
		print('Importing', end="", flush=True)
		print('done')

if __name__ == "__main__":
	m = processAndPushToGspread()
	#m.import_json("file.json")
	#m.import_gdocs()
	#m._process_data(40)
	#m.export_gdocs()
	
