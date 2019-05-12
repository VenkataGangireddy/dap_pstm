import mysql.connector as mc
import configparser
import datetime
import pandas as pd
from pandas import DataFrame
import os

class dataClient():
	'''
	Generic Class for Data Services.
	'''
	def __init__(self):
		'''
		Class constructor or initialization method.
		'''
		# The below line of code is for enabling the code to run in Docker
		config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
		self.config = configparser.ConfigParser()
		# print ("test")
		self.config.read(config_file)
		self.user = self.config['MYSQL']['user']
		self.passwd = self.config['MYSQL']['passwd']
		self.host = self.config['MYSQL']['host']
		self.database = self.config['MYSQL']['database']
		self.auth = self.config['MYSQL']['auth_plugin']

	#get the database connection. database name is in .ini file
	def get_connection(self):
		return mc.connect(user=self.user,password=self.passwd,host=self.host, database=self.database,auth_plugin=self.auth)

	def read_topics2(self):
		topic_select = 'select a.topic_id,a.Name, b.Topic_Entity_Id,b.Entity_Type,b.Entity_Value from topics_tbl a, topic_entities_tbl b where a.topic_id = b.topic_id and a.Active_flag = 1 and b.Active_flag=1'
		df = self.get_dataAsDataFrame(topic_select)
		return df
	
	def callStoredProcedure(self,procname,args):
		try:
			
			connection = self.get_connection()
			cursor = connection.cursor(buffered=True)
			if len(args) > 0:
				cursor.callproc(procname, args)
			else:
				cursor.callproc(procname)
			column_names_list = []
			results = []
			for result in cursor.stored_results():
				column_names_list = [x[0] for x in result.description]
				results = result.fetchall()
			df = DataFrame(results,columns=column_names_list)
			cursor.close()
			connection.close()
			return df
		except Exception as e:
			cursor.close()
			connection.close()


	def get_dataAsDataFrame(self,sql):
		try:
			connection = self.get_connection()
			cursor = connection.cursor(buffered=True) #need to set buffered=True to avoid MySQL Unread result error
			cursor.execute(sql)
			num_fields = len(cursor.description)
			field_names = [i[0] for i in cursor.description]
			df = DataFrame(cursor.fetchall(),columns=field_names)
			connection.commit()
			cursor.close()
			connection.close()
			return df
		except Exception as e:
			print(e)
			cursor.close()
			connection.close()


	# Read the topics from DB
	def read_topics(self):
		topic_select = 'select a.topic_id,a.Name, b.Topic_Entity_Id,b.Entity_Type,b.Entity_Value from topics_tbl a, topic_entities_tbl b where a.topic_id = b.topic_id and a.Active_flag = 1 and b.Active_flag=1'
		result_set = self.run_query(topic_select)
		# print ("test")
		return result_set

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

if __name__ == "__main__":
	# Sample Code to invoke the Stored Procedure 
	data = dataClient()
	args=['ORIGINAL']
	sentiment_df = data.callStoredProcedure('Get_Tweets_Sentiments',args)
	print(sentiment_df)
	arg=[]
	topics_df = data.callStoredProcedure('Get_Topics',arg)
	print(topics_df,arg)
	time1 = datetime.date.today()
	time2 = datetime.date.today()

	ar = [1,time1,time2,100,'SUCCESS']
	response = data.callStoredProcedure('Create_Event_Log',ar)
	print(response)

