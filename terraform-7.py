import json

resources = resources_from_greetings(["hello", "hi", "goodbye", "bye"])
for idx, resource in enumerate(resources):
    with open(f"greeting-{idx}.tf.json", "w") as fpout:
        fpout.write(json.dumps(resource))
