select * from duncanbda.acid_trab_rs_1;

/* 1 - Para nascidos neste século (DATA_NASCIMENTO > "2001"), listar AGENTE_CAUSADOR_ACIDENTE, DATA_NASCIMENTO e SEXO, ordenados por DATA_NASCIMENTO descendente, SEXO e AGENTE_CAUSADOR_ACIDENTE. */

SELECT
        AGENTE_CAUSADOR_ACIDENTE,
        DATA_NASCIMENTO,
        SEXO
FROM
        DUNCANBDA.acid_trab_rs_1
WHERE
        DATA_NASCIMENTO > '2001'
ORDER BY
        DATA_NASCIMENTO DESC,
        SEXO,
        AGENTE_CAUSADOR_ACIDENTE;
        
/* 2 - Ordenados por número de acidentes em ordem decrescente, listar MUNICIPIO, POPULACAO e número de acidentes, dos 20 municípios com mais acidentes. */

SELECT
        MUNICIPIO,
        POPULACAO,
        COUNT(*) AS NUMERO_ACIDENTES
FROM
        DUNCANBDA.acid_trab_rs_1
GROUP BY
        MUNICIPIO,
        POPULACAO
ORDER BY 
        3 DESC
FETCH NEXT 20 ROWS ONLY;

/* 3 - Ordenados em ordem decrescente por número de acidentes, listar as 15 primeiras denominações das atividades econômicas (CNAE_DENOMINACAO),
municípios e número de acidentes. (dica, agrupar por CNAE_DENOMINACAO e MUNICIPIO) */

SELECT 
        CNAE_DENOMINACAO,
        MUNICIPIO,
        COUNT(*) AS NUMERO_ACIDENTES
FROM
        DUNCANBDA.acid_trab_rs_1
GROUP BY
        CNAE_DENOMINACAO,
        MUNICIPIO
ORDER BY
        3 DESC
FETCH NEXT 15 ROWS ONLY;

/* 4 - Ordenados por mês/ano, denominações das atividades econômicas e número de acidentes, filtrando por agente causador de acidente, sexo e atividade econômica.
(escolham uma trinca (agente causador de acidente, sexo e atividade econômica) que permita a consulta retornar entre 5 e 30 linhas). */

SELECT
        AGENTE_CAUSADOR_ACIDENTE,
        SEXO,
        CNAE_DENOMINACAO,
        MES_ANO_ACIDENTE,
        COUNT(*)
FROM
        DUNCANBDA.acid_trab_rs_1
GROUP BY
        AGENTE_CAUSADOR_ACIDENTE,
        SEXO,
        CNAE_DENOMINACAO,
        MES_ANO_ACIDENTE
ORDER BY
        MES_ANO_ACIDENTE,
        CNAE_DENOMINACAO,
        5;


/* 5 - Listar os 10 municípios e respectivas populações com as maiores taxas de acidentes por 100.000 habitantes. */

/* Divide-se o número de determinada infração penal ocorrida no município, durante determinado período (geralmente anual), 
pelo número de habitantes do município. Então, multiplica-se o resultado por 100.000. */

SELECT
        MUNICIPIO,
        POPULACAO,
        ((COUNT(*) / POPULACAO) * 100000) AS TAXA_ACIDENTES_100_HAB
FROM
        DUNCANBDA.acid_trab_rs_1
WHERE
        POPULACAO >= 100000
GROUP BY
        MUNICIPIO,
        POPULACAO
ORDER BY
        3 DESC
FETCH NEXT 10 ROWS ONLY;


