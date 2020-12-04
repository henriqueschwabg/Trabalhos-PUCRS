select * from G01 fetch first 10 rows only;

-- Consulta 1
select AGENTE_CAUSADOR_ACIDENTE, DATA_NASCIMENTO, SEXO from G01
where DATA_NASCIMENTO > '2001'
order by DATA_NASCIMENTO desc, SEXO, AGENTE_CAUSADOR_ACIDENTE;

-- Consulta 2
select MUNICIPIO, POPULACAO, count(*) as NUMERO_ACIDENTES from G01
group by MUNICIPIO, POPULACAO
order by NUMERO_ACIDENTES desc
fetch first 20 rows only;

-- Consulta 3
select CNAE_DENOMINACAO, MUNICIPIO, count(*) as NUMERO_ACIDENTES from G01
group by CNAE_DENOMINACAO, MUNICIPIO
order by NUMERO_ACIDENTES desc
fetch first 15 rows only;

-- Consulta 4
select MES_ANO_ACIDENTE, CNAE_DENOMINACAO, count(*) as NUMERO_ACIDENTES from G01
where AGENTE_CAUSADOR_ACIDENTE = 'Agente Infeccioso ou'
and SEXO = 'Feminino'
and CNAE_DENOMINACAO = 'Atividades de atendimento hospitalar'
group by MES_ANO_ACIDENTE, CNAE_DENOMINACAO
order by MES_ANO_ACIDENTE;

-- Consulta 5
select MUNICIPIO, POPULACAO, ((count(*) / POPULACAO) * 100000) as TAXA_ACIDENTES_100MIL_HAB from G01
group by MUNICIPIO, POPULACAO
order by TAXA_ACIDENTES_100MIL_HAB desc
fetch first 10 rows only;
