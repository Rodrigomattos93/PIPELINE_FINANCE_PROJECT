WITH 
source AS (
    SELECT * FROM {{ source('public', 'unemployment')}}
),

renamed AS (
    SELECT
        id,
        quarter_year,
        left(quarter_year::text, 4) as year,
        right(quarter_year::text, 2) as quarter,
        CASE 
            WHEN right(quarter_year::text, 2) = '01' then array[1,2,3]
            WHEN right(quarter_year::text, 2) = '02' then array[4,5,6]
            WHEN right(quarter_year::text, 2) = '03' then array[7,8,9]
            WHEN right(quarter_year::text, 2) = '04' then array[10,11,12]
        END AS month_list,
        unemployment_value
    FROM source
),

cleaned_data AS (
    SELECT 
    id,
    quarter_year,
    year,
    quarter,
    month_list,
    unnest(month_list) as month,
    unemployment_value
FROM renamed
)

SELECT 
    id,
    quarter_year,
    year,
    quarter,
    month_list,
    month,
    make_date(year::int, month, 1) as date,
    unemployment_value
FROM cleaned_data