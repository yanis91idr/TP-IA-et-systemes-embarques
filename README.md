## Transpile simple model 

Dans ce TP notre objectif est de déployer des modèles déjà entraîné sur des cibles de type micro-controlleur.

## On peut envisager deux approches : 

Faire une librairie qui sera chargée de charger les caractéristiques du modèle et faire en sorte en suite de faire la prédiction. 
Faire en sorte d'avoir un fichier C prêt à l'emploi qui contiendra toutes les informations.

## Composition du dossier :

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
Après compilation , on peut s'apercevoir que la prédiction du modèle model.X  :

Un résulat de prédiction assez cohérent étant donné que la caractéristique de l'orientation de la maison n'a pas été prise en compte.


## Regression logistique 
