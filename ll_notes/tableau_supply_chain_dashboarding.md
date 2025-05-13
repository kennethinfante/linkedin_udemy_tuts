# Tableau Supply Chain Dashboarding

My overall goal is to convert the dashboard to PowerBI

## Procurement

* Cost per Unit
    SUM(OrderTotal)/SUM(OrderQuantity)

* Fulfillment accuracy
    Order Correct = IF {INCLUDE [OrderNum]:SUM([DeliveredQuantity]} = IF {INCLUDE [OrderNum]:SUM([OrderedQuantity]}
    THEN 1 ELSE 0
    END

    Percent of Correct Orders = {FIXED : SUM(Order Correct)}/COUNTD([OrderNum])

* Lead Time
    
    (Implicit)

    Promised Lead Time - Actual Lead Time

* Inbound Transportation Costs
    
    Per Unit Shipping = 
    {FIXED [Product Name]: SUM([ItemShippingCost])}/{FIXED [Product Name]: SUM([Quantity])}

## Transportation
* Average delivery time
    - Implicit measure

* On-time Delivery Percentage
    On Time Delivery =
        IF {FIXED [OrderNum]: SUM(DeliveryDiff)} = 0 THEN 1 ELSE 0 END

    PctOrdersOnTIme =
        {FIXED [CustName]: SUM(OnTime Delivery)}/{FIXED [CustName]: COUNTD([OrderNum])}

* Track Cost per Mile
    
    Outbound CPMile = 
    SUM(DelFuelCost)/SUM(DelMiles)

* Monitor freight bill accuracy

    FreightBillAccurate = 
    IF{FIXED [OrderNum]: SUM(DelQuantity)} = {FIXED [OrderNum]: SUM([OrderQuant])} THEN 1 ELSE 0 END

    PercentFbAccurate

    {FIXED: SUM(FreightBillAccurate)}/{FIXED: COUNTD([OrderNum])}

* Calculate perfect order percentage

    OnTime delivery = 
    IF{FIXED [OrderNum]: SUM(Days late)} = 0 THEN 1 ELSE 0 END

    IsPerfectOrder = 
    OnTimeDelivery * FreightBillAccurate

    PctPerfectOrder
    {FIXED: SUM(IsPerfectOrder}/{FIXED: COUNTD([OrderNum])}

## Tracking Inventory
* Days of Inventory on Hand

    DaysOnHand = CurrentInventory/DailyDemand

* Annual inventory turns
    LOD: FIXED ProductName

    AveInventoryValue = 
    ProductAveInventory * ProductCogs

    SalesRevCogs = 
    ProductSales * ProductCost

    InventoryTurns
    SalesRevCogs/AveInventoryValue

* Display average age of inventory

    Aged Days per Order = 
        Inv Age Days * Inv Quant

    AvgInvAgeDays
    SUM(Aged Days per Order)/SUM(Inv Quant)

* Backorder Percentage

    BackOrderPct
        SUM(IsBackOrder)/COUNTROWS


## Managing Quality
* Defect Rates
    LOD: Fixed Component Name
    Defect Rate = Defect Count/Unit Count

* Ave response time
    Implict avg

* Rate of Returns
    Implicit av

* Customer retention rate

    Cust Retention = IF Comparison Date - Previous Date <= 365 THEN 1 ELSE 0 END

    Implicit Avg

## Strategic Dashboard
* Cash conversion cycle
    CCC = Days of Inventory Outstanding + Days of Sales Outstanding - Days of Payables Outstanding
    CCC = DIO + DSO - DPO

    DIO = Ave Invty/COGS * 365
    DSO = Ave AR/(Sales/365)
    DPO = Ave AP/(COGS/365) 

* Customer satisfaction level
    Rating9or10 = 
    IF Rating >= 9 THEN 1 ELSE 0 END

    Implicit Avg

* Contribution margin per product
    LOD Fixed ProductName
    ProductPrice - Product Cost

* Revenue trends
    Just a line chart

* Sales vol trends

    Just a line chart