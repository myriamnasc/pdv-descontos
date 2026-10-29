# PDV de Descontos — Nível 1

## 1. O que o código faz

Este projeto consiste em um sistema simples de Ponto de Venda (PDV), desenvolvido em Python, que calcula descontos sobre compras de acordo com a idade do cliente e o valor da compra. O programa permite registrar várias compras, armazenar os valores em uma lista e, ao final, apresentar um resumo com a quantidade de compras realizadas, o total bruto, o total de descontos concedidos e o valor final das vendas.

## 2. Como ele faz

O funcionamento do programa segue as seguintes etapas:

1. **Recebimento dos dados:** o programa solicita o valor da compra e a idade do cliente.
2. **Validação:** verifica se o valor da compra ou a idade são negativos. Caso sejam, exibe uma mensagem de aviso.
3. **Desconto por idade:** se o cliente tiver 65 anos ou mais, aplica um desconto de 20% sobre o valor da compra.
4. **Desconto por valor:** após o desconto por idade, verifica se o valor restante é maior que R$ 100,00. Se for, aplica mais 10% de desconto sobre esse valor.
5. **Registro da compra:** armazena o valor original, o desconto concedido e o valor final em uma lista, utilizando o método `.append()`.
6. **Repetição das compras:** utiliza uma estrutura de repetição `while` para permitir o registro de várias compras. O programa encerra quando o usuário digita `0` no valor da compra.
7. **Resumo do dia:** ao encerrar, utiliza `len()` para contar as compras e uma estrutura `for` para somar os valores registrados, exibindo o total bruto, os descontos e o valor final das vendas.

## 3. Como rodar

Certifique-se de ter o Python instalado no computador.

No terminal, acesse a pasta `nivel_1` e execute o comando:

```bash
python pdv.py
```

Em seguida, informe o valor da compra e a idade do cliente conforme solicitado pelo programa.

Para encerrar o registro de compras e visualizar o resumo do dia, digite `0` no campo do valor da compra.

## 4. Tabela de exemplos

A tabela a seguir apresenta casos de teste para verificar a aplicação dos descontos por idade e por valor da compra.

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---|---:|---:|---:|---:|---:|
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |

Como usar a tabela
1. Rode seu programa.
2. Digite o valor e a idade de cada linha.
3. Compare o valor final mostrado no console com a coluna “Valor final esperado”.
4. Se todos baterem ✅ — seu código está correto. Se algum divergir ❌ — revise a ordem das regras (lembre-se: o desconto de 10% é aplicado sobre o valor já descontado pela idade, não sobre o valor original).