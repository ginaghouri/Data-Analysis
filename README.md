# Data Science 
Spreadsheet Analysis: Group 1 Project

This script is a structured program that processes both:

1️⃣ Monthly Sales Data (sales_data.csv)
2️⃣ Vehicle Sales Data (car_prices.csv)

How It Works

1️Reads Sales Data (sales_data.csv)
·Calculates total, average, highest, and lowest sales.
·Generates bar and line plots for monthly sales and percentage changes.
2️Reads Vehicle Sales Data (car_prices.csv)
·Extracts total revenue, average, highest, and lowest sale price.
·Plots a trend graph showing vehicle sales over time.
3️Displays results
·Prints sales insights.
·Shows clear, readable visualisations.

🔹 Example Output
📌 Console Output:

Total Sales: $125000.00
Average Sales per Month: $10416.67
Highest Sales: $15000 in June.
Lowest Sales: $8000 in January.
Total Sales Revenue: $500000.00
Average Sale Price: $20000.00
Highest Sale Price: $50000, Lowest Sale Price: $5000

📊 Generated Plots:

✔ Bar Chart of Monthly Sales
✔ Line Chart of Percentage Sales Change
✔ Vehicle Sales Trend Over Time

🔹 Key Optimisations:

✅ Merged duplicate logic
·Created get_sales() to extract numerical sales values (avoids repetition).
·Simplified sales calculations using built-in Pandas and Python methods.
✅ Improved error handling
·read_csv() gracefully handles missing files or bad data.
·Ensures sellingprice and saledate exist before processing vehicle data.
✅ Better structure
·process_vehicle_data() handles vehicle sales in one function.
·main() processes both datasets in a clear sequence.
✅ Enhanced efficiency
·Uses Pandas for filtering, conversion, and plotting (faster than manual loops).
·Reduced unnecessary prints and redundant operations.

Conclusion
This merged script efficiently processes both monthly sales & vehicle sales, making it an ideal solution for sales analysis.
✅ Concise & Maintainable – No duplicate logic, well-structured functions.
✅ Flexible – Can process multiple datasets without modification.
✅ Fast & Efficient – Uses Pandas for performance optimization.
✅ Scalable – Easy to extend for future enhancements.

🚀 

