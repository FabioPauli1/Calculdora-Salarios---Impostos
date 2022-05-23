#pedir hora e quant de Horas
#salario bruto - IR - 3%sind
#informar o FGTS = 11% do salario bruto
#informar salario liqueido (bruto - desc)

horas_valor = float(input('Valor da Hora: '))
horas_quant = int(input('Quantidade de horas: '))

salbr = horas_valor * horas_quant

#IR
if salbr < 900.00:
  ir = 0.0
  ir_r = 'Isento'
elif 900.00 <= salbr < 1500.00:
  ir = salbr * 0.05
  ir_r = '5%'
elif  1500.00 <= salbr < 2500.00:
  ir = salbr * 0.1
  ir_r = '10%'
elif salbr > 2500.00:
  ir = salbr * 0.2
  ir_r = '20%'

sind = salbr * 0.03
fgts = salbr * 0.11
desc = ir + sind + fgts

print(f'Salário Bruto: {horas_valor} * {horas_quant}')
print(f'R$ {salbr}')
print(f'Imposto de Renda: {ir_r}')
print(f'R$ {ir}')
print(f'Total de Descontos: {desc}')
print(f'Salário Liquido: {salbr - desc}') 

