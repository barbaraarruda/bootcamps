//importar módulos
import React from 'react';
import ReactDOM from 'react-dom';

//componente
class MeuComponente extends React.Component {

    //função
    mensagem(nome){
        alert('Olá ' + nome);
        console.log(this);
    }

    //Render
    render(){
        return <button onClick={this.mensagem.bind(this, 'Bárbara')}>Clique aqui</button>;
    }
}

//Render
ReactDOM.render(<MeuComponente />, document.getElementById('root'));