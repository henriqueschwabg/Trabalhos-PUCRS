
-- 1 - Para nascidos neste século (DATA_NASCIMENTO > "2001"), listar AGENTE_CAUSADOR_ACIDENTE, DATA_NASCIMENTO e SEXO, ordenados por DATA_NASCIMENTO descendente, SEXO e AGENTE_CAUSADOR_ACIDENTE.

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
        
-- 2 - Ordenados por número de acidentes em ordem decrescente, listar MUNICIPIO, POPULACAO e número de acidentes, dos 20 municípios com mais acidentes.

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
        NUMERO_ACIDENTES DESC
FETCH FIRST 20 ROWS ONLY;

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
        NUMERO_ACIDENTES DESC
FETCH FIRST 15 ROWS ONLY;

/* 4 - Ordenados por mês/ano, denominações das atividades econômicas e número de acidentes, filtrando por agente causador de acidente, sexo e atividade econômica.
(escolham uma trinca (agente causador de acidente, sexo e atividade econômica) que permita a consulta retornar entre 5 e 30 linhas). */

SELECT
        AGENTE_CAUSADOR_ACIDENTE,
        SEXO,
        CNAE_DENOMINACAO,
        MES_ANO_ACIDENTE,
        COUNT(*) AS NUM_ACIDENTES
FROM
        DUNCANBDA.acid_trab_rs_1
WHERE
        AGENTE_CAUSADOR_ACIDENTE = 'Agente Infeccioso ou' AND
        SEXO = 'Feminino' AND
        CNAE_DENOMINACAO = 'Atividades de atendimento hospitalar'
GROUP BY
        AGENTE_CAUSADOR_ACIDENTE,
        SEXO,
        CNAE_DENOMINACAO,
        MES_ANO_ACIDENTE
ORDER BY
        MES_ANO_ACIDENTE,
        CNAE_DENOMINACAO,
        NUM_ACIDENTES;
        
-- 5 - Listar os 10 municípios e respectivas populações com as maiores taxas de acidentes por 100.000 habitantes.

SELECT
        MUNICIPIO,
        POPULACAO,
        ((COUNT(*) / POPULACAO) * 100000) AS TAXA_ACIDENTES_100M_HAB
FROM
        DUNCANBDA.acid_trab_rs_1
GROUP BY
        MUNICIPIO,
        POPULACAO
ORDER BY
        TAXA_ACIDENTES_100M_HAB DESC
FETCH FIRST 10 ROWS ONLY;

