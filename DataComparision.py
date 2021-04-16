import datacompy
import pandas as pd
df1 = pd.read_csv(r'D:\Users\kulkarad\Desktop\ISO_B501.csv')
df2 = pd.read_csv(r'D:\Users\kulkarad\Desktop\ISO_EBW1.csv')
compare = datacompy.Compare(
    df1,
    df2,
    # You can also specify a list of columns eg ['policyID','statecode']
    join_columns='ISO_CTRY_CD',
    abs_tol=0,  # Optional, defaults to 0
    rel_tol=0,  # Optional, defaults to 0
    df1_name='Original',  # Optional, defaults to 'df1'
    df2_name='New'  # Optional, defaults to  'df2'
)
print(compare.report())
# compare.report().to_file("Report.html")
# (compare.report().to_file("Report.html")
