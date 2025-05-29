WITH 
source AS (
    SELECT * FROM {{ source('public', 'ipca')}}
),

cleaned_data AS (
    SELECT
        id,
        ipca_value,
        date::date as date
    FROM
        source)

SELECT * FROM cleaned_data
