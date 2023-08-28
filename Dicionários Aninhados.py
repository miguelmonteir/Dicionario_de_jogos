import pprint

jogos = {

    'lego jurassic park':{
        'ano_de_lançamento':2015,  
        'generu':['aventura,dinossauros'],     
        'Classificação':8.8
    
    } ,  

    'Lego City':{
        'ano_de_lançamento':2018,
        'generu':['aventura,oline'],
        'Classificação':7.7

    },
    
    'LEGO DC Super Vilões':{
        'ano_de_lançamento':2020,
        'generu':['aventura,oline'],
        'Classificação':9.7

    },
    
    'LEGO Harry Potter ':{
        'ano_de_lançamento':2016,
        'generu':['aventura,magia'],
        'Classificação':8.3
    
    } ,  

    'LEGO Batman 2':{
        'ano_de_lançamento':2018,
        'generu':['aventura,oline'],
        'Classificação':7.4

    },
    
    'LEGO Senhor dos Anéis':{
        'ano_de_lançamento':2017,
        'generu':['aventura,oline,magia'],
        'Classificação':5.5

    },

}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(jogos)

#1 Buscar informacao dentor do dicio nario aninhado
print(jogos['LEGO Senhor dos Anéis']['generu'])

#2 Adicionar um novo item
jogos ['LEGO Senhor dos Anéis']['players'] = 1
print(jogos['LEGO Senhor dos Anéis'])

#3 Excluir um dicionario
del jogos['LEGO Batman 2']
pp.pprint(jogos)