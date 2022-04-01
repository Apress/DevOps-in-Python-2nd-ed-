>>> today = datetime.datetime.now()
>>> yesterday = today - one_day
>>> builder = builder.not_valid_before(yesterday)
