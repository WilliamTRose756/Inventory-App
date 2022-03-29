import sqlite3

def connect():
	conn = sqlite3.connect("inventory.db")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS item (id INTEGER PRIMARY KEY, item_name text, lot_number integer, exp_date integer )")
	conn.commit()
	conn.close()

def insert(item_name, lot_number, exp_date):
	conn = sqlite3.connect("inventory.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO item VALUES (NULL,?,?,?)",(item_name,lot_number,exp_date))
	conn.commit()
	conn.close()

def view():
	conn = sqlite3.connect("inventory.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM item")
	rows=cur.fetchall()
	conn.close()
	return rows

def search(item_name="",lot_number="",exp_date=""):
	conn = sqlite3.connect("inventory.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM item WHERE item_name=? OR lot_number=? OR exp_date=?", (item_name,lot_number,exp_date))
	rows=cur.fetchall()
	conn.close()
	return rows

def delete(id):
	conn = sqlite3.connect("inventory.db")
	cur = conn.cursor()
	cur.execute("DELETE FROM item WHERE id=?", (id,))
	conn.commit()
	conn.close()

def update(id,item_name,lot_number,exp_date):
	conn = sqlite3.connect("inventory.db")
	cur = conn.cursor()
	cur.execute("UPDATE item SET item_name=?, lot_number=?, exp_date=? WHERE id=?", (item_name,lot_number,exp_date,id))
	conn.commit()
	conn.close()

def expire(exp_date=""):
	conn = sqlite3.connect("inventory.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM item WHERE exp_date <= date('now')")
	rows=cur.fetchall()
	conn.close()
	return rows

connect()
