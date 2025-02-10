import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def read_data(file_path): #read vehicle sales data from a CSV file with error handling
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: Could not parse CSV file.")
        return None

    # Ensure required columns exist
    required_columns = {'sellingprice', 'saledate'}
    if not required_columns.issubset(data.columns):
        print("Error: CSV file is missing required columns:", required_columns - set(data.columns))
        return None

    return data

def collect_sales(data): #extract prices by ensuring numeric values and handling missing data
    data['sellingprice'] = pd.to_numeric(data['sellingprice'], errors='coerce')  # convert non-numeric to NaN
    return data['sellingprice'].dropna().tolist()  # drop missing values

def calculate_total_sales(sales):
    
    return sum(sales) if sales else 0 

def calculate_statistics(data): #average, highest/lowest sales and percentage changes
    if data.empty:
        return 0, 0, 0  # return defaults if empty

    data['sellingprice'] = pd.to_numeric(data['sellingprice'], errors='coerce')
    data.dropna(subset=['sellingprice'], inplace=True)

    data['Monthly Change (%)'] = data['sellingprice'].pct_change() * 100
    avg_sales = data['sellingprice'].mean() #mean means average
    highest_sale = data['sellingprice'].max()
    lowest_sale = data['sellingprice'].min()

    return avg_sales, highest_sale, lowest_sale

def generate_summary(data, output_file='vehicle_sales_summary.csv'): #write the summary results to a new CSV file
    if data is not None and not data.empty:
        data.to_csv(output_file, index=False)
        print(f"Summary saved to {output_file}")
    else:
        print("No valid data to save.")

def visualise_sales(data): #creates a sales trend graph based on sale dates, handling bad dates
    if data is None or data.empty:
        print("No data available for visualisation.")
        return

    # convert saledate to datetime, replacing invalid dates with NaN
    data['saledate'] = pd.to_datetime(data['saledate'], errors='coerce', utc=True)

    # drop rows where the date conversion failed (NaN)
    data.dropna(subset=['saledate'], inplace=True)

    # sort by date after cleaning
    data = data.sort_values(by='saledate')

    # ensure there are valid dates to plot
    if data.empty:
        print("No valid dates available for visualisation.")
        return

    plt.figure(figsize=(12, 6))
    sns.lineplot(x=data['saledate'], y=data['sellingprice'], marker='o', label='Selling Price')
    plt.xticks(rotation=45)
    plt.xlabel("Sale Date")
    plt.ylabel("Selling Price")
    plt.title("Vehicle Sales Price Trend Over Time")
    plt.legend()
    plt.show()

def main():
    file_path = 'car_prices.csv'  # update with actual file path
    data = read_data(file_path)
    
    if data is None:
        return  # stop execution if file is missing or unreadable
    
    sales = collect_sales(data)
    total_sales = calculate_total_sales(sales)
    
    print(f"Total Sales Revenue: ${total_sales:.2f}")
    
    avg_sales, highest_sale, lowest_sale = calculate_statistics(data)
    print(f"Average Sale Price: ${avg_sales:.2f}")
    print(f"Highest Sale Price: ${highest_sale}")
    print(f"Lowest Sale Price: ${lowest_sale}")
    
    generate_summary(data)
    visualise_sales(data)

if __name__ == "__main__":
    main()
