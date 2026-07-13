IF NOT EXISTS (
    SELECT name 
    FROM sys.databases 
    WHERE name = N'FoodOrderPoc'
)
BEGIN
    CREATE DATABASE FoodOrderPoc;
END
GO



USE FoodOrderPoc
GO


CREATE TABLE FoodItems
(
	FoodItemId INT IDENTITY(1,1) PRIMARY KEY
	,FoodItemName VARCHAR(150)
	,FoodPrice DECIMAL(19,4)
	,IsActive BIT
)
GO

IF NOT EXISTS (SELECT * FROM FoodItems)
BEGIN
	INSERT INTO FoodItems(FoodItemName, FoodPrice, IsActive)
	VALUES ('Samosa', 5, 1)
	,('Pizza', 25, 1)
	,('Mango Lassi', 10, 1)
	,('Biryani', 35, 1)
	,('Pav Bajji', 15, 1)
	,('Vada Pav', 12, 1)
END

CREATE TABLE Orders
(
	OrderId INT IDENTITY(1,1) PRIMARY KEY
	,OrderPrice DECIMAL(19,4)
	,Status VARCHAR(500)
	,IsActive BIT
)
GO

CREATE TABLE FoodItemOrder
(
	FoodItemOrderId BIGINT IDENTITY(1,1) PRIMARY KEY
	,OrderId INT
	,FoodItemId INT
	,Quantity INT

	CONSTRAINT FK_FoodItemOrder_Order FOREIGN KEY (OrderId) REFERENCES Orders(OrderId),
    CONSTRAINT FK_FoodItemOrder_FoodItem FOREIGN KEY (FoodItemId) REFERENCES FoodItems(FoodItemId)
)
GO