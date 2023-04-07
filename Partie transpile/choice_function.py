
# TODO : Prendre en entrer un fichier de donné + choix du modèle de transpilation

import joblib
import csv
import argparse
import pandas as pd
from joblib import dump, load
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
import numpy as np

# Chemin vers le fichier joblib contenant le modèle entraîné
MODEL_FILE = 'regression.joblib'


def logistic_regression(filepath):
    def build_model():
        df = pd.read_csv(filepath)
        x = df[df.columns[0:-2]]
        y = np.asarray(df[df.columns[-1]], dtype="|S")
        print(y)
        model = LogisticRegression(solver='saga', multi_class='multinomial')
        model.fit(x, y)
        regression_model = joblib.dump(model, MODEL_FILE)
        return regression_model

    def logistic():
        build_model()

        # Charger le modèle à partir du fichier joblib
        model = joblib.load(MODEL_FILE)

        # Faire une prédiction à partir de caractéristiques données (ici, des caractéristiques aléatoires)
        features = [2.2, 3.19, 7.56]
        prediction_array = model.predict([features])

        # Afficher la prédiction
        print('Model.intercept :', model.intercept_)
        print('Model.coef :', model.coef_)

        # Générer le code C pour calculer la prédiction
        code_c = 'float prediction(float *features, int n_feature) {\n'
        code_c += '  float result = 0;\n'
        for i in range(len(model.coef_)):
            code_c += '  result += %f + %s * features[%d];\n' % (
            model.intercept_[i], "*".join(np.asarray(model.coef_[i], dtype=np.str_)), i)
        code_c += '  return result;\n'
        code_c += '}\n'

        # Afficher le code C généré
        print(code_c)

        # Écrire le code C dans un fichier
        with open('prediction.c', 'w') as f:
            f.write(code_c)

        # Appel de  la fonction "prediction" avec les  caractéristiques définies
        result = prediction_array

        # Affichage de la prédiction
        # print('Prédiction:', result)

        # Générer le code pour la fonction main
        code_main = """
        #include <stdio.h>

        int main() {
            float features[] = { %s };
            int n_feature = %i;
            float result = prediction(features, n_feature);
            printf("The predicted probability is: %%f\\n", result);
            return 0;
        }

            """ % (", ".join(str(x) for x in features), len(features))

        # Écrire le code de la fonction main dans un fichier
        with open('main.c', 'w') as f:
            f.write(code_main)
    logistic()

def linear_regression(filepath):
    def build_model():
        df = pd.read_csv(filepath)
        x = df[df.columns[0:-2]]
        y = df[df.columns[-1]]
        model = LinearRegression()
        model.fit(x, y)
        return joblib.dump(model, MODEL_FILE)

    def linear():
        build_model()

        # Charger le modèle à partir du fichier joblib
        model = joblib.load(MODEL_FILE)

        # Get coefficients
        coefficients = model.coef_
        # Faire une prédiction à partir de caractéristiques données (ici, des caractéristiques aléatoires)
        features = [206, 2, 0]
        prediction_array = model.predict([features])

        # Afficher la prédiction
        print('Prédiction :', prediction_array)

        # Générer le code C pour calculer la prédiction
        code_c = 'float prediction(float *features, int n_feature) {\n'
        code_c += '  float result = %f;\n' % model.intercept_
        for i in range(len(coefficients)):
            code_c += '  result += %f * features[%d];\n' % (coefficients[i], i)
        code_c += '  return result;\n'
        code_c += '}\n'

        # Afficher le code C généré
        print(code_c)

        # Écrire le code C dans un fichier
        with open('prediction.c', 'w') as f:
            f.write(code_c)

        # Appel de  la fonction "prediction" avec les  caractéristiques définies
        result = prediction_array

        # Affichage de la prédiction
        print('Prédiction:', result)

        # Générer le code pour la fonction main
        code_main = """
        #include <stdio.h>

        float prediction(float *features, int n_feature);

        int main() {
            float features[] = {%s};
            int n_feature = %d;
            float result = prediction(features, n_feature);
            printf("Prédiction : %%f\\n", result);
            return 0;
        }
            """ % (", ".join(str(x) for x in features), len(features))

        # Écrire le code de la fonction main dans un fichier
        with open('main.c', 'w') as f:
            f.write(code_main)
    linear()
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filepath', type=str, help='Path to the CSV file')
    parser.add_argument('-m', '--model', type=str, help='Enter the model of transpilation you want')
    args = parser.parse_args()
    if args.model == 'linear':
        linear_regression(args.filepath)
    if args.model == 'logistic':
        logistic_regression(args.filepath)


if __name__ == "__main__":
    main()
