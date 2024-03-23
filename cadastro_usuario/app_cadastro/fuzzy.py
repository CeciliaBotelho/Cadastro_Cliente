import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def calcular_credito(idade, renda_mensal):
    # Ajustes para mapear corretamente os valores de idade e renda
    idade_real = idade
    renda_mensal_real = renda_mensal

    # Faixas para idade e renda mensal ajustadas conforme as categorias definidas
    idade_fuzzy = ctrl.Antecedent(np.arange(0, 100, 1), 'idade')
    renda_mensal_fuzzy = ctrl.Antecedent(np.arange(0, 60000, 1), 'renda mensal')

    # Faixas para crédito ajustadas para representar valores de 1500 a 60000
    credito = ctrl.Consequent(np.arange(1500, 60001, 1), 'credito')

    # Definindo os conjuntos fuzzy para idade
    idade_fuzzy['jovem'] = fuzz.trimf(idade_fuzzy.universe, [0, 30, 65])
    idade_fuzzy['medio'] = fuzz.trimf(idade_fuzzy.universe, [30, 65, 100])
    idade_fuzzy['idoso'] = fuzz.trimf(idade_fuzzy.universe, [65, 100, 100])

    # Definindo os conjuntos fuzzy para renda mensal
    renda_mensal_fuzzy['pobre'] = fuzz.trimf(renda_mensal_fuzzy.universe, [0, 0, 5000])
    renda_mensal_fuzzy['medio'] = fuzz.trimf(renda_mensal_fuzzy.universe, [5000, 10000, 15000])
    renda_mensal_fuzzy['rico'] = fuzz.trimf(renda_mensal_fuzzy.universe, [15000, 20000, 60000])

    # Definindo os conjuntos fuzzy para crédito
    credito['baixo'] = fuzz.trimf(credito.universe, [1500, 1500, 21500])
    credito['medio'] = fuzz.trimf(credito.universe, [21500, 30000, 41500])
    credito['alto'] = fuzz.trimf(credito.universe, [41500, 60000, 60000])

    # Definindo as regras fuzzy
    regra1 = ctrl.Rule(idade_fuzzy['jovem'] & renda_mensal_fuzzy['rico'], credito['alto'])
    regra2 = ctrl.Rule(idade_fuzzy['medio'] & renda_mensal_fuzzy['rico'], credito['alto'])
    regra3 = ctrl.Rule(idade_fuzzy['idoso'] & renda_mensal_fuzzy['rico'], credito['medio'])
    regra4 = ctrl.Rule(idade_fuzzy['medio'] & renda_mensal_fuzzy['medio'], credito['medio'])
    regra5 = ctrl.Rule(idade_fuzzy['jovem'] & renda_mensal_fuzzy['medio'], credito['medio'])
    regra6 = ctrl.Rule(idade_fuzzy['idoso'] & renda_mensal_fuzzy['medio'], credito['medio'])
    regra7 = ctrl.Rule(idade_fuzzy['jovem'] & renda_mensal_fuzzy['pobre'], credito['medio'])
    regra8 = ctrl.Rule(idade_fuzzy['medio'] & renda_mensal_fuzzy['pobre'], credito['baixo'])
    regra9 = ctrl.Rule(idade_fuzzy['idoso'] & renda_mensal_fuzzy['pobre'], credito['baixo'])

    # Criando o sistema de controle
    sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9])

    # Criando a simulação
    simulacao = ctrl.ControlSystemSimulation(sistema_controle)

    # Definindo as entradas
    simulacao.input['idade'] = idade_real
    simulacao.input['renda mensal'] = renda_mensal_real

    # Calculando o crédito
    simulacao.compute()

    # Retornando o valor de crédito, adicionando 1500
    return simulacao.output['credito'] + 1500
