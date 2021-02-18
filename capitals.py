capitals_dict = {
    'Rio Branco':'Acre',
    'Maceió': 'Alagoas',
    'Macapá': 'Amapá',
    'Manaus': 'Amazonas',
    'Salvador': 'Bahia',
    'Fortaleza': 'Ceará',
    'Vitória': 'Espírito Santo',
    'Goiânia': 'Goiás',
    'São Luís': 'Maranhão',
    'Cuiabá': 'Mato Grosso',
    'Campo Grande': 'Mato Grosso do Sul',
    'Belo Horizonte': 'Minas Gerais',
    'Belém': 'Pará',
    'João Pessoa': 'Paraíba',
    'Curitiba': 'Paraná',
    'Recife': 'Pernambuco',
    'Teresina': 'Piauí',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Natal': 'Rio Grande do Norte',
    'Porto Alegre': 'Rio Grande do Sul',
    'Porto Velho': 'Rondônia',
    'Boa Vista': 'Roraima',
    'Florianópolis': 'Santa Catarina',
    'São Paulo': 'São Paulo',
    'Aracaju': 'Sergipe',
    'Palmas': 'Tocantins',
    'Brasília': 'Distrito Federal'
}

import random

capitals = list(capitals_dict.keys())
points = 0

for i in [1,2,3,4,5]:
    capital = random.choice(capitals)
    state = capitals_dict[capital]
    option = input(capital + 'é a capital de: ')

    if (option == state):
        print("Você acertou, bom trabalho!")
        points += 1
    else:
        print("Errado " + capital + "é a capital de " + state)

print("Fim de jogo!")
if (points >= 3):
    print("Parabés! Você venceu!")
else:
    print("Sinto muito! Você perdeu!")


