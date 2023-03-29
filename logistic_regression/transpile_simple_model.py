import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Chemin vers le fichier joblib contenant le modèle entraîné
MODEL_FILE = 'regression.joblib'


def build_model():
    df = pd.read_csv('houses.csv')
    x = df[['size', 'nb_rooms', 'garden']]
    y = df['price']
    model = LogisticRegression()
    model.fit(x, y)
    regression_model = joblib.dump(model, MODEL_FILE)
    return regression_model


def main():
    build_model()

    # Charger le modèle à partir du fichier joblib
    model = joblib.load(MODEL_FILE)

    # recupère les coefficients
    coefficients = model.coef_
    # Faire une prédiction à partir de caractéristiques données (ici, des caractéristiques aléatoires)
    features = [2.2, 3.19, 6.56]
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
   
   // on réutilise les fonctions c codées sur nowledgeable
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
    float denominator = exp_approx(-x, 10) + 1.0;
    return 1.0 / denominator;
    }
    
    float logistic_regression(float* features, float* thetas, int n_parameter) {
    float z = 0.0;
    for (int i = 0; i < n_parameter; i++) {
        z += features[i] * thetas[i];
    }
    return sigmoid(z);
    }
    int main() {
        float features[] = {1.2, 2.3, 3.4, 4.5};
        int n_feature = 4;
        float weights[] = {0.1, 0.2, 0.3, 0.4};
        float result = logistic_regression(features, n_feature, weights);
        printf("The predicted probability is: %.2f\n", result);
        return 0;
    }

        """ % (", ".join(str(x) for x in features), len(features))

    # Écrire le code de la fonction main dans un fichier
    with open('main.c', 'w') as f:
        f.write(code_main)


if __name__ == "__main__":
    main()


