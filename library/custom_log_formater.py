import logging


class CustomFormatter(logging.Formatter):
    # This will add stack trace in the message if raised
    # - To add stack trace in logs, use logger.exception("Custom message"), it will add the stacktrace in current frame to the logs.
    def format(self, record):
        if record.exc_info:
            record.msg = str(record.msg + "  " + repr(super(CustomFormatter, self).formatException(record.exc_info))).replace('"', '\\"')
            record.exc_info = None
        result = super(CustomFormatter, self).format(record)
        return result
