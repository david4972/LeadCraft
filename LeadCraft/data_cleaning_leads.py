# Written by David Okoronkwo
import os
import string

import numpy as np
import pandas as pd
from sqlalchemy import create_engine

'''
db_name = 'lead_data.db'
if os.path.exists(db_name):
    os.remove(db_name)
    print(db_name + " removed")
'''


class DataGeneration:
    def __init__(self, num_samples=500):
        self.num_samples = num_samples
        self.prospect_ids = [f"id_{i}" for i in range(num_samples)]
        self.lead_numbers = np.random.randint(579533, 660738, num_samples)
        self.first_names = np.array(
            ["John", "Jane", "Alice", "Bob", "Charlie", "Emily", "Frank", "Grace", "Henry", "Isabel"])
        self.last_names = np.array(
            ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"])

        self.names = self.generate_random_names()

        self.lead_origins = np.random.choice(["API", "Landing Page Submission", "Lead Add Form"], num_samples,
                                             p=[0.3, 0.5, 0.2])
        self.lead_sources = np.random.choice(
            ["Olark Chat", "Organic Search", "Direct Traffic", "Google", "Welingak Website", "Referral Sites",
             "Facebook", "bing"], num_samples)

        self.lead_scores = np.random.normal(103.32, 105.65, num_samples).astype(int)
        self.engagement_scores = np.random.normal(6.37, 23.98, num_samples).astype(int)
        self.phone_numbers = np.random.randint(0000000000, 9999999999, num_samples)
        self.emails = [f"{''.join(np.random.choice(list(string.ascii_lowercase), size=8))}@example.com" for _ in
                       range(num_samples)]
        # self.lead_grades = np.random.choice(["A", "B", "C", "D"], num_samples, p=[0.1, 0.7, 0.15, 0.05])
        self.total_visits = np.random.poisson(3.45, num_samples)
        self.average_time_per_visit = np.random.normal(0, 600.00, num_samples).astype(int)

    def generate_random_names(self):
        first_name_choices = np.random.choice(self.first_names, self.num_samples)
        last_name_choices = np.random.choice(self.last_names, self.num_samples)
        random_names = np.char.add(first_name_choices, ' ')
        random_names = np.char.add(random_names, last_name_choices)
        return random_names

    def to_dataframe(self):
        data = {
            "Prospect ID": self.prospect_ids,
            "Lead Number": self.lead_numbers,
            "Name": self.names,
            "Lead Origin": self.lead_origins,
            "Lead Source": self.lead_sources,
            "Lead Score": self.lead_scores,
            "Engagement Score": self.engagement_scores,
            "Phone Numbers": self.phone_numbers,
            "Emails": self.emails,
            # "Lead Grade": self.lead_grades,
            "Total Visits": self.total_visits,
            "Average Time Per Visit": self.average_time_per_visit
        }
        df = pd.DataFrame(data)

        # Print the data and labels
        print("Data Labels: ", df.columns.tolist())
        print("Sample Data: ", df.head())

        return df

    def to_sqlite(self, db_name='lead_data.db', table_name='leads'):
        df = self.to_dataframe()
        engine = create_engine(f'sqlite:///{db_name}')
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Data has been saved to the SQLite database '{db_name}' in the '{table_name}' table.")


ren = DataGeneration()
ren.to_sqlite()

'''
def clean_sort_data_csv():
    # Load the CSV file
    csv_file_path = 'SLGDataset - SLG.csv'
    data = pd.read_csv(csv_file_path)

    # Clean column names (remove spaces and replace with underscores for consistency)
    data.columns = data.columns.str.replace(' ', '_')

    # Create a SQLite database
    db_name = 'leads_data.db'
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Get the columns from the DataFrame
    columns = data.columns.tolist()

    # Create a table (assuming all columns are text for simplicity)
    table_name = 'leads'
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        {', '.join([f'{col} TEXT' for col in columns])}
    );
    """
    cursor.execute(create_table_query)

    # Insert the CSV data into the table
    for index, row in data.iterrows():
        row_data = [str(val) for val in row.tolist()]
        insert_query = f"""
        INSERT INTO {table_name} ({', '.join(columns)})
        VALUES ({', '.join(['?' for _ in columns])});
        """
        cursor.execute(insert_query, row_data)

    # Commit and close the connection
    conn.commit()

    # Query the database to retrieve and print the data
    select_query = f"SELECT * FROM {table_name};"
    cursor.execute(select_query)
    rows = cursor.fetchall()

    # Print the data
    print("Data in the database:")
    for row in rows:
        print(row)

    conn.close()

    print(f"Data from {csv_file_path} has been inserted into the {table_name} table in {db_name}.")

# Call the function to execute the data cleaning and insertion
clean_sort_data_csv()
'''
