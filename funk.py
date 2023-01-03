import sqlite3
from main import *
from aiogram import Bot, Dispatcher, executor, types

class Tablitsa:
	def __init__(self):
		self.conn = sqlite3.connect("tiktok.db")
		self.c = self.conn.cursor()




	def bosh(self):
		self.c.execute("""CREATE TABLE IF NOT EXISTS users(
			id integer,
			username varchar(60),
			first_name varchar(60),
			voxt time NULL
			)""")

	# def user_id(self,user_id,username,first_name):
	# 	self.c.execute("SELECT time('now')")
	# 	date = self.c.fetchone()
	# 	return date

	# 	self.c.execute(f"SELECT id FROM users WHERE id = {user_id}")
	# 	data = self.fetchone()

	# 	if data is None:
	# 	  	self.c.execute("INSERT INTO users VALUES ({},'{}','{}',NULL)".format(user_id,username,first_name))
	# 	  	self.c.execute(f"UPDATE users SET voxt = {date} WHERE id = {user_id} ")
	# 	  	self.conn.commit()
	# 		await message.answer('assalomu aleykum')
	# 	else:
	# 		await message.answer('sz royxatdan otkansz')


object1 = Tablitsa()
