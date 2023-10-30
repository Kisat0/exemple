def est_bissectile(annee):
    if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
        return True
    else:
        return False

# Testons avec quelques années
annee1 = 2000
annee2 = 2020
annee3 = 2023

print(f"{annee1} est bissextile : {est_bissectile(annee1)}")
print(f"{annee2} est bissextile : {est_bissectile(annee2)}")
print(f"{annee3} est bissextile : {est_bissectile(annee3)}")
