

class Activity:

    def __init__(self, **kwargs):
        self.id_testdata = kwargs.get('id_testdata')
        self.activity_name = kwargs.get('activity_name')
        self.activity_url = kwargs.get('activity_url')
        self.activity_status = kwargs.get('activity_status')
        self.branch = kwargs.get('branch')
        self.starting_location = kwargs.get('starting_location')
        self.time_zone = kwargs.get('time_zone')
        self.activity_description = kwargs.get('activity_description')
        self.cancellation_policy = kwargs.get('cancellation_policy')
        self.sales_tax = kwargs.get('sales_tax')
        self.activity_duration_days = kwargs.get('activity_duration_days')
        self.activity_duration_hours = kwargs.get('activity_duration_hours')
        self.activity_duration_minutes = kwargs.get('activity_duration_minutes')
        self.activity_color = kwargs.get('activity_color')
        self.ticket_maximum = kwargs.get('ticket_maximum')
        self.sell_out_alert = kwargs.get('sell_out_alert')
        self.alert_guide_upon_sellout = kwargs.get('alert_guide_upon_sellout')
        self.stop_booking_sold = kwargs.get('stop_booking_sold')
        self.ticket_minimum = kwargs.get('ticket_minimum')
        self.minimum_not_met_alert = kwargs.get('minimum_not_met_alert')
        self.stop_no_sales = kwargs.get('stop_no_sales')
        self.stop_midnight_before = kwargs.get('stop_midnight_before')
        self.first_sale_closes_event = kwargs.get('first_sale_closes_event')
        self.add_ticket_type = kwargs.get('add_ticket_type')
        self.first_ticket_type = kwargs.get('first_ticket_type')
        self.first_ticket_price = kwargs.get('first_ticket_price')
        self.second_ticket_type = kwargs.get('second_ticket_type')
        self.second_ticket_price = kwargs.get('second_ticket_price')
        self.third_ticket_type = kwargs.get('third_ticket_type')
        self.third_ticket_price = kwargs.get('third_ticket_price')
        self.fourth_ticket_type = kwargs.get('fourth_ticket_type')
        self.fourth_ticket_price = kwargs.get('fourth_ticket_price')
        self.first_guide = kwargs.get('first_guide')
        self.first_linked_activity = kwargs.get('first_linked_activity')
        self.what_included = kwargs.get('what_included')
        self.what_know = kwargs.get('what_know')
        self.what_bring = kwargs.get('what_bring')
        self.review_redirect = kwargs.get('review_redirect')
        self.review_website = kwargs.get('review_website')

    def __repr__(self):
        return self.id_testdata