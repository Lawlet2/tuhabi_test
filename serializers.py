

def property_serializer(executed_query):
    obj_list = []

    for (address, city, price, description) in executed_query:
        obj_list.append(
            {
                "address": address,
                "city": city,
                "price": price,
                "description": description
            }
        )
    return obj_list
