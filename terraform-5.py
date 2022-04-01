def content_from_greeting(greeting):
    content = greeting + " ${var.person}"
    if greeting.endswith("bye"):
        content += ", see you later!"
    content += "\n"
    return content
