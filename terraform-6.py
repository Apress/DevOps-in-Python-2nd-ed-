def resources_from_greetings(all_greetings):
    for idx, greeting in enumerate(all_greetings):
        content = content_from_greeting(greeting)
        resource = resource_from_content_idx(content, idx)
        yield resource
