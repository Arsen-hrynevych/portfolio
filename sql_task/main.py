import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="mydatabase"
)

cour = mydb.cursor()

cour.execute("CREATE TABLE IF NOT EXISTS Brand \
 (Id INT AUTO_INCREMENT PRIMARY KEY, \
 Name VARCHAR(50), \
 VendorPhoneNumber VARCHAR(15))")

brand_columns_data = [("Apple", "+380456323987"),
                      ("Samsung", "+380866428712")]

sql_brand_insert = "INSERT INTO Brand (Name, VendorPhoneNumber) VALUES (%s, %s)"

cour.executemany(sql_brand_insert, brand_columns_data)

cour.execute("CREATE TABLE IF NOT EXISTS Model \
 (Id INT AUTO_INCREMENT PRIMARY KEY, \
 Description VARCHAR(255), \
 Price DECIMAL(18,2), \
 BrandId INT, \
 FOREIGN KEY(BrandId) REFERENCES Brand(Id))")


model_columns_data = [("At the heart of iPhone SE", 10000),
                      ("the same superpowerful A15 Bionic ", 3000)]

sql_model_insert = "INSERT INTO Model (Description, Price) VALUES (%s, %s)"

cour.executemany(sql_model_insert, model_columns_data)


cour.execute("CREATE TABLE IF NOT EXISTS Consultant \
 (Id INT AUTO_INCREMENT PRIMARY KEY, \
 FirstName VARCHAR(25), \
 LastName VARCHAR(25), \
 ContactPhoneNumber VARCHAR(15))")

consultant_columns_data = [("Hulio", "Hulian", "+3746183134"),
                           ("Joan", "Joanion", "+374216183134"),
                           ("Margarita", "Margaritona", "+374618312134")]

sql_consultant_insert = "INSERT INTO Consultant (FirstName, LastName, ContactPhoneNumber) VALUES (%s, %s, %s)"

cour.executemany(sql_consultant_insert, consultant_columns_data)


cour.execute("CREATE TABLE IF NOT EXISTS BrandConsultant \
 (BrandId INT, \
 ConsultantId INT, \
 FOREIGN KEY(BrandId) REFERENCES Brand(Id), \
 FOREIGN KEY(ConsultantId) REFERENCES Consultant(Id))")


cour.execute("CREATE TABLE IF NOT EXISTS PurchaseOrder \
 (Id INT AUTO_INCREMENT PRIMARY KEY, \
 DateTime DATETIME, \
 ModelId INT, \
 ConsultantId INT, \
 Price DECIMAL (18,2), \
 FOREIGN KEY(ModelId) REFERENCES Model(Id), \
 FOREIGN KEY(ConsultantId) REFERENCES Consultant(Id))")

order_colum_data = ("2020-01-01 04:40:10", 1, 1, 3000)

sql_order_insert = "INSERT INTO PurchaseOrder (DateTime, ModelId, ConsultantId, Price) VALUES (%s,%s,%s,%s)"

cour.execute(sql_order_insert, order_colum_data)

mydb.commit()
cour.close()
mydb.close()