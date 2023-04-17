import sqlite3 
import pandas as pd 
import matplotlib.pyplot as plt


conn=sqlite3.connect("Nortwind.db")
#Obteniendo los 10 productos mas rentable
query='''
    SELECT ProductName,SUM(price*Quantity) as Revenue 
    from OrderDetails od 
    join Products p on  p.ProductID = od.ProductID 
    group by od.ProductID 
    Order  by revenue desc 
    LIMIT 10 
    '''
    
top_products=pd.read_sql_query(query,conn)
top_products.plot(x="ProductName",y="Revenue",kind="bar", figsize=(10,5), legend=False)

plt.title("Productos Rentables")
plt.xlabel("Productos")
plt.ylabel("Rvenue")
plt.xticks(rotation=90)
plt.show()
#Obteniendo los 10 productos mas rentable
query2='''
    SELECT FirstName || "" || LastName as Employee, Count(*) as Total
    from orders o 
    join Employees e
    ON e.EmployeeID= o.EmployeeID
    Group by o.EmployeeID 
    Order by Total Desc 

    '''
top_empoyees=pd.read_sql_query(query2,conn)
top_empoyees.plot(x="Employee",y="Total",kind="bar", figsize=(10,5), legend=False)

plt.title("Empleados mas efectivos")
plt.xlabel("Empleados")
plt.ylabel("Total Vendido")
plt.xticks(rotation = 45)
plt.show()