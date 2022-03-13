from queries import select_properties_query


def property_filter(allowed_statuses, year, city):
    """basic function to filter properties"""
    year_value = f" and p.year={year} "
    city_value = f" and p.city='{city}' "

    default_query = select_properties_query(
        allowed_statuses=allowed_statuses
    )

    if year and city:
        default_query += (
                year_value
                + city_value
        )
    elif year:
        default_query += year_value
    elif city:
        default_query += city_value
    else:
        return default_query

    return default_query
