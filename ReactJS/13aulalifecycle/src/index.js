//importar módulos
import React from 'react';
import ReactDOM from 'react-dom';

//componente

class Componente extends React.Component{
    //construtor
    constructor(props){
        super(props);

        this.state = {cor: 'vermelho'};
    }
    
    //depois de realizar o render
    componentDidMount(){
        setTimeout(() => {
            this.setState({cor: 'azul'});
        }, 2000);
    }

    //render
    render(){
        return(
            <h1>A cor escolhida é {this.state.cor}</h1>
        );
    }
}

//render
ReactDOM.render(<Componente />, document.getElementById('root'));   