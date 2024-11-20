import csv

with open("produtos.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Produto", "Preço"])  
    writer.writerow([1, "Produto A", 10.50])
    writer.writerow([2, "Produto B", 20.75])
    writer.writerow([3, "Produto C", 15.00])
    writer.writerow([4, "Produto D", 12.30])
    writer.writerow([5, "Produto E", 18.40])
    writer.writerow([6, "Produto F", 22.90])
    writer.writerow([7, "Produto G", 25.00])
    writer.writerow([8, "Produto H", 30.70])
    writer.writerow([9, "Produto I", 14.80])
    writer.writerow([10, "Produto J", 19.99])

with open("produtos.csv", "r") as file:
    reader = csv.reader(file)
    print("Produtos e Preços:")
    next(reader)  
    for row in reader:
        print(f"{row[1]}: R$ {row[2]}")

with open("produtos.csv", "r") as file:
    reader = csv.reader(file)
    with open("produtos_desconto.csv", "w", newline="") as new_file:
        writer = csv.writer(new_file)
        writer.writerow(next(reader)) 
        for row in reader:
            id, produto, preco = row[0], row[1], float(row[2])
            preco_com_desconto = round(preco * 0.9, 2)  
            writer.writerow([id, produto, preco_com_desconto])