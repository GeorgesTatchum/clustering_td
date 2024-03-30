def find_missing_letters(table1, table2):
  """
  Détermine les lettres du premier tableau qui ne sont pas dans le second.

  Args:
      table1: Le premier tableau.
      table2: Le deuxième tableau.

  Returns:
      Un ensemble contenant les lettres manquantes.
  """

  set1 = set(table1)
  set2 = set(table2)
  return set1.difference(set2)

# Exemple d'utilisation
table1 = ["a", "b", "c", "d"]
table2 = ["b", "c", "e", "f"]

missing_letters = find_missing_letters(table2, table1)
print(f"Lettres manquantes : {len(missing_letters)}")