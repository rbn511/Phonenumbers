import phonenumbers

#ajuste do telefone pra usarmos o phonenumbers
telefone = "+5521999999999"
telefone_ajustado = phonenumbers.parse(telefone)
print(telefone_ajustado)

# descobrir a localização do telefone

from phonenumbers import geocoder
local = geocoder.description_for_valid_number(telefone_ajustado, 'pt-br')
print(local)

#formatar o número de telefone
telefone_formulario = "21999999999"
telefone_formulario_ajustado = phonenumbers.parse(telefone_formulario, "BR")
telefone_formatado = phonenumbers.format_number(telefone_formulario_ajustado, phonenumbers.PhoneNumberFormat.NATIONAL)

print(telefone_formatado)

#descobrir a operadora do telefone
from phonenumbers import carrier
operadora = carrier.name_for_number(telefone_ajustado, "pt-br")
print(operadora)

#retirar um telefone de um texto
corpo_email = """
Prezados

Quando tiverem outra resposta da proposta, favor entrar em contato.

Att,
Rodolfo
(21)999999999"""
for telefone in phonenumbers.PhoneNumberMatcher(corpo_email, "BR"):
    print(telefone)