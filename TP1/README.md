# Expressão Regular para Strings Binárias sem `011`

## Autor
- Nome: Tiago José Fernandes 
- Numero: A98983
- Foto:  - <img src="fotografia.jpg" alt="Foto" width="120"/>

## Resumo
Este trabalho apresenta uma expressão regular que descreve **todas as cadeias binárias que não contêm a substring `011`.

A lógica é simples:
- As cadeias podem ser compostas apenas pelos dígitos `0` e `1`.
- É proibido que em qualquer posição apareça a sequência `011`.
- Foi também criado um .py para testar a expressao regular.

## Expressão Regular (Final)
```regex
^(?!.*011)[01]*$
