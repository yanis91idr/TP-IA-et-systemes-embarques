
import joblib
import csv
import argparse
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
import numpy as np

# Chemin vers le fichier joblib contenant le modele entraine
MODEL_FILE = 'logistic_regression.joblib'


def logistic_regression():
	def build_model():
		df = pd.read_csv("predictive_maintenance.csv")
		x = df[['vibration', 'avg_speed', 'age', 'last_revision']]
		y = df['broke']
		model = LogisticRegression()
		model.fit(x, y)
		joblib.dump(model, MODEL_FILE)

	def logistic():
		build_model()

		# Charger le modele a partir du fichier joblib
		model = joblib.load(MODEL_FILE)

		# Faire une prediction a partir de caracteristiques donnees (ici, des caracteristiques aleatoires)
		features = [2.2, 3.19, 7.56, 8.42]
		prediction_array = model.predict([features])

		# Afficher la prediction
		print('Model.intercept :', model.intercept_)
		print('Model.coef :', model.coef_)

		# Generer le code C pour calculer la prediction
		code_c = 'float prediction(float *features, int n_feature) {\n'
		code_c += '  float result = 0;\n'
		for i in range(len(model.coef_)):
			code_c += '  result += %f + %f * features[%d];\n' % (
				model.intercept_[i],
				model.coef_[0][i],
				i
			)
		code_c += '  return result;\n'
		code_c += '}\n'


		# Ecrire le code C dans un fichier
		with open('logistic_regression.c', 'w') as f:
			f.write(code_c)

		# Appel de  la fonction "prediction" avec les  caracteristiques definies
		result = prediction_array

		# Generer le code pour la fonction main
		code_main = """
		#include <stdio.h>

		float exp_approx(float x, int n_term) {
			float result = 1.0;
			float term = 1.0;

			for (int i = 1; i <= n_term; i++) {
				term *= x / i;
				result += term;
			}
			
			return result;
		}
		float sigmoid(float x) {
			return 1.0/(exp_approx(-x,10) + 1.0);
		}

		int main() {
			float features[] = { %s };
			int n_feature = %i;
			float result = prediction(features, n_feature);
			printf("The predicted probability is: %%f\\n", result);
			return 0;
		}

			""" % (", ".join(str(x) for x in features), len(features))

		# Ecrire le code de la fonction main dans un fichier
		with open('main.c', 'w') as f:
			f.write(code_main)
	logistic()

logistic_regression()