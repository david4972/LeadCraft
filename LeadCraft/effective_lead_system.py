# Written by David Okoronkwo

import sqlite3
import pandas as pd
import Neural_Network as neu


# takes real data stored in SQL Database and runs it in the Neural Network
# [Average Time Per
#         Visit]
class ELSystem:

    @staticmethod
    def get_lead_data_from_db(db_path):
        conn = sqlite3.connect(db_path)
        query = '''SELECT [Lead Number], [Lead Origin], [Lead Source], [Total Visits], [Average Time Per Visit] FROM 
        leads'''
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df

    @staticmethod
    def generate_leads():
        # Initialize the data generator and train models
        generator = neu.EffectiveLeadDataGenerator()
        generator.train_models()

        # Path to the SQLite database
        db_path = 'lead_data.db'

        # Get lead data from the database
        lead_data = ELSystem.get_lead_data_from_db(db_path)

        # Make predictions
        lead_score_predictions, engagement_score_predictions = generator.predict_leads(lead_data)

        # Create a DataFrame to hold the predictions and IDs
        predictions_df = lead_data.copy()
        predictions_df["Lead Score"] = lead_score_predictions
        predictions_df["Engagement Score"] = engagement_score_predictions

        # Suggest contact method based on engagement score
        predictions_df["Contact Method"] = predictions_df["Engagement Score"].apply(generator.suggest_contact_method)

        # Sort by Lead Score to get the best leads
        best_leads = predictions_df.sort_values(by="Lead Score", ascending=False).head(10)

        print(best_leads)

        # Save best leads to different tables within the same SQLite database based on contact method
        conn = sqlite3.connect(db_path)
        contact_methods = best_leads["Contact Method"].unique()

        for method in contact_methods:
            method_leads = best_leads[best_leads["Contact Method"] == method]

            # Extract additional columns for the selected leads
            lead_numbers = method_leads["Lead Number"].tolist()
            lead_numbers_str = ', '.join([f"'{num}'" for num in lead_numbers])

            query = f'''
                SELECT [Lead Number], [Name], [Phone Numbers], [Emails]
                FROM leads
                WHERE [Lead Number] IN ({lead_numbers_str})
            '''

            additional_info = pd.read_sql_query(query, conn)

            # Merge with the method_leads DataFrame
            method_leads = method_leads.merge(additional_info, on="Lead Number")

            table_name = f'best_leads_{method}'
            method_leads.to_sql(table_name, conn, if_exists='replace', index=False)

        conn.close()


if __name__ == "__main__":
    ELSystem.generate_leads()
