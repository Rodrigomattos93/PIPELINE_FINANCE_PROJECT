WITH source_ipca AS (
    SELECT 
        *
    FROM {{ ref("stg_bacen__ipcas")}}
),

source_unemployment AS (
    SELECT
        *
    FROM {{ ref("stg_ibge__unemployments")}}
),

joins_ipca_and_unemployment AS (
    SELECT
        i.id as ipca_id,
        u.id as unemployment_id,
        ipca_value,
        unemployment_value,
        i.date,
        quarter_year
    FROM source_ipca AS i
    JOIN source_unemployment AS u 
        ON i.date = u.date
)

SELECT * FROM joins_ipca_and_unemployment
