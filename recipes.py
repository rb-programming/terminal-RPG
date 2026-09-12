class Recipe:
    def __init__(self, recipes = {"Arrow":{"Bone": 1, "Feather": 1, "Sharp Stone": 1},
                                  "Pillow":{"Feather":10},
                                  "Fertilizer":{"Bone": 1},
                                  }):
        self.recipes = recipes