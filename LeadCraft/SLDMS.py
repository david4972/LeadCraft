import sqlite3
import os


class DeleteDatabase:

    @staticmethod
    def delete_database():
        db_name = 'lead_data.db'
        if os.path.exists(db_name):
            os.remove(db_name)


class FullLeadListAccess:
    # Connect to the SQLite database
    conn = sqlite3.connect('lead_data.db')
    cursor = conn.cursor()

    # Functions for Lead list data
    @staticmethod
    # Define a function to print entire lead list
    def Full_Lead_List():
        FullLeadListAccess.cursor.execute(f"SELECT * FROM leads")
        rows = FullLeadListAccess.cursor.fetchall()

        try:

            if len(rows) == 0:
                print(f"No data found for the lead list.")
            else:
                print(f"Data in the lead list:")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"No Data Available: {e}")


    @staticmethod
    # Define a function to print all Prospect IDs and Lead Numbers in the database
    def Prospect_LeadNumbers_data():
        FullLeadListAccess.cursor.execute(f"SELECT Prospect ID, Lead Number, Name FROM Origination_Loans")
        rows = FullLeadListAccess.cursor.fetchall()

        try:

            if len(rows) == 0:
                print(f"No data found in the Lead List.")
            else:
                print(f"IDs for full Lead List:")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"No Data Available: {e}")


    @staticmethod
    # Define a function to print the sources of leads in the Lead List
    def source_Lead_List():
        FullLeadListAccess.cursor.execute(f"SELECT Prospect ID, Lead Number, Name, Lead Origin, Lead Source FROM leads")
        rows = FullLeadListAccess.cursor.fetchall()

        try:

            if len(rows) == 0:
                print(f"No data found in the Lead List.")
            else:
                print(f"Sources for the Lead List:")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"No Data Available: {e}")


    @staticmethod
    # Define a function to print lead and engagement scores from Lead List
    def Lead_Engagement_data():
        FullLeadListAccess.cursor.execute(
            f"SELECT Prospect ID, Lead Number, Name, Lead Score, Engagement Score FROM leads")
        rows = FullLeadListAccess.cursor.fetchall()

        try:

            if len(rows) == 0:
                print(f"No data found in the Lead List.")
            else:
                print(f"Lead and Engagement Scores in the Lead List:")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"No Data Available: {e}")


    @staticmethod
    # Define a function to print Per Visits from Lead List
    def Per_Visits_data():
        FullLeadListAccess.cursor.execute(
            f"SELECT Prospect ID, Lead Number, Name, Total Visits, Average Time Per Visit FROM leads")
        rows = FullLeadListAccess.cursor.fetchall()

        try:

            if len(rows) == 0:
                print(f"No data found in the Lead List.")
            else:
                print(f"Per Visits Data in the Lead List:")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"No Data Available: {e}")


    @staticmethod
    def delete_data():
        # Create a DELETE statement to remove all rows from the table
        delete_query = "DELETE FROM leads"

        try:

            # Execute the DELETE query
            FullLeadListAccess.cursor.execute(delete_query)
            FullLeadListAccess.conn.commit()
            print(f'All Lead data have been deleted.')
        except sqlite3.Error as e:
            print(f"Error deleting rows: {e}")
        finally:
            FullLeadListAccess.conn.close()


