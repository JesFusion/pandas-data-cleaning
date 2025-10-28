import pandas as pd

dataset1 = pd.DataFrame({
    'Employee': ['Alice', 'Bob', 'Carol'],
    'Sales': [100, 150, 50]
}, index = [1, 2, 3])

print(f'''
============================= dataset 1 =============================
      
{dataset1}
''')


dataset2 = pd.DataFrame({
    'Employee': ['David', 'Emily'],
    'Sales': [200, 120]
}, index = [4, 5])


print(f'''
============================= dataset2 =============================
      
{dataset2}


============================= Vertically Stacked (default) =============================

{pd.concat([dataset1, dataset2])}
''')


clean_v_stack = pd.concat([dataset1, dataset2], ignore_index = True)

print(f'''
============================= Vertically Stacked with ignore_index = True =============================
      
{clean_v_stack}
''')

dataset3_l = pd.DataFrame({
    'Location': ['New York', 'London', 'Tokyo', 'Paris', 'Sydney']
}, index = [0, 1, 2, 3, 4])


print(f'''
============================= Location data =============================

{dataset3_l}


============================= Horizontally Stacked (axis = 1) =============================

{pd.concat([clean_v_stack, dataset3_l], axis = 1)}
''')
