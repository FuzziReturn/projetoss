# 💧 Sistema de Consumo de Água

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![GitHub](https://img.shields.io/badge/GitHub-Projeto-black?logo=github)

## 📌 Sobre o projeto

O **Sistema de Consumo de Água** é um programa desenvolvido em Python com o objetivo de classificar o consumo mensal de água de acordo com o tipo de imóvel.

O usuário informa o tipo de imóvel e o consumo mensal em metros cúbicos (m³). O sistema verifica essas informações e apresenta uma mensagem de acordo com as regras definidas no projeto.

## 🎯 Objetivo

O objetivo do projeto é praticar conceitos básicos de programação em Python, principalmente:

- Entrada de dados;
- Variáveis;
- Conversão de valores;
- Estruturas condicionais (`if`, `elif` e `else`);
- Operadores de comparação;
- Organização de um projeto no GitHub.

## 🐍 Linguagem utilizada

- Python 3.x

## 🏠 Tipos de imóvel

O sistema trabalha com três tipos de imóvel:

- 🏢 Comercial
- 🏠 Casa
- 🏙️ Apartamento

## 📊 Regras de classificação

O programa utiliza as seguintes regras:

### 🏢 Imóvel comercial

Quando o imóvel é comercial, o sistema apresenta:

> Tarifa comercial aplicada – consulte o plano corporativo.

### 🏙️ Apartamento

Para apartamentos:

- Menos de **10 m³**:
  - Consumo econômico – excelente controle de água!

- Entre **10 m³ e 25 m³**:
  - Consumo moderado – dentro do padrão residencial.

- Acima de **25 m³**:
  - Consumo excessivo – adote medidas de economia e verifique vazamentos.

### 🏠 Casa

Para os outros casos que não se encaixam nas regras anteriores, o sistema apresenta:

> Consumo excessivo – adote medidas de economia e verifique vazamentos.

