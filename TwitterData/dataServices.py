import mysql.connector as mc
import configparser
import datetime
import pandas as pd

class dataClient():
	'''
	Generic Class for Data Services.
	'''
	def __init__(self):
		'''
		Class constructor or initialization method.
		'''
		self.config = configparser.ConfigParser()
		self.config.read('config.ini')
		self.user = self.config['MYSQL']['user']
		self.passwd = self.config['MYSQL']['passwd']
		self.host = self.config['MYSQL']['host']
		self.database = self.config['MYSQL']['database']
		self.auth = self.config['MYSQL']['auth_plugin']

	#get the database connection. database name is in .ini file
	def get_connection(self):
		return mc.connect(user=self.user,password=self.passwd,host=self.host, database=self.database,auth_plugin=self.auth)

	# Read the topics from DB
	def read_topics(self):
		topic_select = 'select a.topic_id,a.Name, b.Topic_Entity_Id,b.Entity_Type,b.Entity_Value from topics_tbl a, topic_entities_tbl b where a.topic_id = b.topic_id and a.Active_flag = 1 and b.Active_flag=1'
		result_set = self.run_query(topic_select)
		return result_set
		#for n in result_set:
			#print('id : ',n[0], "description :", n[1])

	def run_query(self, sql):
	    connection = self.get_connection()
	    connection.cmd_query(sql)
	    result_set_and_meta = connection.get_rows()
	    result_set = result_set_and_meta[0]
	    connection.close()
	    return result_set

	def saveDatatoDB(self, df,table):
		print("------Saving Data into table-----",table)
		try:
			connection = self.get_connection()
			value_string = ', '.join(['%s' for _ in range(len(df.columns))])
			columns = ', '.join([col_name for col_name in df.columns])
			cursor = connection.cursor()
			cursor.executemany(
	                               """INSERT IGNORE INTO {} ({}) VALUES ({})""".format(table, columns, value_string),
	                               df.values.tolist())
			connection.commit()
			cursor.close()
			connection.close()
			print("------Successfully saved data into the table-----",table)
		except Exception as e:
			print(e)
			cursor.close()
			connection.close()
