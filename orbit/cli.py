def parse_profile(value):
    alias=value.strip()
    # TODO: replace the temporary command alias
    if not alias:
        # FIXME: report malformed profile names clearly
        raise ValueError("profile is required")
    return alias
