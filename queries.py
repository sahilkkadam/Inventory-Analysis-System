from connection import execute_query

def highest_revenue_products():
    query = '''
        SELECT
	        p.ProductName,
	        SUM(o.UnitPrice*o.Quantity) AS TotalRevenue
        FROM product p
        Join orderitem o
        ON p.Id = o.ProductId
        GROUP BY p.ProductName
        ORDER BY TotalRevenue Desc
        LIMIT 10;
    '''
    execute_query(query, "highest_revenue_products")

def top_customers():
    query = '''
        SELECT
	        c.FirstName,
	        c.LastName,
	        Count(*) AS NoOfOrders,
	        SUM(o.TotalAmount) AS TotalAmountSpent
        FROM customer c
        JOIN orders o
        ON c.Id = o.CustomerId
        GROUP BY 
	        c.FirstName,
	        c.LastName
        ORDER BY NoOfOrders Desc,
	    TotalAmountSpent Desc;
    '''
    execute_query(query, "top_customers")

def avg_order_value_region():
    query = '''
        SELECT
	        c.City,
	        c.Country,
	        Avg(o.TotalAmount) AS AverageOrderValue
        FROM customer c
        JOIN orders o
        ON c.Id = o.CustomerId
        GROUP BY 
	        c.City,
	        c.Country
        ORDER BY AverageOrderValue Desc;
    '''
    execute_query(query, "avg_order_value_region")

def highest_sales_products():
    query = '''
        SELECT
	        ProductName,
	        SUM(o.Quantity) AS TotalSales
        FROM product p
        JOIN orderitem o
        ON p.Id = o.ProductId
        GROUP BY ProductName
        ORDER BY TotalSales Desc;
    '''
    execute_query(query, "highest_sales_products")

def supplier_revenue():
    query = '''
        SELECT
	        s.CompanyName,
	        p.ProductName,
	        SUM(o.UnitPrice*o.Quantity) AS Revenue
        FROM supplier s
        JOIN product p
        ON s.Id = p.SupplierId
        JOIN orderitem o
        ON p.Id = o.OrderId
        GROUP BY 
	        s.CompanyName,
	        p.ProductName
        ORDER BY Revenue Desc;
    '''
    execute_query(query, "supplier_revenue")

def discontinued_product_sales():
    query = '''
        SELECT
	        p.ProductName,
	        SUM(o.UnitPrice*o.Quantity) AS Revenue
        FROM product p
        Join orderitem o
        ON p.Id = o.ProductId
        WHERE p.IsDiscontinued = b'1'
        GROUP BY p.ProductName
        ORDER BY Revenue Desc;
    '''
    execute_query(query, "discontinued_product_sales")

def products_purchased_together():
    query = '''
        WITH productbundles AS(
	        SELECT
		        p1.ProductName AS Product1,
		        p2.ProductName AS Product2,
		        SUM(o1.UnitPrice*o1.Quantity + o2.UnitPrice*o2.Quantity) AS TotalRevenue,
		        Count(*) AS Frequency
	        FROM orderitem o1
	        JOIN orderitem o2
		        ON o1.OrderId = o2.OrderId
		    AND o1.ProductId < o2.ProductId
	        JOIN product p1
		        ON o1.ProductId = p1.Id
	        JOIN product p2
		        ON o2.ProductId = p2.Id
	        GROUP BY 
		        p1.ProductName, p2.ProductName
        )
        SELECT
	        Product1,
	        Product2,
	        TotalRevenue,
	        Frequency
        FROM productbundles
        WHERE Frequency = (SELECT MAX(Frequency) FROM productbundles)
        ;
    '''
    execute_query(query, "products_purchased_together")