import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def read_csv(filepath): #Task 1: read CSV file and return data as a list of dictionaries
    try:
        with open(filepath, 'r') as file:
            return list(csv.DictReader(file))
    except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError): #error-handling
        print("Error: Unable to read file.")
        return None

def get_sales(data, key='sales'): #Task 2: extract numerical sales data from a given key
    return [int(row[key]) for row in data if row[key].isdigit()]

def total_sales(data): #Task 3: calculate and print total sales
    total = sum(get_sales(data))
    print(f'Total Sales: ${total:.2f}')
    return total

    def average_sales(data): #Extended 1: calculates and print average monthly sales
    sales = get_sales(data)
    avg = sum(sales) / len(sales) if sales else 0
    print(f'Average Sales per Month: ${avg:.2f}')
    return avg

    def min_max_sales(data): #Ext. 2: find and print months with highest and lowest sales
    sales = get_sales(data)
    months = [row['month'] for row in data]
    
    if sales:
        max_idx, min_idx = sales.index(max(sales)), sales.index(min(sales))
        print(f'Highest Sales: ${sales[max_idx]} in {months[max_idx]}.')
        print(f'Lowest Sales: ${sales[min_idx]} in {months[min_idx]}.')
        return sales[max_idx], months[max_idx], sales[min_idx], months[min_idx]
    
    return None, None, None, None

def percentage_changes(data): #Ext. 3: calculate monthly percentage changes in sales
    sales = get_sales(data)
    return [((sales[i] - sales[i - 1]) / sales[i - 1]) * 100 for i in range(1, len(sales))] if len(sales) > 1 else []

def plot_sales(data): #Ext.4: create a bar plot of monthly sales
    df = pd.DataFrame(data)
    df['sales'] = pd.to_numeric(df['sales'], errors='coerce').dropna().astype(int)
    
    sns.barplot(x='month', y='sales', data=df, palette='coolwarm')
    plt.title('Monthly Sales')
    plt.xticks(rotation=45)
    plt.show()

def plot_percentage_changes(data): #Ext. 5: create a line plot of percentage changes in sales
    changes = percentage_changes(data)
    months = [row['month'] for row in data][1:]

    if changes:
        sns.lineplot(x=months, y=changes, marker='o', color='b')
        plt.title('Monthly Percentage Changes in Sales')
        plt.xticks(rotation=45)
        plt.show()

def process_vehicle_data(filepath): #Ext 6 Using Different Spreadsheet: reads, processes, and visualizes vehicle sales data from CSV
    data = pd.read_csv(filepath)

    if not {'sellingprice', 'saledate'}.issubset(data.columns):
        print("Error: Missing required columns.")
        return
    
    data['sellingprice'] = pd.to_numeric(data['sellingprice'], errors='coerce').dropna()
    total = data['sellingprice'].sum()
    avg = data['sellingprice'].mean()
    max_sale, min_sale = data['sellingprice'].max(), data['sellingprice'].min()

    print(f"Total Sales Revenue: ${total:.2f}")
    print(f"Average Sale Price: ${avg:.2f}")
    print(f"Highest Sale Price: ${max_sale}, Lowest Sale Price: ${min_sale}")

    data['saledate'] = pd.to_datetime(data['saledate'], errors='coerce')
    data = data.dropna(subset=['saledate']).sort_values('saledate')

    plt.figure(figsize=(10, 5))
    sns.lineplot(x=data['saledate'], y=data['sellingprice'], marker='o')
    plt.xticks(rotation=45)
    plt.title("Vehicle Sales Price Trend Over Time")
    plt.show()

def main():
    sales_filepath = 'sales_data.csv'
    vehicle_filepath = 'car_prices.csv'

    # Process Monthly Sales Data
    sales_data = read_csv(sales_filepath)
    if sales_data:
        total_sales(sales_data)
        average_sales(sales_data)
        min_max_sales(sales_data)
        plot_sales(sales_data)
        plot_percentage_changes(sales_data)

    # Process Vehicle Sales Data
    process_vehicle_data(vehicle_filepath)

if __name__ == "__main__":
    main()
