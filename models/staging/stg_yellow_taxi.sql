SELECT
    vendor_id,
    pickup_datetime,
    dropoff_datetime,
    passenger_count,
    trip_distance,
    payment_type,
    fare_amount,
    tip_amount,
    total_amount,
    pu_location_id AS pickup_location_id,
    do_location_id AS dropoff_location_id
FROM {{ source('raw', 'yellow_taxi') }}
WHERE trip_distance > 0
  AND fare_amount >= 0
  AND pickup_datetime >= '2023-01-01'
  AND pickup_datetime < '2023-02-01'
