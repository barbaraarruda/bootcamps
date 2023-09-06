//importando módulos
import React from "react";
import ReactDOM from "react-dom";

//componentes
class Componente extends React.Component{

    //construtor
    constructor(props){
        super(props);

        this.state={exibir : false};

    }

    //função
    alterarState = () =>{
        let converter = !this.state.exibir;
        this.setState({exibir : converter});
    }

    //render
    render(){
        //condicional
        let meuTexto = '';
        if(this.state.exibir == true){
            meuTexto = <h1>Olá! Utilizando condicionais</h1>
        }else{
            meuTexto = ''
        }

        //retorno
        return(
            <div>
                {meuTexto}
               <button onClick={this.alterarState}>Clique Aqui</button>
            </div>
        )
    }
}

//Renderizando o componente
ReactDOM.render(<Componente />, document.getElementById("root"));