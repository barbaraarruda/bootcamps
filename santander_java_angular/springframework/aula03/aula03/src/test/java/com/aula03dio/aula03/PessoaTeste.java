package com.aula03dio.aula03;

import java.time.LocalDate;
import java.time.LocalDateTime;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;

public class PessoaTeste {
    @Test
    void deveCalcularIdadeCorretamente(){
        Pessoa jessica = new Pessoa(nome: "Jessica", LocalDateTime.of(year: 2000, month: 1, dayOfMonth: 1, hour: 15, minute: 0, second:0));
        Assertions.assertEquals(expected: 22, jessica.getIdade());
    }
}

