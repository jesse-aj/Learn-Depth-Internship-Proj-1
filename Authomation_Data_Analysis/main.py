from utils.processing import read_data, clean_data, process_data
from utils.analysis import total_revenue_by_category, top_selling_product, monthly_sales_trends
from utils.reporting import generate_report, generate_charts



df = read_data("data/sales.csv")
df = clean_data(df)
df = process_data(df)

tot_rev = total_revenue_by_category(df)
top_sale = top_selling_product(df)
trends = monthly_sales_trends(df)



while True:
    print("===== Sales Analytics System =====")
    print("1. View dataset overview")
    print("2. View total revenue by category")
    print("3. View top selling product")
    print("4. View monthly sales trends")
    print("5. Generate report (CSV)")
    print("6. Generate charts")
    print("7. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print(df.head())
        
    elif choice == "2":
        print("=== Total Revenue by Category ===")
        print(tot_rev)

    elif choice == "3":
        print("\n=== Top Selling Product ===")
        print(top_sale)

    elif choice == "4":
        print("\n=== Monthly Sales Trend ===")
        print(trends)

    elif choice == "5":
        report = generate_report(tot_rev, top_sale, trends)
        print("Report saved to reports/output.csv")

    elif choice == "6":
        generate_charts(tot_rev, trends)
        print("Charts saved to reports/")


    elif choice == "7":
        break  # exits the loop