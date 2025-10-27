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































practice_emp_Dset = {
    'Employee': [
        'Rhonda Williams', 'James Miller', 'Kevin Smith', 'David Jones', 'Heidi Lewis', 
        'Michael Johnson', 'Anthony Taylor', 'David Miller', 'Daniel Williams', 'Scott Anderson', 
        'David Jones', 'Robert Garcia', 'Jason Brown', 'William Smith', 'Melissa Smith', 
        'Nicole Smith', 'Joseph Rodriguez', 'Thomas Smith', 'James Smith', 'Thomas Allen', 
        'Robert Smith', 'Michelle Jones', 'Michael Williams', 'John Miller', 'John Smith', 
        'Jennifer Smith', 'Mary Johnson', 'David Johnson', 'Mark Williams', 'Mary Williams', 
        'Mary Miller', 'Robert Williams', 'Michael Smith', 'Michael Johnson', 'William Williams', 
        'Mark Smith', 'Mary Smith', 'Linda Jones', 'Jennifer Williams', 'Robert Brown', 
        'Robert Johnson', 'William Johnson', 'Michael Davis', 'James Williams', 'Michael Brown', 
        'Patricia Johnson', 'James Johnson', 'Richard Johnson', 'Richard Williams', 'David Smith', 
        'William Jones', 'Richard Smith', 'Richard Miller', 'Patricia Williams', 'Jennifer Johnson', 
        'David Davis', 'Elizabeth Johnson', 'Barbara Johnson', 'Linda Smith', 'Patricia Smith', 
        'Linda Williams', 'Susan Smith', 'Robert Jones', 'Jennifer Brown', 'Patricia Jones', 
        'Elizabeth Smith', 'Barbara Williams', 'Mary Brown', 'Barbara Smith', 'Elizabeth Jones', 
        'Elizabeth Miller', 'Susan Johnson', 'Maria Smith', 'Linda Johnson', 'Linda Brown', 
        'Jennifer Jones', 'Mary Jones', 'Susan Williams', 'Susan Jones', 'Barbara Brown', 
        'Maria Williams', 'Sarah Johnson', 'Elizabeth Williams', 'Maria Garcia', 'Maria Rodriguez', 
        'Maria Jones', 'Karen Smith', 'Karen Williams', 'Karen Johnson', 'Sarah Williams', 
        'Maria Martinez', 'Sarah Jones', 'Jessica Smith', 'Karen Jones', 'Nancy Smith', 
        'Jessica Johnson', 'Nancy Williams', 'Jessica Williams', 'Sarah Miller', 'Nancy Jones', 
        'Lisa Smith', 'Betty Smith', 'Lisa Williams', 'Betty Williams', 'Nancy Johnson', 
        'Lisa Jones', 'Betty Johnson', 'Helen Williams', 'Sandra Smith', 'Dorothy Smith', 
        'Helen Smith', 'Sandra Johnson', 'Dorothy Johnson', 'Sandra Williams', 'Helen Johnson', 
        'Dorothy Williams', 'Lisa Johnson', 'Sandra Jones', 'Helen Jones', 'Betty Jones', 
        'Dorothy Jones', 'Margaret Smith', 'Ashley Smith', 'Margaret Williams', 'Kimberly Smith', 
        'Ashley Williams', 'Emily Smith', 'Margaret Johnson', 'Kimberly Williams', 'Ashley Johnson', 
        'Emily Williams', 'Kimberly Johnson', 'Margaret Jones', 'Emily Johnson', 'Ashley Jones', 
        'Amanda Smith', 'Kimberly Jones', 'Melissa Smith', 'Emily Jones', 'Amanda Williams', 
        'Melissa Williams', 'Amanda Johnson', 'Deborah Smith', 'Melissa Johnson', 'Amanda Jones', 
        'Carol Smith', 'Deborah Williams', 'Michelle Smith', 'Melissa Jones', 'Carol Williams'
    ],
    'Department': [
        'Sales', 'Support', 'Engineering', 'Marketing', 'Engineering', 'Engineering', 
        'Sales', 'Sales', 'Sales', 'Engineering', 'Support', 'Engineering', 
        'Support', 'Engineering', 'Support', 'Support', 'Support', 'Sales', 
        'Engineering', 'Sales', 'Engineering', 'IT', 'Sales', 'Sales', 
        'Engineering', 'Marketing', 'Sales', 'IT', 'Finance', 'Engineering', 
        'Support', 'Sales', 'Support', 'Support', 'Sales', 'Engineering', 
        'Support', 'Engineering', 'Marketing', 'Engineering', 'Engineering', 'Engineering', 
        'IT', 'Marketing', 'Sales', 'Engineering', 'Support', 'Engineering', 
        'Engineering', 'Engineering', 'Engineering', 'IT', 'Engineering', 'Sales', 
        'Sales', 'Engineering', 'Sales', 'Engineering', 'Engineering', 'Engineering', 
        'Engineering', 'Sales', 'Engineering', 'Sales', 'Sales', 'Engineering', 
        'Sales', 'Support', 'Marketing', 'Sales', 'Engineering', 'Engineering', 
        'Engineering', 'Support', 'Support', 'Engineering', 'Marketing', 'Engineering', 
        'Marketing', 'Sales', 'Sales', 'Engineering', 'Engineering', 'Engineering', 
        'Engineering', 'Marketing', 'Sales', 'IT', 'Engineering', 'Engineering', 
        'Support', 'Sales', 'Sales', 'Engineering', 'Support', 'Marketing', 
        'Sales', 'Support', 'Sales', 'Engineering', 'Support', 'IT', 
        'Engineering', 'Marketing', 'Engineering', 'Support', 'Sales', 'Engineering', 
        'Engineering', 'IT', 'Sales', 'IT', 'Finance', 'Sales', 
        'Sales', 'Sales', 'Support', 'Engineering', 'IT', 'Sales', 
        'Support', 'Marketing', 'Engineering', 'Support', 'Sales', 'IT', 
        'Engineering', 'Support', 'Sales', 'HR', 'Support', 'Support', 
        'Engineering', 'Sales', 'Support', 'IT', 'Sales', 'Engineering', 
        'IT', 'Marketing', 'Sales', 'Support', 'Support', 'HR', 
        'Finance', 'Engineering', 'Engineering'
    ],
    'Status': [
        'Full-Time', 'Full-Time', 'Full-Time', 'Part-Time', 'Full-Time', 'Full-Time', 
        'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 
        'Full-Time', 'Full-Time', 'Part-Time', 'Full-Time', 'Full-Time', 'Full-Time', 
        'Full-Time', 'Part-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Part-Time', 
        'Full-Time', 'Part-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 
        'Full-Time', 'Full-Time', 'Part-Time', 'Full-Time', 'Full-Time', 'Full-Time', 
        'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 
        'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Part-Time', 'Full-Time', 
        'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Part-Time', 'Full-Time', 
        'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 
        'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 
        'Part-Time', 'Full-Time', 'Full-Time', 'Part-Time', 'Full-Time', 'Full-Time', 
        'Full-Time', 'Full-Time', 'Part-Time', 'Full-Time', 'Full-Time', 'Full-Time', 
        'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 
        'Full-Time', 'Part-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 
        'Full-Time', 'Part-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 
        'Full-Time', 'Part-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 
        'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 
        'Full-Time', 'Part-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 
        'Full-Time', 'Full-Time', 'Part-Time', 'Full-Time', 'Full-Time', 'Full-Time', 
        'Full-Time', 'Full-Time', 'Part-Time', 'Full-Time', 'Full-Time', 'Full-Time', 
        'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 
        'Part-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Part-Time', 'Full-Time', 
        'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 'Full-Time', 
        'Full-Time', 'Full-Time', 'Full-Time'
    ],
    'Salary': [
        86700, 71500, 114600, 37200, 115100, 107600, 101100, 89300, 68700, 
        110600, 56300, 110900, 60800, 116600, 31000, 51300, 75500, 110600, 
        116100, 58100, 120500, 89000, 93500, 35000, 142400, 46100, 77500, 
        88200, 91500, 112100, 65600, 105900, 27300, 56900, 114900, 108300, 
        57600, 114700, 84300, 102200, 122200, 128400, 98900, 84000, 112300, 
        134200, 28100, 129700, 114900, 137400, 147500, 83100, 69600, 89100, 
        100900, 149300, 77300, 115300, 109700, 105600, 137200, 84000, 100400, 
        113000, 60400, 139500, 47700, 60800, 88200, 43900, 124200, 136200, 
        99600, 122200, 25200, 128100, 73100, 106000, 106200, 127600, 108800, 
        105200, 92400, 112200, 37400, 123800, 107600, 104500, 140200, 65500, 
        30600, 120500, 76200, 71500, 80800, 61500, 26900, 100700, 60800, 
        90200, 73600, 107300, 41200, 124300, 71900, 113300, 102000, 115200, 
        103800, 99600, 95900, 68000, 83900, 32300, 120600, 87400, 103200, 
        75800, 45100, 105800, 107100, 86800, 26600, 108800, 66300, 65800, 
        64600, 68000, 76200, 60900, 50600, 90700, 109800, 40100, 68600, 
        74400, 77400, 57100, 91500, 64200, 131700
    ],
    'Projects': [
        3, 3, 5, 2, 8, 4, 3, 3, 4, 7, 2, 7, 2, 5, 1, 3, 1, 4, 6, 2, 7, 5, 5, 2, 
        7, 3, 5, 4, 3, 7, 2, 5, 1, 2, 6, 8, 1, 5, 6, 6, 7, 6, 4, 4, 5, 7, 1, 7, 
        7, 6, 7, 6, 3, 4, 3, 5, 4, 7, 7, 5, 4, 5, 6, 4, 7, 2, 5, 4, 1, 7, 8, 
        5, 5, 1, 6, 2, 6, 4, 6, 5, 8, 6, 6, 2, 7, 5, 5, 5, 3, 2, 5, 3, 5, 5, 2, 
        1, 4, 2, 4, 3, 5, 2, 8, 3, 8, 4, 6, 6, 5, 6, 3, 4, 1, 6, 4, 4, 2, 2, 6, 
        6, 5, 1, 5, 1, 2, 3, 1, 3, 3, 2, 6, 2, 3, 2, 6, 3, 2, 5, 5, 1, 3, 2, 
        3, 7, 5
    ]
}