class CallListData:
    # Connect to the SQLite database
    conn = sqlite3.connect('lead_data.db')
    cursor = conn.cursor()

    # Functions for Lead list data
    @staticmethod
    # Define a function to print entire lead list
    def Full_Lead_List():
        FullLeadListAccess.cursor.execute(f"SELECT * FROM best_leads_call")
        rows = FullLeadListAccess.cursor.fetchall()

        try:

            if len(rows) == 0:
                print(f"No data found for the lead list.")
            else:
                print(f"Data in the lead list:")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"No Data Available: {e}")


    @staticmethod
    # Define a function to print all Prospect IDs and Lead Numbers in the database
    def Prospect_LeadNumbers_data():
        FullLeadListAccess.cursor.execute(f"SELECT Prospect ID, Lead Number, Name FROM best_leads_call")
        rows = FullLeadListAccess.cursor.fetchall()

        try:

            if len(rows) == 0:
                print(f"No data found in the Lead List.")
            else:
                print(f"IDs for full Lead List:")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"No Data Available: {e}")


    @staticmethod
    # Define a function to print the sources of leads in the Lead List
    def source_Lead_List():
        FullLeadListAccess.cursor.execute(
            f"SELECT Prospect ID, Lead Number, Name, Lead Origin, Lead Source FROM best_leads_call")
        rows = FullLeadListAccess.cursor.fetchall()

        try:

            if len(rows) == 0:
                print(f"No data found in the Lead List.")
            else:
                print(f"Sources for the Lead List:")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"No Data Available: {e}")


    @staticmethod
    # Define a function to print lead and engagement scores from Lead List
    def Lead_Engagement_data():
        FullLeadListAccess.cursor.execute(
            f"SELECT Prospect ID, Lead Number, Name, Lead Score, Engagement Score FROM best_leads_call")
        rows = FullLeadListAccess.cursor.fetchall()

        try:

            if len(rows) == 0:
                print(f"No data found in the Lead List.")
            else:
                print(f"Lead and Engagement Scores in the Lead List:")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"No Data Available: {e}")


    @staticmethod
    # Define a function to print Per Visits from Lead List
    def Per_Visits_data():
        FullLeadListAccess.cursor.execute(
            f"SELECT Prospect ID, Lead Number, Name, Total Visits, Average Time Per Visit FROM best_leads_call")
        rows = FullLeadListAccess.cursor.fetchall()

        try:
            if len(rows) == 0:
                print(f"No data found in the Lead List.")
            else:
                print(f"Per Visits Data in the Lead List:")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"No Data Available: {e}")


    @staticmethod
    def delete_data():
        # Create a DELETE statement to remove all rows from the table
        delete_query = "DELETE FROM best_leads_call"

        try:

            # Execute the DELETE query
            FullLeadListAccess.cursor.execute(delete_query)
            FullLeadListAccess.conn.commit()
            print(f'All Lead data have been deleted.')
        except sqlite3.Error as e:
            print(f"Error deleting rows: {e}")
        finally:
            FullLeadListAccess.conn.close()


class EmailListData:
    # Connect to the SQLite database
    conn = sqlite3.connect('lead_data.db')
    cursor = conn.cursor()

    # Functions for Lead list data
    @staticmethod
    # Define a function to print entire lead list
    def Full_Lead_List():
        FullLeadListAccess.cursor.execute(f"SELECT * FROM best_leads_email")
        rows = FullLeadListAccess.cursor.fetchall()

        try:

            if len(rows) == 0:
                print(f"No data found for the lead list.")
            else:
                print(f"Data in the lead list:")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"No Data Available: {e}")


    @staticmethod
    # Define a function to print all Prospect IDs and Lead Numbers in the database
    def Prospect_LeadNumbers_data():
        FullLeadListAccess.cursor.execute(f"SELECT Prospect ID, Lead Number, Name FROM best_leads_email")
        rows = FullLeadListAccess.cursor.fetchall()

        try:

            if len(rows) == 0:
                print(f"No data found in the Lead List.")
            else:
                print(f"IDs for full Lead List:")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"No Data Available: {e}")


    @staticmethod
    # Define a function to print the sources of leads in the Lead List
    def source_Lead_List():
        FullLeadListAccess.cursor.execute(
            f"SELECT Prospect ID, Lead Number, Name, Lead Origin, Lead Source FROM best_leads_email")
        rows = FullLeadListAccess.cursor.fetchall()

        try:

            if len(rows) == 0:
                print(f"No data found in the Lead List.")
            else:
                print(f"Sources for the Lead List:")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"No Data Available: {e}")


    @staticmethod
    # Define a function to print lead and engagement scores from Lead List
    def Lead_Engagement_data():
        FullLeadListAccess.cursor.execute(
            f"SELECT Prospect ID, Lead Number, Name, Lead Score, Engagement Score FROM best_leads_email")
        rows = FullLeadListAccess.cursor.fetchall()

        try:

            if len(rows) == 0:
                print(f"No data found in the Lead List.")
            else:
                print(f"Lead and Engagement Scores in the Lead List:")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"No Data Available: {e}")


    @staticmethod
    # Define a function to print Per Visits from Lead List
    def Per_Visits_data():
        FullLeadListAccess.cursor.execute(
            f"SELECT Prospect ID, Lead Number, Name, Total Visits, Average Time Per Visit FROM best_leads_email")
        rows = FullLeadListAccess.cursor.fetchall()
        try:

            if len(rows) == 0:
                print(f"No data found in the Lead List.")
            else:
                print(f"Per Visits Data in the Lead List:")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"No Data Available: {e}")


    @staticmethod
    def delete_data():
        # Create a DELETE statement to remove all rows from the table
        delete_query = "DELETE FROM best_leads_email"

        try:

            # Execute the DELETE query
            FullLeadListAccess.cursor.execute(delete_query)
            FullLeadListAccess.conn.commit()
            print(f'All Lead data have been deleted.')
        except sqlite3.Error as e:
            print(f"Error deleting rows: {e}")
        finally:
            FullLeadListAccess.conn.close()


