# Arquitetura de Sistemas IoT

Este repositorio contem o material didatico e os exemplos praticos das aulas de Arquitetura de Internet das Coisas (IoT). O curso aborda desde o desenvolvimento de firmware em microcontroladores ate a integracao com scripts de processamento de dados.

## Objetivo
O objetivo deste material e fornecer uma base solida sobre a integracao entre hardware e software, focando na coleta, transmissao e tratamento de informacoes provenientes de dispositivos inteligentes.

## Tecnologias Utilizadas

### Hardware e Microcontroladores
- Plataforma Arduino (Uno, Nano, Mega)
- Microcontroladores com conectividade (ESP32 / ESP8266)
- Sensores (Temperatura, Umidade, Presenca, Ultrassonico)
- Atuadores (Reles, Servomotores, LEDs)

### Linguagens de Programacao

#### C++ (Firmware)
A linguagem C++ e utilizada para o desenvolvimento do codigo que reside no hardware (Arduino).
- Gerenciamento de portas de entrada e saida (GPIO)
- Implementacao de protocolos de comunicacao local (I2C, SPI, UART)
- Controle de interrupcoes e temporizadores
- Bibliotecas de sensores e drivers de baixo nivel

#### Python (Backend e Integracao)
A linguagem Python e utilizada para a camada de gateway, processamento de dados e interface com o usuario.
- Comunicacao Serial com dispositivos Arduino (Biblioteca PySerial)
- Implementacao de protocolos de rede (MQTT, HTTP)
- Manipulacao e armazenamento de dados recebidos
- Automacao de tarefas e integracao com APIs externas

## Conteudo Programatico

1. Introducao a Arquitetura IoT
   - Camadas da arquitetura (Percepcao, Rede, Aplicacao)
   - Protocolos de comunicacao

2. Desenvolvimento com Arduino e C++
   - Estrutura de codigo (setup e loop)
   - Leitura de sensores analogicos e digitais
   - Controle de dispositivos de saida

3. Conectividade e Comunicacao
   - Integracao Serial entre Arduino e Computador
   - Introducao ao protocolo MQTT para dispositivos moveis

4. Processamento de Dados com Python
   - Leitura de dados da porta serial
   - Armazenamento em arquivos e bancos de dados simples
   - Criacao de scripts para monitoramento em tempo real

## Estrutura do Repositorio

- /firmware: Codigos fonte em C++ desenvolvidos para a IDE Arduino.
- /scripts: Scripts em Python para comunicacao e tratamento de dados.
- /docs: Esquemas de montagem e documentacao teorica.

## Requisitos de Software
- Arduino IDE
- Python 3.x
- Bibliotecas Python: pyserial, paho-mqtt
- Editor de texto ou IDE (VS Code sugerido)