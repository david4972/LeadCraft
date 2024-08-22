# Sales Software for Lead Generation
# Written by David Okoronkwo
import effective_lead_system
import SLDMS


class MBASalesSystem:
    def __init__(self, Virtual_Marketer):
        self.Virtual_Marketer = Virtual_Marketer

    def intro(self):
        print("This is a Sales Software prototype for a Lead Generation & Marketing platform")
        print("Welcome to the MBA Course Sales System, My name is " + self + "\n"
                                                                             "I will be assisting in helping you with "
                                                                             "your in house CRM system, My goal is to "
                                                                             "\n"
                                                                             "increase your quality of potential "
                                                                             "customers in turn increasing your "
                                                                             "conversion rate \n"
                                                                             "as well as rentention. Choose what "
                                                                             "you'd Like to view today")
        print("Contents: View Entire Lead Data - Access to entire Data of all leads acquired")
        print("Contents: Effective Lead Gen System - Runs ML program to create a list of the best leads based on "
              "Entire Lead Data")
        print("Contents: View Analyzed Lead Data -  Access Effective Lead Gen System analyzed data on leads with "
              "call, text and email as best point of contact")

        print("1) View Entire Lead Data")  # Access to entire Data of all leads acquired
        print("2) Effective Lead Gen System")  # Runs ML program to create a list of the best leads based on Entire
        # Lead Data
        # print("3) Email Template/Automation")  # draft and send to leads with email as best point of contact
        # print("4) Call Template")  # draft and send to leads with Call as best point of contact
        # print("5) Text Template/Automation")  # draft and send to leads with Text as best point of contact
        print("3) View Analyzed Lead Data")  # Access data on leads with call, text and email as best point of contact
        print("4) Exit Program")
        select = input()

        if select == "1":
            MBASalesSystem.Rawlead_data_system(self)
        if select == "2":
            MBASalesSystem.eff_lead_system(self)
        if select == "3":
            MBASalesSystem.leads_data_system(self)
        if select == "4":
            exit(0)
        '''
        if select == "3":
            # email_marketing_system()
        if select == "4":
            # PhoneText_marketing_system()
        '''

    def Rawlead_data_system(self):
        print(self + ": What Data are you looking to access right now?")
        print("1) IDs & Lead Numbers")
        print("2) Lead Sources")
        print("3) Engagement metrics")
        print("4) Page Visit Metrics")
        print("5) All Data")
        print("6) Delete Data")
        select = input()
        if select == "1":
            SLDMS.FullLeadListAccess.Prospect_LeadNumbers_data()
            MBASalesSystem.intro(self)
        if select == "2":
            SLDMS.FullLeadListAccess.source_Lead_List()
            MBASalesSystem.intro(self)
        if select == "3":
            SLDMS.FullLeadListAccess.Lead_Engagement_data()
            MBASalesSystem.intro(self)
        if select == "4":
            SLDMS.FullLeadListAccess.Per_Visits_data()
            MBASalesSystem.intro(self)
        if select == "5":
            SLDMS.FullLeadListAccess.Full_Lead_List()
            MBASalesSystem.intro(self)
        if select == "6":
            SLDMS.FullLeadListAccess.delete_data()
            MBASalesSystem.intro(self)

    def eff_lead_system(self):
        print(self + ": Evaluating Lead Data.......")
        effective_lead_system.ELSystem.generate_leads()
        print(self + ": Evaluation Complete, Here are your best leads and how to best contact them.")
        MBASalesSystem.intro(self)

    def leads_data_system(self):
        print(self + ": What are you looking to access right now?")
        print("1) Best Leads to Call")
        print("2) Best Leads to Email")
        print("3) Best Leads to Text")
        select = input()
        if select == "1":
            print(self + ": What Data are you looking to access right now?")
            print("1) IDs & Lead Numbers")
            print("2) Lead Sources")
            print("3) Engagement metrics")
            print("4) Page Visit Metrics")
            print("5) All Data")
            print("6) Delete Data")
            select1 = input()
            if select1 == "1":
                SLDMS.CallListData.Prospect_LeadNumbers_data()
                MBASalesSystem.intro(self)
            if select1 == "2":
                SLDMS.CallListData.source_Lead_List()
                MBASalesSystem.intro(self)
            if select1 == "3":
                SLDMS.CallListData.Lead_Engagement_data()
                MBASalesSystem.intro(self)
            if select1 == "4":
                SLDMS.CallListData.Per_Visits_data()
                MBASalesSystem.intro(self)
            if select1 == "5":
                SLDMS.CallListData.Full_Lead_List()
                MBASalesSystem.intro(self)
            if select1 == "6":
                SLDMS.CallListData.delete_data()
                MBASalesSystem.intro(self)

        if select == "2":
            print(self + ": What Data are you looking to access right now?")
            print("1) IDs & Lead Numbers")
            print("2) Lead Sources")
            print("3) Engagement metrics")
            print("4) Page Visit Metrics")
            print("5) All Data")
            print("6) Delete Data")
            select2 = input()
            if select2 == "1":
                SLDMS.EmailListData.Prospect_LeadNumbers_data()
                MBASalesSystem.intro(self)
            if select2 == "2":
                SLDMS.EmailListData.source_Lead_List()
                MBASalesSystem.intro(self)
            if select2 == "3":
                SLDMS.EmailListData.Lead_Engagement_data()
                MBASalesSystem.intro(self)
            if select2 == "4":
                SLDMS.EmailListData.Per_Visits_data()
                MBASalesSystem.intro(self)
            if select2 == "5":
                SLDMS.EmailListData.Full_Lead_List()
                MBASalesSystem.intro(self)
            if select2 == "6":
                SLDMS.EmailListData.delete_data()
                MBASalesSystem.intro(self)
        if select == "3":
            print(self + ": What Data are you looking to access right now?")
            print("1) IDs & Lead Numbers")
            print("2) Lead Sources")
            print("3) Engagement metrics")
            print("4) Page Visit Metrics")
            print("5) All Data")
            print("6) Delete Data")
            select3 = input()
            if select3 == "1":
                SLDMS.TextListData.Prospect_LeadNumbers_data()
                MBASalesSystem.intro(self)
            if select3 == "2":
                SLDMS.TextListData.source_Lead_List()
                MBASalesSystem.intro(self)
            if select3 == "3":
                SLDMS.TextListData.Lead_Engagement_data()
                MBASalesSystem.intro(self)
            if select3 == "4":
                SLDMS.TextListData.Per_Visits_data()
                MBASalesSystem.intro(self)
            if select3 == "5":
                SLDMS.TextListData.Full_Lead_List()
                MBASalesSystem.intro(self)
            if select3 == "6":
                SLDMS.TextListData.delete_data()
                MBASalesSystem.intro(self)


if __name__ == "__main__":
    MBASalesSystem.intro(self="LAM")
