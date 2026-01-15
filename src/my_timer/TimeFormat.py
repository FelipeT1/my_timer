import re

class TimeFormat:
    """ Validates time formats and returns time in seconds. Valid format 00h00m00s """
    _ALLOWED_FORMAT = re.compile(
            r"""
            ^(?=.*\d) # Lookahead so empty strings are invalid
            (?P<h>\d{1,2}h)? # hour
            (?P<m>\d{1,2}m)? # minute
            (?P<s>\d{1,2}s)?$ # seconds
            """
            ,re.I | re.X)

    @staticmethod
    def _validate(time_format: str) -> re.Match:
        """ Validates the format if invalid raises ValueError"""
        pattern = TimeFormat._ALLOWED_FORMAT.fullmatch(time_format)
        if not pattern: 
            raise ValueError(f'invalid format, got {time_format}')
        return pattern
    
    @staticmethod
    def _extract_number(time: str) -> float:
        """ Extracts a number and returns it """
        p = re.compile(r'\d{1,2}')
        return float(p.findall(time)[0])

    @staticmethod
    def parse(time_format: str) -> float:
        """ Parses the time format into seconds """
        s = 0
        m = TimeFormat._validate(time_format)
        for t in m.groupdict():
            if t == 'h' and m[t]:
                s += TimeFormat._extract_number(m[t]) * 3600
            elif t == 'm' and m[t]:
                s += TimeFormat._extract_number(m[t]) * 60
            elif t == 's' and m[t]:
                s += TimeFormat._extract_number(m[t])
        return s
