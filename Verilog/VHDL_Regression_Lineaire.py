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

# Génération du module VHDL à partir du modèle entraîné
template = Template('''
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity regression_lineaire is
{% for feature in features %}  port({{ feature }}: in std_logic_vector(31 downto 0);
{% endfor %}  y_pred: out std_logic_vector(31 downto 0));
end entity regression_lineaire;

architecture behavioral of regression_lineaire is

begin

  y_pred <= std_logic_vector(to_signed({{ intercept }}, 32));
{% for feature, coef in zip(features, coefficients) %}
  y_pred <= std_logic_vector(unsigned(y_pred) + unsigned(std_logic_vector(to_signed({{ coef }}, 32)) * std_logic_vector(signed({{ feature }}))));
{% endfor %}

end architecture behavioral;
''')

module_code = template.render(
    features=X.columns,
    intercept=int(model.intercept_),
    coefficients=[int(coef) for coef in model.coef_]
)

# Enregistrement du module VHDL dans un fichier
with open('regression_lineaire.vhd', 'w') as f:
    f.write(module_code)

