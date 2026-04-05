import pandas as pd #type: ignore
import matplotlib.pyplot as plt #type: ignore

def generate_report(tot_rev, top_sale, trends):
    with open("reports/output.csv", "w") as f:
        f.write("=== Total Revenue by Category ===\n")
        tot_rev.to_csv(f)
        
        f.write("\n=== Top Selling Product ===\n")
        f.write(f"{top_sale}\n")
        
        f.write("\n=== Monthly Sales Trend ===\n")
        trends.to_csv(f)


def generate_charts(tot_rev, trends):

    # Chart 1 - Revenue by Category
    plt.figure(figsize=(8, 5))
    plt.bar(tot_rev.index, tot_rev.values, color="skyblue")
    plt.title("Revenue by Category")
    plt.xlabel("Category")
    plt.ylabel("Revenue")
    plt.savefig("reports/category_revenue.png")
    plt.close()

     # Chart 2 - Monthly Sales Trend
    plt.figure(figsize=(8, 5))
    plt.plot(trends.index, trends.values, marker="o", color="green")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.savefig("reports/monthly_trend.png")
    plt.close()

    print("Charts saved to reports/")

    

    



