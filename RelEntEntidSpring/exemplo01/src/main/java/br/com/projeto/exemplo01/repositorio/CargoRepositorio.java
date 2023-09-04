package br.com.projeto.exemplo01.repositorio;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CargoRepositorio extends CrudRepository<Cargo, Long> {
    
}
