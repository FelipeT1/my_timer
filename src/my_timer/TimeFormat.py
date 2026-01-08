import re

class TimeFormat:
    """ Validates time formats. Valid format 00h00m00s """
    _ALLOWED_FORMAT = re.compile(
            r"""
            (\d{1,2}h)? # hour
            (\d{1,2}m)? # minute
            (\d{1,2}s)? # seconds
            """
            ,re.I | re.X)

    @staticmethod
    def validate(time_format: str) -> None:
        """ Validates the format if invalid raises ValueError"""
        pattern = TimeFormat._ALLOWED_FORMAT.fullmatch(time_format)
        if not pattern: 
            raise ValueError(f'invalid format, got {time_format}')
