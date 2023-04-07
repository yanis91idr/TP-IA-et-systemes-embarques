import pandas as pd
from sklearn.linear_model import LinearRegression
from jinja2 import Template

# Chargement des données CSV
data = pd.read_csv('donnees.csv')

# Séparation des variables d'entrée (X) et de la variable cible (y)
X = data.drop(columns=['y'])
y = data['y']

# Entraînement du modèle de régression linéaire
model = LinearRegression()
model.fit(X, y)

# Génération du module Verilog à partir du modèle entraîné
template = Template('''
module regression_lineaire(
{% for feature in features %}  input signed [31:0] {{ feature }},
{% endfor %}  output signed [31:0] y_pred
);

  assign y_pred = {{ intercept }};
{% for feature, coef in zip(features, coefficients) %}
  assign y_pred = y_pred + {{ coef }} * {{ feature }};
{% endfor %}

endmodule
''')

module_code = template.render(
    features=X.columns,
    intercept=int(model.intercept_),
    coefficients=[int(coef) for coef in model.coef_]
)

# Enregistrement du module Verilog dans un fichier
with open('regression_lineaire.v', 'w') as f:
    f.write(module_code)
