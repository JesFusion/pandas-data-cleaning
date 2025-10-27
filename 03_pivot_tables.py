import pandas as pd


raw_data = {
    "Employee": ["John", "Mary", "Peter", "Jane", "Tom", "Lisa"],
    "Department": [
        "Sales",
        "Engineering",
        "Sales",
        "Engineering",
        "Marketing",
        "Marketing",
    ],
    "Status": [
        "Full-Time",
        "Part-Time",
        "Full-Time",
        "Full-Time",
        "Part-Time",
        "Full-Time",
    ],
    "Salary": [90000, 80000, 95000, 110000, 60000, 75000],
    "Projects": [5, 3, 7, 6, 4, 5],
}


pra_dataset = pd.DataFrame(raw_data)


print(f"""
============================= Original DataFrame =============================
      
{pra_dataset}


============================= Multi-level GroupBy (Average Salary and Projects) =============================

{pra_dataset.groupby(["Department", "Status"]).mean(numeric_only=True)}
""")


pivot_average_sal = pd.pivot_table(
    data=pra_dataset,
    index="Department",
    columns="Status",
    values="Salary",
    aggfunc="mean",
)


print(f"""
============================= Pivot Table (Average Salary) =============================
      
{pivot_average_sal}


============================= More Complex Pivot Table (Sum of Projects) =============================

{
    pd.pivot_table(
        data=pra_dataset,
        index="Department",
        columns="Status",
        values="Projects",
        aggfunc="sum",
    )
}
""")


pv_mul_table = pd.pivot_table(
    data=pra_dataset,
    index="Department",
    columns="Status",
    # Using a dictionary for aggfunc allows specifying different aggregation functions for each column.
    aggfunc={"Salary": "mean", "Projects": "sum"},
)

print(f"""
============================= pivot table with Multiple Values =============================
      
{pv_mul_table}
""")
