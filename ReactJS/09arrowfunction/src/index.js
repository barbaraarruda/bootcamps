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

    minhaArrowFunction = (curso) => {
        alert('Estou fazendo o curso de ' + curso);
        console.log(this);
    } 

    teclado = (obj) =>{
        //alert('tecla pressionada');
        console.log(obj.target.value);
    }


    //Render
    render(){
        return (
            <div>
                <button onClick={this.mensagem.bind(this, 'Bárbara')}>Clique aqui</button>
                <button onClick={() => this.minhaArrowFunction('ReactJS')}>Arrow Function</button>

                <hr />
                <input type='text' onChange={this.teclado}/>
            </div>
        );
        
    }
}

//Render
ReactDOM.render(<MeuComponente />, document.getElementById('root'));