import pandas as pd

# 1. Define the exact dataset from the assignment
data = {
    "Year": [2001, 2003, 2004, 2002, 2005, 2002, 2002, 2004, 2004, 2001, 2002, 2003, 2005, 2004, 2001, 2001, 2003, 2005, 2002],
    "Product": ["Books", "Machine", "Table", "Chair", "TV", "Phones", "Machine", "TV", "Phones", "Chair", "Table", "Laptop", "Chair", "Books", "Pen", "Car", "Laptop", "Table", "Car"],
    "Region": ["East", "West", "South", "North", "North", "East", "South", "West", "East", "North", "East", "East", "North", "North", "South", "West", "West", "South", "South"],
    "Name": ["Riya", "Jai", "Mohini", "Gautam", "Aastha", "Riya", "Suvashree", "Mohini", "Jai", "Aakriti", "Gautam", "Naman Jain", "Ronit", "Naman Jain", "Ronit", "Rohit", "Supriya", "Suvashree", "Jayanti"],
    "Sales": [162, 200, 350, 770, 540, 1600, 170, 920, 573, 856, 491, 986, 863, 220, 819, 407, 100, 51, 220],
    "Profit": [50, 45, 76, 100, 49, 1009, 60, 789, 98, 349, 312, 581, 544, 654, 710, 38, 78, 7, 89]
}

df = pd.DataFrame(data)

# Pre-calculate grouped data for charting
df_yearly = df.groupby("Year")[["Sales", "Profit"]].sum().reset_index()
df_regional = df.groupby("Region")["Sales"].sum().reset_index()

# Filter North and East Region data
df_filtered = df[df["Region"].isin(["North", "East"])]

# Initialize Excel Writer using xlsxwriter engine
file_name = "Adstacks_Media_Advanced_Solution.xlsx"
with pd.ExcelWriter(file_name, engine="xlsxwriter") as writer:
    workbook = writer.book

    # --- SHEET 1: MASTER DATA & LIVE FORMULAS ---
    df.to_excel(writer, sheet_name="Master Data", index=False)
    worksheet = writer.sheets["Master Data"]
    
    # Task 3 & Task 5: Inject Excel Formulas for Sales * 2 and NAME (CAPS)
    worksheet.write("G1", "Sales * 2")
    worksheet.write("H1", "NAME (CAPS)")
    
    for row_num in range(2, len(df) + 2):
        # Excel rows are 1-indexed, so row_num 2 is Excel row 2
        worksheet.write_formula(f"G{row_num}", f"=E{row_num}*2")
        worksheet.write_formula(f"H{row_num}", f'=UPPER(D{row_num})')
    
    # Task 1 & Task 4: Inject SUM and AVERAGE formulas
    last_row = len(df) + 1
    worksheet.write(f"D{last_row + 2}", "Total Sum")
    worksheet.write_formula(f"E{last_row + 2}", f"=SUM(E2:E{last_row})")
    worksheet.write_formula(f"F{last_row + 2}", f"=SUM(F2:F{last_row})")
    
    worksheet.write(f"D{last_row + 3}", "Average Sales")
    worksheet.write_formula(f"E{last_row + 3}", f"=AVERAGE(E2:E{last_row})")

    # --- SHEET 2: FILTERED DATA (Task 2) ---
    df_filtered.to_excel(writer, sheet_name="North & East Filter", index=False)
    
    # --- SHEET 3: LINE GRAPH (Task 6) ---
    df_yearly.to_excel(writer, sheet_name="Yearly Chart Data", index=False)
    chart_sheet_line = writer.sheets["Yearly Chart Data"]
    
    # Create Line Chart Object
    line_chart = workbook.add_chart({'type': 'line'})
    line_chart.add_series({
        'name':       'Sales',
        'categories': ['Yearly Chart Data', 1, 0, len(df_yearly), 0],
        'values':     ['Yearly Chart Data', 1, 1, len(df_yearly), 1],
    })
    line_chart.add_series({
        'name':       'Profit',
        'categories': ['Yearly Chart Data', 1, 0, len(df_yearly), 0],
        'values':     ['Yearly Chart Data', 1, 2, len(df_yearly), 2],
    })
    line_chart.set_title({'name': 'Sales and Profit by Year'})
    line_chart.set_x_axis({'name': 'Year'})
    line_chart.set_y_axis({'name': 'Sales & Profit (USD)'})
    chart_sheet_line.insert_chart('E2', line_chart)

    # --- SHEET 4: PIE CHART (Task 7) ---
    df_regional.to_excel(writer, sheet_name="Regional Chart Data", index=False)
    chart_sheet_pie = writer.sheets["Regional Chart Data"]
    
    # Create Pie Chart Object
    pie_chart = workbook.add_chart({'type': 'pie'})
    pie_chart.add_series({
        'name': 'Regional Sales',
        'categories': ['Regional Chart Data', 1, 0, len(df_regional), 0],
        'values':     ['Regional Chart Data', 1, 1, len(df_regional), 1],
        'data_labels': {'percentage': True, 'category': True}
    })
    pie_chart.set_title({'name': 'Total Sales by Region'})
    chart_sheet_pie.insert_chart('D2', pie_chart)

print(f"Deep solution generated successfully: {file_name}")