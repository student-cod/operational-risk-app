def rule_based_risk(task):
    """
    Returns:
    1  -> High risk
    0  -> Low risk
    None -> Let ML decide
    """

    # Business rule:
    # Past delay + High team load = High risk
    if task["past_delay"] == 1 and task["team_load"] == 2:
        return 1

    return None
