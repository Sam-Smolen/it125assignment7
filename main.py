import pandas as pd

input_url = "it125assignment7/assignment_seven.csv"
output_url = "it125assignment7/output.csv"

try: 
    # Read the CSV file into a Pandas Dataframe
    df = pd.read_csv(input_url) 
    

    # Print info about the input Dataframe
    print(df.info())
    
    #Remove rows that have empty cells
    new_df = df.dropna()
    
    # Print info about the output Dataframe
    print(new_df.info())

    #Clean full_name column
    for x in df.index:
        new_df.loc[x, "full_name"] = "NA"

    # Write pandas dataframe to output.csv
    new_df.to_csv(output_url)


except Exception as e:
    print("Unexpected exception:" + str(e))