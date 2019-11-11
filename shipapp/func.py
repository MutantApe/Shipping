import numpy as np
import pandas as pd

from datetime import datetime as dt


# main data
def insert_excel_data(selected_datym):
    # Pandas dataframe created
    df = pd.read_excel('/home/muitant/Documents/04oct2018to16apr2019.xlsx', header=[0])

    # data in dataframe without nans
    data = df.loc[3:df.shape[0] - 2]
    print(data)

    # Get noon time series from dataframe
    noon_time_column_data = df['Unnamed: 7'].iloc[3:df.shape[0] - 2]
    # #
    # Convert noon time series into list
    column_list = list(noon_time_column_data)
    # print(column_list)

    print('Noon Time from database : ', selected_datym)
    # timestamp of excel
    selected_datym_stamp = selected_datym.timestamp()
    print('Time Stamp of Noon Time from database : ', selected_datym_stamp)

    # Converted datetime to timestamp
    m = []
    for i in column_list:
        m.append(i.timestamp())
    # print(m)
    # Since the selected noon time from database is in dd/mm/Y 00:00:00+00:00 format so we will pick the timestamp of
    # selected noon time and will convert it back to date time to get dd/mm/Y 00:00:00 format
    selected_datym_reformat = dt.fromtimestamp(selected_datym_stamp)  # dt is defined as datetime in import packages
    print('formatted noon time from DB', selected_datym_reformat)
    if m.__contains__(selected_datym_stamp):
        last_noon_time = noon_time_column_data.iloc[-1]
        print('Last Noon Time', last_noon_time)
        position_of_record = df.index[df['Unnamed: 7'] == selected_datym_reformat].astype(int)[0]
        print('Position of noon time in excel dataframe : ', position_of_record)
        updated_position_of_record = position_of_record + 1
        print('Position from where to update database : ', updated_position_of_record)

        # filtered data
        result = df.iloc[updated_position_of_record:df.shape[0] - 2]
        columns_list = [
            'ship_name',
            'lane',
            'voyage',
            'bound',
            'section',
            'dep_port',
            'next_port',
            'noon_time',
            'costal_time',
            'tym_zone',
            'latitude_degree',
            'latitude_minute',
            'latitude_ns',
            'longitude_degree',
            'longitude_minute',
            'longitude_EW',
            'distance_togo',
            'weather_weather',
            'weather_wind_direction',
            'weather_wind_scale',
            'weather_sea',
            'weather_swell',
            'draught_fore',
            'draught_aft',
            'ballast_m',
            'cargo_onboard',
            'hours_of_operation_total',
            'hours_of_operation_fullspeed',
            'hours_of_operation_anchor',
            'hours_of_operation_shift',
            'hours_of_operation_inport',
            'miles_speed_plus_shifting',
            'miles_full_speed_only',
            'speed_log_water_dept',
            'speed_log_speed_trought_water',
            'average_speed_fsp_acture_ave_speed',
            'average_speed_fsp_propeller_ave_speed',
            'rpm_at_noon',
            'rpm_ave',
            'me_output_kw',
            'thrust',
            'slip',
            'fuel_oil_consume_for_propelling_me',
            'fuel_oil_consume_propelling_ae',
            'fuel_oil_consume_propelling_boiler',
            'fuel_oil_consume_shift_manueuvering_me',
            'fuel_oil_consume_shift_manueuvering_ae',
            'fuel_oil_consume_shift_manueuvering_boiler',
            'fuel_oil_consume_inport_ae',
            'fuel_oil_consume_inport_boiler',
            'me_cyl_oil_consum',
            'me_lub_oil_consum',
            'dg_lub_oil_consum',
            'report_total_consum_inc',
            'bring_frwd_balnc_hshfo',
            'bring_frwd_balnc_hshfo_sulfur',
            'bring_frwd_balnc_lshfo',
            'bring_frwd_balnc_lshfo_sulfur',
            'bring_frwd_balnc_mdo',
            'bring_frwd_balnc_mdo_sulfur',
            'bring_frwd_balnc_lsmdo',
            'bring_frwd_balnc_lsmdo_sulfur',
            'bring_frwd_balnc_me_cyl_oil',
            'bring_frwd_balnc_me_lub_oil',
            'bring_frwd_balnc_dg_lub_oil',
            'replenish_hshfo',
            'replenish_hshfo_sulfur',
            'replenish_lshfo',
            'replenish_lshfo_sulfur',
            'replenish_mdo',
            'replenish_mdo_sulfur',
            'replenish_lsmdo',
            'replenish_lsmdo_sulfur',
            'replenish_me_cyl_oil',
            'replenish_me_lub_oil',
            'replenish_dg_lub_oil',
            'fuel_invnrty_hshfo',
            'fuel_invnrty_lshfo',
            'fuel_invnrty_mdo',
            'fuel_invnrty_lsmdo',
            'rob_hshfo',
            'rob_lshfo',
            'rob_mdo',
            'rob_lsmdo',
            'rob_me_cyl_oil',
            'rob_me_lub_oil',
            'rob_dg_lub_oil',
            'fig_of_consum_replesnish_rob_col1',
            'fig_of_consum_replesnish_rob_col2',
            'actual_total_consum_hshfo',
            'actual_total_consum_lshfo',
            'actual_total_consum_mdo',
            'actual_total_consum_lsmdo',
            'reefer_container_num',
            'sludge_to_store_facility',
            'bilge_to_store_facility',
            'generator_output',
            'remark',
        ]

        result.columns = columns_list
        # return result
        result = result.where(pd.notnull(result), None)
        # return result
    else:
        print('Noon Time does not exist in excel')



