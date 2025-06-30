def get_submission_url(candidate):
    """
    Simulate an API call that returns a unique form URL for a candidate.
    This mock just converts their name into a slug and appends it to a fake domain.
    """
    name_slug = candidate["name"].lower().replace(" ", "-")
    return f"file:///E:/dummy_form.html"
