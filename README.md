## Transpile simple model 

Dans ce TP notre objectif est de déployer des modèles déjà entraîné sur des cibles de type micro-controlleur.

## On peut envisager deux approches : 

Faire une librairie qui sera chargée de charger les caractéristiques du modèle et faire en sorte en suite de faire la prédiction. 
Faire en sorte d'avoir un fichier C prêt à l'emploi qui contiendra toutes les informations.

## Composition du dossier :
Une partie concernant Verilog puis ensuite dans la partie transpile :

## Regression lineaire
Le dataset de ce modèle est tiré du fichier '[houses.csv](./houses.csv)'

Le programme est '[linear_regression.py](./linear_regression.py)'

Le programme permet de charger un modele de regression linèaire entrainé '[linear_regression.joblib](./linear_regression.joblib)'
Il récupère ensuite  les valeurs de coefficients , génère une chaîne de caractère contenant le code C, permettant de calculer la prédiction du modèle (float prediction(float *features, int n_feature) )avec les valeur du coefficient.

Ensuite , il génère une fonction main  [main.c](./main.c)'qui permet d'appeler prediction sur une donnée définié par un tableau statique de votre choix puis sauvegarde le code c généré dans [linear_regression.c](./linear_regression.c)'.

Le fichier [makefile](./makefile)'affiche la commande de compilation à lancer pour le compiler telle que :
```sh
make
```


## Regression logistique 
Le dataset de ce modèle est tiré du fichier '[prediction_maintenance.csv](./prediction_maintenance.csv)'

Le programme est '[logisitic_regression.py](./linear_regression.py)'

Le programme permet de charger un modele de regression linèaire entrainé '[linear_regression.joblib](./linear_regression.joblib)'
Il récupère ensuite  les valeurs de coefficients , génère une chaîne de caractère contenant le code C, permettant de calculer la prédiction du modèle (float prediction(float *features, int n_feature) )avec les valeur du coefficient.

Ensuite , il génère une fonction main  [main.c](./main.c)'qui permet d'appeler prediction sur une donnée définié par un tableau statique de votre choix puis sauvegarde le code c généré dans [logistic_regression.c](./linear_regression.c)'.

Le fichier [makefile](./makefile)'affiche la commande de compilation à lancer pour le compiler telle que :
```sh
make
```
## Decision Tree

Le modèle est entrainé

## Choice Function

Un programme python écrit '[choice_function.py](./choice_fucnction.py)' il permet une ligne de commande du type :
```sh
python choice_function.py -f %filepath_csv_model% -m %model%
```
Ainsi il suffit d'entrer le chemin de fichier csv puis le modele de prediction que vous souhaitez dans la ligne de commande .
