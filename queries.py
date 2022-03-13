def select_properties_query(allowed_statuses):
    """
    function to return query based on allowed
    statuses
    """
    query = (
        "SELECT p.address, p.city, p.price, p.description "
        "FROM habi_db.status_history as sh "
        "JOIN habi_db.property as p on p.id = sh.property_id "
        "JOIN habi_db.status as s on s.id = sh.status_id"
        " WHERE s.name "
        f"IN ({allowed_statuses})"
    )
    return query
