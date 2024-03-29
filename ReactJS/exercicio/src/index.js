//importar módulos
import React from 'react';
import ReactDOM from 'react-dom';

//componente
class MeuComponente extends React.Component {

    //construtor
    constructor(props){
        super(props);

        this.state = {texto: this.props.textoInicial};
    }

    //função
    minhaFuncao = (elemento) => {
        this.setState({texto: elemento.target.value});
    }

    //Render
    render(){
        return(
            <div>
                <h1>{this.state.texto}</h1>
                <input type='text' onChange={this.minhaFuncao} value={this.state.texto}/>
            </div>
        );
    }
}

//Render
ReactDOM.render(<MeuComponente textoInicial='Digite algo...'/>, document.getElementById('root'));