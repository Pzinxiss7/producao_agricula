class ProducaoAgricola:
    def __init__(self, fruta, preco_kg, kg_hec, hectares):
        self.fruta = fruta
        self.preco_kg = preco_kg
        self.kg_hec = kg_hec
        self.hectares = hectares

        self.arrendamento = 500
        self.mudas = 300
        self.insumos = 250
        self.mao_obra = 600
        self.energia = 150

    def calcular_gastos_totais(self):
        gasto_por_hec = (
            self.arrendamento +
            self.mudas +
            self.insumos +
            self.mao_obra +
            self.energia
        )
        return gasto_por_hec * self.hectares

    def calcular_valor_bruto(self):
        producao_total = self.kg_hec * self.hectares
        return producao_total * self.preco_kg

    def calcular_lucro(self):
        return self.calcular_valor_bruto() - self.calcular_gastos_totais()

    def mostrar_resultados(self):
        gastos = self.calcular_gastos_totais()
        bruto = self.calcular_valor_bruto()
        lucro = self.calcular_lucro()

        print("\n--- RESULTADO DA PRODUÇÃO ---")
        print(f"Fruta escolhida: {self.fruta}")
        print(f"Gasto total: R$ {gastos:.2f}")
        print(f"Valor bruto (receita): R$ {bruto:.2f}")
        print(f"Valor líquido (lucro): R$ {lucro:.2f}")
        