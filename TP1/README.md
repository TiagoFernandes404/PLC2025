# Expressão Regular para Strings Binárias sem `011`

## Autor
- **Nome:** Tiago José Fernandes  
- **Número:** A98983  
- **Foto:**  
  <img width="180" height="180" alt="Fotografia" src="https://github.com/user-attachments/assets/e18badb7-9116-4655-af0c-2739ae2570ce" />

## Resumo
Este trabalho apresenta uma expressão regular que descreve **todas as cadeias binárias que não contêm a substring `011`**.

A lógica é simples:
- As cadeias podem ser compostas apenas pelos dígitos `0` e `1`.
- É proibido que, em qualquer posição, apareça a sequência `011`.
- Foi também criado um script em Python (`.py`) para testar a expressão regular.

## Lista de resultados
- Ficheiro com a expressão pedida
[TP1.txt](TP1.txt)
- Ficheiro de codigo Python
[TP1.py](TP1.py)

  ## Solução
```regex
^(?!.*011)[01]*$
