# Calcul de Distance Point-Ellipse

Ce projet implémente une solution pour calculer la distance signée entre un point et une ellipse en utilisant la méthode de Newton-Raphson pour résoudre l'équation polynomiale d'ordre 4.

## Description

La distance d'un point à une ellipse est un problème mathématique qui n'a pas de solution analytique simple. Ce code résout ce problème en:

1. Formulant une équation polynomiale d'ordre 4
2. Utilisant la méthode de Newton-Raphson pour trouver les racines de l'équation
3. Calculant la distance signée finale à partir des racines trouvées
4. Visualisant l'ellipse, le point d'origine et le point de projection sur l'ellipse

## Fonctionnalités

- Calcul précis de la distance signée d'un point à une ellipse
- Détection de toutes les racines potentielles d'une équation polynomiale d'ordre 4
- Visualisation graphique de l'ellipse et des points pertinents
- Vérification de la précision des résultats

## Comment utiliser

1. Définissez les paramètres de l'ellipse (demi-axes `a` et `b`)
2. Spécifiez les coordonnées du point pour lequel calculer la distance (`x_0` et `y_0`)
3. Exécutez le script principal pour:
   - Visualiser la fonction polynomiale et ses racines
   - Calculer la distance signée
   - Afficher une représentation graphique de l'ellipse et des points

## Exemples de résultats

Le code génère deux figures:
- `polynome.png`: Visualisation de la fonction polynomiale avec ses racines
- `solution.png`: Représentation graphique de l'ellipse, du point de référence et du point projeté

### Détails techniques
### Fonctions principales

- `newton_raphson()`: Implémente l'algorithme de Newton-Raphson pour trouver les racines
- `trouver_toutes_racines()`: Recherche toutes les racines de l'équation polynomiale
- `distance_signee()`: Calcule la distance signée à partir de la valeur λ trouvée
- `tracer_ellipse_et_points()`: Crée une visualisation de l'ellipse et des points

## Exécution

```bash
python exercice_3.py
```
