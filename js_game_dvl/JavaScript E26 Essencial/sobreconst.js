const name = 'Bárbara';

//não podemos alterar o valor
name = 'Bárbara';

const user = {
    name: 'Bárbara'
};

//mas se for um objeto, podemos trocar suas propriedades
user.name = 'Outro nome';

//não podemos fazer o objeto "apontar" para outro lugar
user = {
    name: 'Bárbara'
};

const persons = ['Bárbara', 'Mariana', 'Ana'];

//Podemos adicionar novos itens
persons.push('Sabrina');

//Podemos remover algum item
persons.shift();

//Podemos alterar diretamente
persons[2] = 'Carina';

console.log('\nArray após as alterações: ', persons);

