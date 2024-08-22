# Written by David Okoronkwo
import string

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split


class EffectiveLeadDataGenerator:
    def __init__(self, num_samples=1500):
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
        self.lead_scores = np.random.normal(0, 100, num_samples).astype(int)
        self.engagement_scores = np.random.normal(-50, 100, num_samples).astype(int)
        self.phone_numbers = np.random.randint(0000000000, 9999999999, num_samples)
        self.emails = [f"{''.join(np.random.choice(list(string.ascii_lowercase), size=8))}@example.com" for _ in
                       range(num_samples)]
        # self.lead_grades = np.random.choice(["A", "B", "C", "D"], num_samples, p=[0.1, 0.7, 0.15, 0.05])
        self.total_visits = np.random.poisson(3.45, num_samples)
        self.average_time_per_visit = np.random.normal(0, 600.50, num_samples).astype(int)

        # Ensure no negative values in Engagement Score and Average Time Per Visit
        self.engagement_scores = np.maximum(self.engagement_scores, 0)
        self.average_time_per_visit = np.maximum(self.average_time_per_visit, 0)

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
        return pd.DataFrame(data)

    def train_models(self, num_runs=25):
        df = self.to_dataframe()
        X = df[["Lead Number", "Lead Origin", "Lead Source", "Total Visits", "Average Time Per Visit"]]
        X = pd.get_dummies(X, columns=["Lead Origin", "Lead Source"], drop_first=True)
        y_lead_score = df["Lead Score"]
        y_engagement_score = df["Engagement Score"]

        best_lead_score_model = None
        best_engagement_score_model = None
        best_lead_score_mse = float('inf')
        best_engagement_score_mse = float('inf')

        for _ in range(num_runs):
            X_train, X_test, y_lead_score_train, y_lead_score_test, y_engagement_score_train, y_engagement_score_test = train_test_split(
                X, y_lead_score, y_engagement_score, test_size=0.2, random_state=None)  # Remove fixed random_state

            # Neural network for lead score prediction
            lead_score_regressor = MLPRegressor(hidden_layer_sizes=(50, 50), max_iter=1000, random_state=None)
            lead_score_regressor.fit(X_train, y_lead_score_train)
            y_lead_score_pred = lead_score_regressor.predict(X_test)
            lead_score_mse = mean_squared_error(y_lead_score_test, y_lead_score_pred)

            # Neural network for engagement score prediction
            engagement_score_regressor = MLPRegressor(hidden_layer_sizes=(50, 50), max_iter=1000, random_state=None)
            engagement_score_regressor.fit(X_train, y_engagement_score_train)
            y_engagement_score_pred = engagement_score_regressor.predict(X_test)
            engagement_score_mse = mean_squared_error(y_engagement_score_test, y_engagement_score_pred)

            # Update the best models
            if lead_score_mse < best_lead_score_mse:
                best_lead_score_mse = lead_score_mse
                best_lead_score_model = lead_score_regressor

            if engagement_score_mse < best_engagement_score_mse:
                best_engagement_score_mse = engagement_score_mse
                best_engagement_score_model = engagement_score_regressor

        self.lead_score_regressor = best_lead_score_model
        self.engagement_score_regressor = best_engagement_score_model

    def predict_leads(self, lead_data):
        # Check if 'Lead Origin' and 'Lead Source' are in the DataFrame
        if 'Lead Origin' not in lead_data.columns:
            lead_data['Lead Origin'] = 'Unknown'  # or any default value
        if 'Lead Source' not in lead_data.columns:
            lead_data['Lead Source'] = 'Unknown'  # or any default value

        # Convert categorical variables into dummy/indicator variables
        lead_data = pd.get_dummies(lead_data, columns=["Lead Origin", "Lead Source"], drop_first=True)

        # Continue with your prediction logic
        lead_score_predictions = self.lead_score_regressor.predict(lead_data)
        engagement_score_predictions = self.engagement_score_regressor.predict(lead_data)

        return lead_score_predictions, engagement_score_predictions

    def suggest_contact_method(self, engagement_score):
        if engagement_score > 50:
            return "call"
        elif engagement_score > 20:
            return "email"
        else:
            return "text"


'''

# Example usage
generator = EffectiveLeadDataGenerator()
generator.train_models()

# Example lead data for prediction
example_lead_data = generator.to_dataframe()[
    ["Lead Number", "Lead Origin", "Lead Source", "Total Visits", "Average Time Per Visit"]]
lead_score_predictions, engagement_score_predictions = generator.predict_leads(example_lead_data)

# Create a DataFrame to hold the predictions and IDs
predictions_df = generator.to_dataframe()[["Prospect ID", "Lead Number"]]
predictions_df["Lead Score"] = lead_score_predictions
predictions_df["Engagement Score"] = engagement_score_predictions

# Suggest contact method based on engagement score
predictions_df["Contact Method"] = predictions_df["Engagement Score"].apply(generator.suggest_contact_method)

# Sort by Lead Score to get the best leads
best_leads = predictions_df.sort_values(by="Lead Score", ascending=False).head(10)

print(best_leads)
'''
