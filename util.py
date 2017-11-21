from datetime import timedelta


def date_to_display(current_dt):
    MONDAY = 0
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6
    day_index = current_dt.weekday()  # Monday = 0, Sunday = 6
    hour = current_dt.hour

    # Test for after 11am on Friday, all weekend, and Monday before 11am
    if day_index in [FRIDAY, SATURDAY, SUNDAY, MONDAY]:
        if FRIDAY == day_index and hour > 10:
            # Add three days to get Monday
            return current_dt + timedelta(3)
        if SATURDAY == day_index:
            # add two days to get Monday
            return current_dt + timedelta(2)
        if SUNDAY == day_index:
            # add one day to get Monday
            return current_dt + timedelta(1)
        if MONDAY == day_index and hour <= 10:
            return current_dt

    # At this point, we can simply test for before 11am
    if hour <= 10:
        # and return the current day if it's before 11am
        return current_dt

    # It is after 11am on a weekday, return the next day
    return current_dt + timedelta(1)
