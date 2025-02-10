import csv
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def read_data(filepath): #Task 1: read data from given CSV file
    data = []
    with open(filepath, 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data

def totalsales(data): #Tasks 2-3: calculate and output total sales
    sales = [int(row['sales']) for row in data]
    total = sum(sales)
    print('Total sales: {}'.format(total))
    return total

# Extended Part:  

def changes_percentage(data):#Task 1:calculate monthly changes as percentage
    sales = [int(row['sales']) for row in data]
    percentages = []
    for i in range(1, len(sales)):
        previous = sales[i - 1]
        current = sales[i]
        percentage = ((current - previous) / previous) * 100
        percentages.append(percentage)
    return percentages

def averagesales(data):#Task2:calculate average sales per month
    sales = [int(row['sales']) for row in data]
    average = sum(sales) / len(sales)
    print('Average sales per month: {:.2f}'.format(average))
    return average

def min_and_max(data):#Task3:months with highest and lowest sales
    sales = [int(row['sales']) for row in data]
    months = [row['month'] for row in data]
    max_sale = max(sales)
    min_sale = min(sales)
    max_month = months[sales.index(max_sale)]
    min_month = months[sales.index(min_sale)]
    print('Highest sales were {} in {}.'.format(max_sale, max_month))
    print('Lowest sales were {} in {}.'.format(min_sale, min_month))
    return max_sale, max_month, min_sale, min_month

def plot_sales(data): #Task4:generate bar plot for monthly sales
    df = pd.DataFrame(data)
    df['sales'] = df['sales'].astype(int)
    sns.barplot(x='month', y='sales', data=df, palette='coolwarm')
    plt.title('Monthly Sales')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_percentage_changes(data):#Task5:generate line plot for percentage changes in sales
    percentages = changes_percentage(data)
    months = [row['month'] for row in data][1:]
    sns.lineplot(x=months, y=percentages, marker='o', color='b')
    plt.title('Monthly Percentage Changes in Sales')
    plt.xlabel('Month')
    plt.ylabel('Percentage Change')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    #extended using other datasheet from kaggle
    filepath = './car_prices.csv'  #path to uploaded CSV file
    data = read_data(filepath)

    # Required Tasks 1-3
    total = totalsales(data)

    # Extended Tasks 1-5 
    average = averagesales(data)
    max_sale, max_month, min_sale, min_month = min_and_max(data)

    # Visualisations
    plot_sales(data)
    plot_percentage_changes(data)

if __name__ == "__main__":
    main()
