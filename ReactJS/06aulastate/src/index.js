// importar módulos
import React from 'react';
import ReactDOM from 'react-dom';

//componente
class Componente extends React.Component {

    //construtor
    constructor(props){
        super(props);

        this.state = {nome: 'Bárbara'};
    }

    //Render
    render(){
        return <h1>{this.state.nome}</h1>
    }

}

//Render
ReactDOM.render(<Componente />, document.getElementById('root'));