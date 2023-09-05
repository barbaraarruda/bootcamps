//importar módulos
import React from 'react';
import ReactDOM from 'react-dom';

//componente 
class Componente extends React.Component{
    render(){
        return ( //<h1>Olá {this.props.nome} </h1>
            <div>
                <p>{this.props.informacoes.nome}</p>
                <p>{this.props.informacoes.idade}</p>
            </div>
            
        );
    }
}

//JSON
var dados = {nome:"Bárbara", idade:25};

//render
ReactDOM.render(<Componente informacoes={dados} />, document.getElementById('root'));