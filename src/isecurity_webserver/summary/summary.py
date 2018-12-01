from ..data_model import get_data_model

def get_summary(self, modificator=""):
    data_model = get_data_model()
    if modificator != "" and modificator != None:
        query = {
            "range":{
                "@datetime":{
                    "gte":"now-{}".format(modificator),
                    "lt": "now"
                }
            }
        }
    else:
        query = {}

    total_alerts = data_model._elk.count_results_of_query(query, index="isecurity_datamodel-alerts")
    total_users = data_model._elk.count_results_of_query(query, index="isecurity_datamodel-users")
    total_devices = data_model._elk.count_results_of_query(query, index="isecurity_datamodel-devices")
    total_domains = data_model._elk.count_results_of_query(query, index="isecurity_datamodel-domains")

    result = {
        "num_users": total_users.get('count',0),
        "num_devices": total_devices.get('count',0),
        "num_alerts": total_alerts.get('count',0),
        "num_domains": total_alerts.get('count',0)
    }
    return result
