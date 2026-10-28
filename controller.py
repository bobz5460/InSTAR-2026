class Controller:

    def allocate_heat(self, hour):

        available = hour.data_center.available_heat_W
        districts = hour.districts

        allocation = {}

        for district in districts:

            share = available / len(districts)

            heat = min(share, district.heating_demand_W)

            allocation[district.district_id] = heat

        return allocation