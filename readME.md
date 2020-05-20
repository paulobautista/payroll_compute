# This is to compute for payroll

This uses payroll data and payscheme matrix to output computation

## Getting Started

Route Data - query from metabase:
`select route_id,  route_date, courier_id as rider_id, courier_name as rider_name , depot_id as hub_id , depot_name as hub_name, scheme_type, courier_type as driver_type, parcels_delivered   from ph_views.fleet_performance_base_data where depot_id in (1,3) and fleet_type = 'Last - Mile' and route_start between {{start_date}} and {{end_date}}`

Pay Scheme Data -
csv_template = `https://docs.google.com/spreadsheets/d/1xlSAU5Idg-CgXS6Z7iwYS6AQlOaa2CGlo7ZJcpMGCMY/edit?usp=sharing`

columns = (hub_id,hub_name,zone_id,zone_name,driver_type,min_parcel,max_parcel,daily_min_wage,	per_parcel_rate,fixed_component,fixed_incentive_component)

"testing"
