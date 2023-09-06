//importar módulos
import React from 'react';
import ReactDOM from 'react-dom';

//Componente
class MeuComponente extends React.Component{

    //função
    minhaFuncao = (elemento) => {
        elemento.preventDefault();
        alert('Testando evento onSubmit');
    }

    //render
    render(){
        return(
            <form onSubmit={this.minhaFuncao} action='http://www.google.com'>
                <input type='submit' />
            </form>
        );
    }
}

//render
ReactDOM.render(<MeuComponente />, document.getElementById('root'));