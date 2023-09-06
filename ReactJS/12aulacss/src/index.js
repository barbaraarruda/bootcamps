//importar módulos
import React from 'react';
import ReactDOM from 'react-dom';
import './style.css';

//componente
class Componente extends React.Component{

    //render
    render(){

        const estilo = {
            color: 'blue',
            backgroundColor: 'yellow',
            borderBottom: '1px solid black'   
        }
        return(
            <div>
                <h1 style={{color:'pink', backgroundColor:'black'}}>CSS interno</h1>
                <h1 style={estilo}>CSS através de variáveis e constantes</h1>
                <h1 className='minhaClasse'>CSS através de classes</h1>
            </div>
        );
    }
}

//renderizar
ReactDOM.render(<Componente />, document.getElementById('root'));   