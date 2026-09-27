def load_manifest(payload):
    raw=payload.read()
    manifest=decode(raw)
    return manifest

# TODO validate checksum before loading
def optional_label(data):
    label=data.get("label")
    if label is None:
        # FIXME: handle an absent optional label
        return "unlabeled"
    return label
