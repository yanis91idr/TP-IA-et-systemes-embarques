import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

# Chemin vers le fichier joblib contenant le modèle entraîné
MODEL_FILE = 'linear_regression.joblib'


def build_model():
    df = pd.read_csv('houses.csv')
    print(df)
    x = df[['size', 'nb_rooms', 'garden']]
    y = df['price']
    model = LinearRegression()
    model.fit(x, y)
    regression_model = joblib.dump(model, MODEL_FILE)
    return regression_model


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
    with open('linear_regression.c', 'w') as f:
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


if __name__ == "__main__":
    linear()


