import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

def build_model():

    df = pd.read_csv('predictive_maintenance.csv')

    x = df.drop(columns='last_revision')
    y = df['last_revision']

    model = DecisionTreeClassifier(random_state=42, max_depth=20)

    model.fit(x, y)

    joblib.dump(model, "decision_tree.joblib")


build_model()
