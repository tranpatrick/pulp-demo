from pulp import LpProblem, LpMaximize, LpVariable, LpInteger, PULP_CBC_CMD, LpConstraint, LpConstraintLE, LpAffineExpression

if __name__ == '__main__':
    # Paramètres
    n_caoutchouc = 400
    n_acier = 600
    prix_petite_voiture = 10000
    prix_grosse_voiture = 16000

    # Définition des variables
    x = LpVariable('x', lowBound=0, cat=LpInteger)
    y = LpVariable('y', lowBound=0, cat=LpInteger)

    # Problème
    probleme = LpProblem(name='chiffre_affaires', sense=LpMaximize)

    # Contraintes
    contrainte_caoutchouc = LpConstraint(e=x + y, sense=LpConstraintLE, name='contrainte_caouthouc', rhs=n_caoutchouc)
    probleme.add(contrainte_caoutchouc)
    contrainte_acier = LpConstraint(e=2 * x + y, sense=LpConstraintLE, name='contrainte_acier', rhs=n_acier)
    probleme.add(contrainte_acier)

    # Fonction objectif
    fonction_objectif = LpAffineExpression(e=prix_grosse_voiture*x + prix_petite_voiture*y)
    probleme.setObjective(fonction_objectif)

    # Résolution
    solver = PULP_CBC_CMD(timeLimit=20, msg=True)
    probleme.solve(solver=solver)

    # Résultat
    print(f'x = {x.value()}')
    print(f'y = {y.value()}')