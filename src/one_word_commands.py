def describe_scene(scene_name):
    print(scenes[scene_name]["decription"])


one_word_commands = {
    "look": {
        "func": describe_scene
    }
}
