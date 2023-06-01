function clicou(){

    document.getElementById("agradecimento").innerHTML = "<b>Obrigado por clicar.</b>";
    //console.log(document.getElementById("agradecimento"));
    //alert("Obrigado por clicar");
}

function redirecionar(){
    window.open("https://www.google.com/"); //abre em nova aba.
    //window.location.href = "https://www.google.com/"; //esse redireciona automaticamente.

}

function trocar(elemento){
    //document.getElementById("mousemove").innerHTML = "Obrigado por passar o mouse";
    //alert("Trocar texto");
    elemento.innerHTML = "Obrigado por passar o mouse";
}

function voltar(elemento){
    //document.getElementById("mousemove").innerHTML = "Passe o mouse aqui";
    elemento.innerHTML = "Passe o mouse aqui" //esse método é alternativo ao document.getelementbyid
}

function load(){
    alert("Página carregada");
}

function funcaoChange(elemento){
    console.log(elemento.value);
}

/*
function soma(n1, n2){
    return n1 + n2;
}
*/

/*

function validaIdade(idade){
    var validar; //variável local
    if(idade >= 18){
        validar = true
    }else{
        validar = false
    }
    return validar;
}

var idade = prompt("Qual sua idade?");
console.log(validaIdade(idade));
*/


//alert(soma(5,10));




/*
var d = new Date(); //como inserir data no js.
//alert(d); //mostra a data e horário completos.
//alert(d.getMonth()+1); //o month sempre parte do zero, por isso se faz necessário acrescentar o +1.
//alert(d.getMinutes());
//alert(d.getHours());
//alert(d.getDay());
*/


/*
var count;
for(count = 0; count <= 5; count++){
    alert(count);
};
*/

/*
var count = 0;
while (count < 5){
    console.log(count);
    alert(count);
    count++;; //pode colocar o ++ ou +1, ambos serão adicionando +1.
};
*/

/*
var idade = prompt("Qual sua idade"); //serve para coletar informações.
if (idade >= 18){
    alert("maior de idade");
}else{
    alert("menor de idade");
};
*/


/*
var frutas = [{nome:"maçã", cor:"vermelha"}, {nome:"uva", cor:"roxa"}]
console.log(frutas);
alert(frutas[1].nome);
*/

/*
var fruta = {nome:"maçã", cor:"vermelha"}
console.log(fruta.nome);
alert(fruta.cor);
*/

//var lista = ["maçã", "pêra", "laranja"];
///lista.push("uva"); //acrescenta elementos na lista
//lista.pop(); //retira elemento. Aqui ele retirou o último.
//console.log(lista[0]);
//alert(lista[1]);
///console.log(lista.length); //tamannho da lista.
//console.log(lista.reverse()); //esse é um método. Inverte a ordem dos elmentos da lista.
//console.log(lista.toString()); //tira a array e vira string. Quando especifica apenas um elemento [], imprime apenas a letra referente.
//console.log(lista.join(" - ")); //coloca o que quiser entre os elementos.




//var nome = "Bárbara Arruda";
//var idade = 24;
//var idade2 = 10;
//var frase = "Japão é o melhor time do mundo";
//alert(nome + " tem " + idade + " anos"); //adiciona pop-up na página.
//alert(idade + idade2)
//console.log(nome);
//console.log(idade);
///console.log(frase.replace("Japão", "Coreia do Sul"));
//console.log(frase.toUpperCase());
///alert(frase.replace("Japão", "Coreia do Sul");