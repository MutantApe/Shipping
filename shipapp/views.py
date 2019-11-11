from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from shipapp.func import insert_excel_data
from shipapp.models import YangMIng_Daily_Noon
from datetime import datetime


# Create your views here.


@api_view(['GET'])
def insert_table_data(request):
    try:

        # URL parameters
        entered_date_time = request.GET.get("date")

        # Converting entered_date_time which is string into datetime
        dt_string = entered_date_time
        # Considering date is in dd/mm/yy format
        dt_object = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
        print("dt_object1 =", dt_object)

        # Converting entered date_time into timestamp
        entered_date_time_stamp = dt_object.timestamp()
        print(entered_date_time_stamp)

        noon_date_time = YangMIng_Daily_Noon.objects.values_list('noon_time', flat=True)
        # print(noon_date_time)

        # Check whether entered date is in the database or not through their timestamps
        m = []
        for i in noon_date_time:
            m.append(i.timestamp())
            # print(m)
        if m.__contains__(entered_date_time_stamp):
            print("Entered Noon Time exist in Database")

            # Get latest date time from database
            field_name = 'noon_time'
            obj = YangMIng_Daily_Noon.objects.last()
            latest_date_time = getattr(obj, field_name)
            # print(latest_date_time)

            # Convert latest_date_time into timestamp
            latest_date_time_stamp = latest_date_time.timestamp()
            print(latest_date_time_stamp)
            if latest_date_time_stamp != entered_date_time_stamp:
                print("Entered Noon Time is not the latest")
            else:
                print("Entered Noon Time is latest")

                # Function Call to Update latest data
                excel_data = insert_excel_data(latest_date_time)

                # for index, row in excel_data.iterrows():
                #     row_dict = dict(row)
                #     print(index)
                # YangMIng_Daily_Noon.objects.create(**row_dict)
        else:
            print("Entered Noon Time is not in Database")

        # Getting some last entries from table
        field_name = 'noon_time'
        obj = YangMIng_Daily_Noon.objects.last()
        latest_date_time = getattr(obj, field_name)

        last_entries = YangMIng_Daily_Noon.objects.filter(noon_time= latest_date_time).values('ship_name', 'voyage',
                                                                                              'dep_port', 'next_port',
                                                                                              'noon_time', 'remark')
        print(last_entries)

        return Response(status=status.HTTP_200_OK, data={'Last Entries In DB': last_entries})
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        data={"success": False, "error": e})
