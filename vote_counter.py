import csv

def count_votes(file_path):

    results = {}

    # Leer el archivo y procesar las filas
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # Saltar el encabezado si existe

        for row in reader:
            try:
                city, candidate, votes = row[0], row[1], int(row[2])
            except (IndexError, ValueError):  # Manejo de errores: fila incompleta o votos inválidos
                continue  # Ignorar filas con datos erróneos

            results[candidate] = results.get(candidate, 0) + votes  # Acumular votos por candidato

    # Ordenar los resultados por cantidad de votos
    sorted_results = sorted(results.items(), key=lambda item: item[1], reverse=True)

    if not sorted_results:
        print("No valid votes found.")
        return

    # Mostrar resultados
    for candidate, total_votes in sorted_results:
        print(f"{candidate}: {total_votes} votes")

    # Determinar si hay empate
    if len(sorted_results) > 1 and sorted_results[0][1] == sorted_results[1][1]:
        print("There is a tie.")
    else:
        print(f"Winner is {sorted_results[0][0]}")

# Ejemplo de uso
count_votes('votes.csv')
