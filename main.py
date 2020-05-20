import pandas as pd

def get_scheme_rate(row):
    ps = pd.read_csv('sample_payscheme.csv')
    hub = ps.hub_id == row.hub_id
    driver_type = ps.driver_type ==row.driver_type
    min_parcel = ps.min_parcel < row.parcels_delivered
    rate_card =  tuple(ps.loc[hub & driver_type & min_parcel].agg({'per_parcel_rate':'max','daily_min_wage':'max','fixed_component':'max','fixed_incentive_component':'max'}).fillna(0))
    revenue = (rate_card[0] * row.parcels_delivered) + (sum(rate_card[1:]))
    return revenue,rate_card

def main():
    df = pd.read_csv('sample_route_data.csv')

    df['result'] = df.apply(get_scheme_rate,axis=1)
    df['delivery_pay']  = [x[0] for x in df.result]

    df.groupby(['rider_id','rider_name','hub_id','hub_name','driver_type']).agg({'parcels_delivered':'sum','route_date':'nunique','delivery_pay':'sum'}).reset_index().to_csv('rider_level.csv',index=False)
    df.groupby(['hub_id','hub_name']).agg({'parcels_delivered':'sum','route_date':'nunique','delivery_pay':'sum'}).reset_index().to_csv('hub_level.csv',index=False)

if __name__ == '__main__':
    main()
