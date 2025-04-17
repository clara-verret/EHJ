import numpy as np
import matplotlib.pyplot as plt

def fonction_polynomiale(x, coefficients):
    """
    Évalue un polynôme d'ordre 4 à la valeur x
    coefficients = [a, b, c, d, e] pour ax**4 + bx**3 + cx**2 + dx + e
    """
    a, b, c, d, e = coefficients
    return a * x**4 + b * x**3 + c * x**2 + d * x + e

def derivee_polynomiale(x, coefficients):
    """
    Évalue la dérivée d'un polynôme d'ordre 4 à la valeur x
    coefficients = [a, b, c, d, e] pour ax**4 + bx**3 + cx**2 + dx + e
    La dérivée est 4ax**3 + 3bx**2 + 2cx + d
    """
    a, b, c, d, e = coefficients
    return 4 * a * x**3 + 3 * b * x**2 + 2 * c * x + d

def newton_raphson(coefficients, x0, epsilon=1e-10, max_iterations=100):
    """
    Implémente la méthode de Newton-Raphson pour trouver une racine
    d'un polynôme d'ordre 4
    
    Args:
        coefficients: Coefficients du polynôme [a, b, c, d, e]
        x0: Valeur initiale
        epsilon: Précision souhaitée
        max_iterations: Nombre maximum d'itérations
        
    Returns:
        racine: La racine trouvée
        iterations: Nombre d'itérations effectuées
        convergence: Liste des valeurs successives de x
    """
    x = x0
    convergence = [x]
    
    for i in range(max_iterations):
        f_x = fonction_polynomiale(x, coefficients)
        if abs(f_x) < epsilon:
            return x, i+1, convergence
        
        df_x = derivee_polynomiale(x, coefficients)
        if df_x == 0:
            return None, i+1, convergence  # Division par zéro, échec
        
        x_next = x - f_x / df_x
        convergence.append(x_next)
        
        if abs(x_next - x) < epsilon:
            return x_next, i+1, convergence
        
        x = x_next
    
    return x, max_iterations, convergence  # Max itérations atteintes

def trouver_toutes_racines(coefficients, valeurs_initiales):
    """
    Trouve toutes les racines d'un polynôme d'ordre 4 en utilisant
    différentes valeurs initiales
    
    Args:
        coefficients: Coefficients du polynôme [a, b, c, d, e]
        valeurs_initiales: Liste des valeurs de départ
        
    Returns:
        racines: Liste des racines trouvées
    """
    racines = []
    
    for x0 in valeurs_initiales:
        racine, iterations, _ = newton_raphson(coefficients, x0)
        if racine is not None:
            # Vérifier si cette racine n'est pas déjà trouvée
            est_nouvelle = True
            for r in racines:
                if abs(r[0] - racine) < 1e-8:
                    est_nouvelle = False
                    break
            
            if est_nouvelle:
                racines.append((racine, iterations))
    
    return racines

def distance_signee(lambda_, x_0,y_0,a,b):
    x = x_0/(1-lambda_/(a**2))
    y= y_0/(1-lambda_/(b**2))
    d = np.sqrt((x-x_0)**2+(y-y_0)**2)
    print(f"Distance signée: {np.sign((x_0/a)**2 + (y_0/b)**2 -1)*d:.10f}")
    return x,y,np.sign((x_0/a)**2 + (y_0/b)**2 -1)*d


######################################################## PLOTS #######################################################
def tracer_ellipse_et_points(a, b,points, O_1=0, O_2=0):
    """
    Trace une ellipse centrée en (x0, y0) avec demi-axes a et b
    ainsi que les points donnés sur la même figure.
    
    Args:
        a (float): Longueur du demi-grand axe de l'ellipse
        b (float): Longueur du demi-petit axe de l'ellipse
        x0 (float): Coordonnée x du centre de l'ellipse
        y0 (float): Coordonnée y du centre de l'ellipse
        points (list): Liste de tuples (x, y) représentant les points à tracer
    """
    # Créer la figure
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Paramétrage de l'ellipse
    theta = np.linspace(0, 2 * np.pi, 1000)
    x = O_1 + a * np.cos(theta)
    y = O_2 + b * np.sin(theta)
    
    # Tracer l'ellipse
    ax.plot(x, y, 'b-', label=f'Ellipse (a={a}, b={b})')
    
    # Tracer le centre de l'ellipse
    ax.plot(O_1, O_2, 'ro', markersize=8, label=f'Centre ({O_1}, {O_2})')
    
    # Tracer les points
    for i, (x, y) in enumerate(points):
        ax.plot(x, y, 'go', markersize=6)
        ax.annotate(f'P{i+1}({x:.2f}, {y:.2f})', (x, y), xytext=(5, 5), 
                    textcoords='offset points')
    
    # Déterminer les limites du graphique
    max_a_b = max(a, b)
    margin = max_a_b * 0.2  # Marge de 20%
    ax.set_xlim(O_1 - a - margin, O_1 + a + margin)
    ax.set_ylim(O_2 - b - margin, O_2 + b + margin)
    
    # Ajouter une grille et des axes égaux
    ax.grid(True)
    ax.set_aspect('equal')
    
    # Ajouter des titres et légendes
    ax.set_title(f"Ellipse centrée en ({O_1}, {O_2}) avec demi-axes a={a} et b={b}")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    
    # Afficher la figure
    plt.tight_layout()
    plt.savefig('./solution.png')


######################################################### MAIN #######################################################
if __name__ == "__main__":
    # Définir les paramètres de l'ellipse et le point M_0
    a=3
    b=2

    x_0=2
    y_0=1

    # Coefficients du polynôme d'ordre 4
    # f(x) = c_4*x^4 + c_3*x^3 + c_2*x^2 + c_1*x + c_0
    c_4=1
    c_3=-2*a**2-2*b**2
    c_2=-x_0**2*a**2-y_0**2*b**2+4*a**2*b**2+a**4+b**4
    c_1=-2*b**2*a**4-2*a**2*b**4+2*x_0**2*a**2*b**2+2*y_0**2*b**2*a**2
    c_0=-x_0**2*a**2*b**4-y_0**2*b**2*a**4+a**4*b**4

    coeffs = [c_4, c_3, c_2, c_1, c_0]
    
    # Visualiser la fonction pour déterminer des valeurs initiales pertinentes
    x = np.linspace(-8, 8, 1000)
    y = [fonction_polynomiale(val, coeffs) for val in x]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.axhline(y=0, color='r', linestyle='-', alpha=0.3)
    plt.grid(True)
    plt.title("Visualisation de la fonction polynomiale")
    plt.xlabel("x")
    plt.ylabel("f(x)")
        
    # Essayer plusieurs valeurs initiales pour trouver toutes les racines
    valeurs_initiales = [0.5*(x_0**2+y_0**2-a**2-b**2), 2,3,4,5]
    racines = trouver_toutes_racines(coeffs, valeurs_initiales)
    
    print("Racines trouvées:")
    for racine, iterations in racines:
        print(f"x = {racine:.10f} (convergence en {iterations} itérations)")
        print(f"f(x) = {fonction_polynomiale(racine, coeffs):.15f}")
        plt.plot(racine, 0, 'go', markersize=8)
    plt.savefig('./polynome.png')
    
    x,y,d= distance_signee(racines[0][0], x_0, y_0, a, b)
    tracer_ellipse_et_points(a, b,points=[(x_0, y_0), (x, y)])
