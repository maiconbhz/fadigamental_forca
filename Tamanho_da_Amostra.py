import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.power import TTestPower

# Define os parâmetros
cohen_d = 0.8  # Tamanho do efeito (Cohen's d)
power = 0.8    # Poder desejado (80%)
sig_level = 0.05  # Nível de significância (5%)

# Inicializa o objeto para análise de poder do teste t pareado
power_analysis = TTestPower()

# Calcula o tamanho da amostra para um teste t pareado
sample_size = power_analysis.solve_power(effect_size=cohen_d, power=power, alpha=sig_level, alternative='two-sided')

# Exibe o resultado
print(f"Tamanho ótimo da amostra: {np.ceil(sample_size)} participantes")

# Cria um intervalo de tamanhos de amostra para calcular o poder
sample_sizes = np.arange(5, 41, 1)  # Intervalo de tamanhos de amostra (de 5 a 40)
powers = [power_analysis.power(effect_size=cohen_d, nobs=n, alpha=sig_level, alternative='two-sided') for n in sample_sizes]

# Plota a curva de poder
plt.figure(figsize=(10, 6))
plt.plot(sample_sizes, powers, marker='o', color='#2863A7', label='Poder')
plt.axvline(x=sample_size, color='red', linestyle='--', label=f'Tamanho da Amostra = {np.ceil(sample_size)}')
plt.text(sample_size + 0.5, 0.5, f"Tamanho da Amostra = {np.ceil(sample_size)}", color='black')

# Adiciona rótulos e título ao gráfico
plt.title("Cálculo Amostral", fontsize=14)
plt.xlabel("Tamanho da Amostra", fontsize=12)
plt.ylabel("Poder (1 - β)", fontsize=12)
plt.ylim(0, 1)
plt.legend()
plt.grid()

# Salva o gráfico como uma imagem
plt.savefig(r"C:\Users\CTE\OneDrive\Projetos_de_Pesquisa\CNPq_Universal_2024\calculo_amostral_teste_t_pareado.jpg", dpi=300)
plt.show()
