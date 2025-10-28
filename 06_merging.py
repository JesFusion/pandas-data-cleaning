import pandas as pd


emp_data = pd.DataFrame(
    {
        "emp_id": [101, 102, 103, 104],
        "Name": ["Alice", "Bob", "Carol", "David"],
        "Department": ["Sales", "Engineering", "Sales", "Marketing"],
    }
)

dept_data = pd.DataFrame(
    {"Department": ["Sales", "Marketing", "HR"], "Manager": ["Chris", "Emily", "Frank"]}
)


print(f"""
============================= Employee table =============================
      
{emp_data}


============================= Department table =============================

{dept_data}


============================= Inner join Result  =============================

{pd.merge(emp_data, dept_data, on="Department", how="inner")}

The above is the "inner" join. Notice how bob is gone because "Engineering" isn't the Department DataFrame


============================= Left join Result (All employees, bob has NaN)  =============================

{pd.merge(
    emp_data, dept_data,
    on = "Department", how = "left"
)}


============================= Outer Join Result (Everyone is here, lots of NaN)  =============================

{pd.merge(
    emp_data,
    dept_data,
    on = "Department",
    how = "outer"
)}


============================= Right join Result (All employees, bob has NaN)  =============================

{pd.merge(
    emp_data,
    dept_data,
    on = "Department",
    how = "right"
)}
""")
