//importar módulos
import React from "react";
import ReactDOM from "react-dom";

//componente
class Componente extends React.Component{

    //render
    render(){

        //vetor
        let cores = ['Azul', 'Amarelo', 'Vermelho'];

        //listar
        let listar = cores.map((cor, index) =>{
            return <li key={index}>{index} - {cor}</li>
        });

        //retorno
        return(
            <ul>
                {listar}
            </ul>
        );
    }
}

//renderizar
ReactDOM.render(<Componente/>, document.getElementById("root"));