class TextListData:
    # Connect to the SQLite database
    conn = sqlite3.connect('lead_data.db')
    cursor = conn.cursor()

    # Functions for Lead list data
    @staticmethod
    # Define a function to print entire lead list
    def Full_Lead_List():
        FullLeadListAccess.cursor.execute(f"SELECT * FROM best_leads_text")
        rows = FullLeadListAccess.cursor.fetchall()

        try:

            if len(rows) == 0:
                print(f"No data found for the lead list.")
            else:
                print(f"Data in the lead list:")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"No Data Available: {e}")


    @staticmethod
    # Define a function to print all Prospect IDs and Lead Numbers in the database
    def Prospect_LeadNumbers_data():
        FullLeadListAccess.cursor.execute(f"SELECT Prospect ID, Lead Number, Name FROM best_leads_text")
        rows = FullLeadListAccess.cursor.fetchall()

        try:

            if len(rows) == 0:
                print(f"No data found in the Lead List.")
            else:
                print(f"IDs for full Lead List:")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"No Data Available: {e}")


    @staticmethod
    # Define a function to print the sources of leads in the Lead List
    def source_Lead_List():
        FullLeadListAccess.cursor.execute(
            f"SELECT Prospect ID, Lead Number, Name, Lead Origin, Lead Source FROM best_leads_text")
        rows = FullLeadListAccess.cursor.fetchall()

        try:

            if len(rows) == 0:
                print(f"No data found in the Lead List.")
            else:
                print(f"Sources for the Lead List:")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"No Data Available: {e}")


    @staticmethod
    # Define a function to print lead and engagement scores from Lead List
    def Lead_Engagement_data():
        FullLeadListAccess.cursor.execute(
            f"SELECT Prospect ID, Lead Number, Name,  Lead Score, Engagement Score FROM best_leads_text")
        rows = FullLeadListAccess.cursor.fetchall()

        try:

            if len(rows) == 0:
                print(f"No data found in the Lead List.")
            else:
                print(f"Lead and Engagement Scores in the Lead List:")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"No Data Available: {e}")


    @staticmethod
    # Define a function to print Per Visits from Lead List
    def Per_Visits_data():
        FullLeadListAccess.cursor.execute(
            f"SELECT Prospect ID, Lead Number, Name, Total Visits, Average Time Per Visit FROM best_leads_text")
        rows = FullLeadListAccess.cursor.fetchall()
        try:

            if len(rows) == 0:
                print(f"No data found in the Lead List.")
            else:
                print(f"Per Visits Data in the Lead List:")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"No Data Available: {e}")


    @staticmethod
    def delete_data():
        # Create a DELETE statement to remove all rows from the table
        delete_query = "DELETE FROM best_leads_text"

        try:

            # Execute the DELETE query
            FullLeadListAccess.cursor.execute(delete_query)
            FullLeadListAccess.conn.commit()
            print(f'All Lead data have been deleted.')
        except sqlite3.Error as e:
            print(f"Error deleting rows: {e}")
        finally:
            FullLeadListAccess.conn.close()
