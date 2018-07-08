import pymysql

class Database:
    #self.cur.execute("CREATE TABLE IF NOT EXISTS Booligans.Test1 (ID INT primary key, Name VARCHAR(50))")

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='appleuser', autocommit=True)
        self.cur = self.conn.cursor()
        self.locationTbl = 'LocationHistory'
        self.cur.execute('USE Booligans')
        self.cur.execute("CREATE TABLE IF NOT EXISTS Booligans."+self.locationTbl+"(ID INT NOT NULL primary key AUTO_INCREMENT, Latitude DECIMAL(10,7), Longitude DECIMAL(10,7), Time TIMESTAMP)")

        self.filesTbl = 'Files'
        self.cur.execute("CREATE TABLE IF NOT EXISTS Booligans."+self.filesTbl+"(ID INT NOT NULL primary key AUTO_INCREMENT, Name VARCHAR(30), FilePath VARCHAR(255))")

    def connect(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='appleuser', autocommit=True)
        self.cur = self.conn.cursor()
        self.cur.execute('USE Booligans')

    def closeConn(self):
        self.cur.close()
        self.conn.close()


    def insert(self, table, *args):
        if table == "LocationHistory":
            str = "INSERT INTO Booligans." + table + " (Latitude, Longitude, Time)" + " VALUES ('" + args[0] + "', '" + args[1] +  "','"+ args[2] + "')"
            print(str)
            self.cur.execute("INSERT INTO Booligans." + table + " (Latitude, Longitude, Time)" + " VALUES ('" + args[0] + "', '" + args[1] +  "','"+ args[2] + "')")
        if table == "Files":
            self.cur.execute("INSERT INTO Booligans." + table + " (Name, FilePath)" + " VALUES ('" + args[0] + "', '" + args[1] + "')")
        #cur.execute("INSERT INTO Booligans.Test1 VALUES (1, 'Jack')")
        #cur.execute("INSERT INTO Booligans.Test1 VALUES (2, 'Joe')")
        print(self.cur.description)

    def getTableSnapshot(self, table):
        self.cur.execute("SELECT * FROM Booligans." + table)
        rows = self.cur.fetchall()
        return rows

    def customCmd(self, cmd):
        self.cur.execute(cmd)

