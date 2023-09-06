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

    //função - nome
    funcaoNome = (campo) => {
        this.setState({nome : campo.target.value});
    }

    //função - idade
    funcaoIdade = (campo) => {
        this.setState({idade : campo.target.value});
    }

    //render
    render(){
        return(
            <form>
                <input type='text' placeholder='Nome' onChange={this.funcaoNome}/>
                <input type='number' placeholder='Idade' onChange={this.funcaoIdade}/>
                <p>{this.state.nome}</p>
                <p>{this.state.idade}</p>
            </form>
        );
    }

}

//render
ReactDOM.render(<Componente />, document.getElementById('root')); 