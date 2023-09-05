// importar módulos
import React from 'react';
import ReactDOM from 'react-dom';

//componente
class MeuComponente extends React.Component {

    //função
    mensagem(){
        alert('Hello World');
    }

    //Render
    render(){
        return <button onClick={this.mensagem}>Clique aqui</button>;
    }
}

//Render
ReactDOM.render(<MeuComponente />, document.getElementById('root'));