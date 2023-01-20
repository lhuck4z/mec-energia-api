from datetime import date

from contracts.models import EnergyBill

class CreateEnergyBillTestUtil:
    energy_bill_dicts = [
        {
            'date': date.today(),
            'invoice_in_reais': 100.00,
            'is_atypical': False,
            'peak_consumption_in_kwh': 100.00,
            'off_peak_consumption_in_kwh': 100.00,
            'peak_measured_demand_in_kw': 100.00,
            'off_peak_measured_demand_in_kw': 100.00,
        },
    ]

    def create_energy_bill(energy_bill_dict, contract, consumer_unit):
        energy_bill = EnergyBill.objects.create(
            date = energy_bill_dict['date'],
            invoice_in_reais = energy_bill_dict['invoice_in_reais'],
            is_atypical = energy_bill_dict['is_atypical'],
            peak_consumption_in_kwh = energy_bill_dict['peak_consumption_in_kwh'],
            off_peak_consumption_in_kwh = energy_bill_dict['off_peak_consumption_in_kwh'],
            peak_measured_demand_in_kw = energy_bill_dict['peak_measured_demand_in_kw'],
            off_peak_measured_demand_in_kw = energy_bill_dict['off_peak_measured_demand_in_kw'],
            contract = contract,
            consumer_unit = consumer_unit
        )

        return energy_bill
    
    def create_energy_bill_by_index(index, contract, consumer_unit):
        energy_bill_dict = CreateEnergyBillTestUtil.get_energy_bill_dict(index)
        energy_bill = CreateEnergyBillTestUtil.create_energy_bill(energy_bill_dict, contract, consumer_unit)

        return energy_bill

    def create_current_energy_bill(contract, consumer_unit):
        energy_bill_dict = CreateEnergyBillTestUtil.get_energy_bill_dict(0)
        energy_bill = CreateEnergyBillTestUtil.create_energy_bill(energy_bill_dict, contract, consumer_unit)

        return energy_bill

    def get_energy_bill_dict(index):
        return CreateEnergyBillTestUtil.energy_bill_dicts[index]
    