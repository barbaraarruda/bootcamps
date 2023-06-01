function fn(){
    log('Hosting de Função');

    function log(value){
        console.log(value);
    }
}

fn();

/**
 * function fn(){
 *     function.log(value){
 *          console.log(value);
 *      }
 * 
 *  log('Hoisting de Função);
 * }
 */