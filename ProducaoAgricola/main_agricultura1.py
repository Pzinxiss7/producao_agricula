from ProducaoAgricola.agricultura1 import ProducaoAgricola

frutas = {
    1: ("Manga", 1.85, 2500),
    2: ("Caju", 0.70, 5100),
    3: ("Umbu", 6.00, 500),
    4: ("Siriguela", 9.54, 1500),
    5: ("Abacaxi", 1.20, 4000)
}

print("=== PRODUÇÃO AGRÍCOLA ===")
hectares = float(input("Informe a quantidade de hectares: "))

print("\nEscolha o tipo de fruta:")
print("1. Manga (R$ 1.85/kg, 2500 kg/hectare)")
print("2. Caju (R$ 0.70/kg, 5100 kg/hectare)")
print("3. Umbu (R$ 6.00/kg, 500 kg/hectare)")
print("4. Siriguela (R$ 9.54/kg, 1500 kg/hectare)")
print("5. Abacaxi (R$ 1.20/kg, 4000 kg/hectare)")

opcao = int(input("Digite o número da fruta escolhida: "))

if opcao == 1:
    nome, preco_kg, produtividade = "Manga", 1.85, 2500
elif opcao == 2:
    nome, preco_kg, produtividade = "Caju", 0.70, 5100
elif opcao == 3:
    nome, preco_kg, produtividade = "Umbu", 6.00, 500
elif opcao == 4:
    nome, preco_kg, produtividade = "Siriguela", 9.54, 1500
elif opcao == 5:
    nome, preco_kg, produtividade = "Abacaxi", 1.20, 4000
else:
    print("Opção inválida.")

producao = ProducaoAgricola(nome, preco_kg, produtividade, hectares)
producao.mostrar_resultados()
