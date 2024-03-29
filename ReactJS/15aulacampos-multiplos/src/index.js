//importar módulos
import React from 'react';
import ReactDOM from 'react-dom';

//componente
class Componente extends React.Component{

    //construtor
    constructor(props){
        super(props);

        this.state = {
            nome : '',
            idade : null
        }
    }

    //função para enviar os dados para os states
    enviarParaState = (campo) => {
        this.setState({[campo.target.name] : campo.target.value});
    }

    
    //render
    render(){
        return(
            <form>
                <input type='text' placeholder='Nome' name='nome' onChange={this.enviarParaState}/>
                <input type='number' placeholder='Idade' name='idade' onChange={this.enviarParaState}/>
                <p>{this.state.nome}</p>
                <p>{this.state.idade}</p>
            </form>
        );
    }

}

//render
ReactDOM.render(<Componente />, document.getElementById('root')); 