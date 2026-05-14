#  Lógica de Programação 

Este documento provê uma análise técnica e estruturada sobre o desenvolvimento de algoritmos utilizando Python e os protocolos de versionamento profissional com Git e GitHub.

## 1. Lógica de Programação e Algoritmos em Python

A lógica de programação é o raciocínio estruturado aplicado ao desenvolvimento de software. Python é a ferramenta para traduzir esse raciocínio em instruções executáveis.

### 1.1 Variáveis e Estrutura de Memória
Python utiliza referências a objetos. A declaração de variáveis não exige tipos explícitos, mas a integridade dos dados é mantida pela tipagem forte.

- Inteiros (int): Representação de valores numéricos integrais.
- Ponto Flutuante (float): Representação de valores reais com precisão decimal.
- Booleano (bool): Operadores binários (True ou False) fundamentais para álgebras de decisão.
- String (str): Sequências imutáveis de caracteres.

### 1.2 Estruturas de Dados Avançadas
- Listas (List): Coleções indexadas e mutáveis de elementos.
- Dicionários (Dict): Estruturas baseadas em tabelas de dispersão (hash maps) para mapeamento de chave-valor.
- Tuplas (Tuple): Sequências imutáveis, ideais para integridade de dados constantes.
- Conjuntos (Set): Coleções não ordenadas de elementos únicos para operações matemáticas de conjuntos.

### 1.3 Estruturas de Controle de Fluxo
O fluxo de execução é controlado por avaliações lógicas e ciclos de repetição.

#### Condicionais (Seleção)
Utilizam operadores relacionais (==, !=, >, <, >=, <=) e lógicos (and, or, not).
```python
if condicao_a:
    # Execução prioritária
elif condicao_b:
    # Alternativa lógica
else:
    # Tratamento de exceção ou fluxo residual