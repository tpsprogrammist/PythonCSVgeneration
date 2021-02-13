my_file = open("sampleData.csv", "w")
i=0
 
my_file.write("FirstName,LastName,Title,Birthdate,Description\n")
 
# FirstName,LastName,Title,ReportsTo.Email,Birthdate,Description
 
while i<600:
my_file.write("John"+str(i)+",Testo"+str(i)+",Employee,1980-01-09Z,TheBest\n")
 
 
i=i+1
my_file.close()
