WITH source AS (
    SELECT
        quarter_year,
        date,
        ipca_value,
        unemployment_value        
    FROM {{ ref("int_joins_ipca_and_unemployment")}}
),

lagged_values AS (
    SELECT
        quarter_year,
        date,
        ipca_value,
        unemployment_value,
        LAG(unemployment_value) OVER (
            ORDER BY date
        ) AS lagged_unemployment
    FROM source
),

finalized_indicators AS (
    SELECT 
        quarter_year,
        date,
        ipca_value,
        (EXP(SUM(LN(1 + ipca_value / 100.0)) OVER (
            PARTITION BY quarter_year
            ORDER BY date
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        )) - 1)*100 AS ipca_quarter_cumulative,
                (EXP(SUM(LN(1 + ipca_value / 100.0)) OVER (
            ORDER BY date
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        )) - 1)*100 AS ipca_cumulative,
        unemployment_value,
        (((unemployment_value / lagged_unemployment)-1)*100) as percent_change_unemployment
    FROM 
        lagged_values
)

SELECT 
    quarter_year,
    date,
    ipca_value,
    ipca_quarter_cumulative,
    ipca_cumulative,
    unemployment_value,
    NULLIF(percent_change_unemployment, 0) AS percent_change_unemployment
FROM finalized_indicators ORDER BY date ASC
