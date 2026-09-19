import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_dashboard_visuals():
    print("Loading cleaned dataset...")
    input_path = 'data/clean/cleaned_hr_dataset.csv'
    
    if not os.path.exists(input_path):
        print(f"Error: Could not find {input_path}.")
        return

    df = pd.read_csv(input_path)
    
    # Create output directory for visuals
    os.makedirs('dashboards/visuals', exist_ok=True)
    
    # --- 1. KPI Calculations ---
    total_employees = len(df)
    active_employees = len(df[df['Attrition'] == 'No'])
    exited_employees = len(df[df['Attrition'] == 'Yes'])
    attrition_rate = (exited_employees / total_employees) * 100
    avg_salary = df[df['Attrition'] == 'No']['Salary'].mean()
    
    print("\n" + "-" * 40)
    print("🎯 HR DASHBOARD KPIs")
    print("-" * 40)
    print(f"Total Employees:    {total_employees}")
    print(f"Active Employees:   {active_employees}")
    print(f"Exited Employees:   {exited_employees}")
    print(f"Attrition Rate:     {attrition_rate:.2f}%")
    print(f"Avg Active Salary:  ${avg_salary:,.2f}")
    print("-" * 40)
    
    # --- 2. Visualization: Attrition by Department ---
    plt.figure(figsize=(10, 6))
    dept_attrition = df[df['Attrition'] == 'Yes'].groupby('Department').size() / df.groupby('Department').size() * 100
    dept_attrition = dept_attrition.sort_values(ascending=False)
    dept_attrition.plot(kind='bar', color='#e74c3c', edgecolor='black')
    plt.title('Attrition Rate by Department (%)', fontsize=14, fontweight='bold')
    plt.ylabel('Attrition Rate (%)')
    plt.xlabel('Department')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('dashboards/visuals/1_attrition_by_department.png')
    plt.close()
    
    # --- 3. Visualization: Attrition vs Job Satisfaction ---
    plt.figure(figsize=(10, 6))
    sat_attrition = df.groupby('JobSatisfaction')['AttritionFlag'].mean() * 100
    sat_attrition.plot(kind='line', marker='o', color='#9b59b6', linewidth=2, markersize=8)
    plt.title('Attrition Rate vs. Job Satisfaction', fontsize=14, fontweight='bold')
    plt.ylabel('Attrition Rate (%)')
    plt.xlabel('Job Satisfaction Rating (1 = Low, 5 = High)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('dashboards/visuals/2_attrition_vs_satisfaction.png')
    plt.close()

    print("\n✅ Visualizations successfully generated and saved to the 'dashboards/visuals/' folder!")

if __name__ == "__main__":
    generate_dashboard_visuals()