SELECT CAST(pickup_datetime AS DATE) as trip_date ,
        count(*) as total_trips,
        Sum(total_amount) as total_revenue,
        AVG(trip_distance) as avg_trip_distance
from {{ ref('stg_yellow_taxi') }}
Group by CAST(pickup_datetime AS DATE) 
order by trip_date