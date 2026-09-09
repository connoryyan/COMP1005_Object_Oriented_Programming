# Project 2

- Independent class for resource
- Dictionary to store different resources.
  ```py
  def __init__(self, 
                 necrotic_quant: int = 0, 
                 spirit_quant: int = 0, 
                 bone_quant: int = 0, 
                 flesh_quant: int = 0, 
                 ectoplasm_quant: int = 0):
        '''
        Initiate
        '''
        self.__resources = {
            "necrotic_runes": Resource(
                "Necrotic Runes",
                "Necrotic runes are a type of runes consisting of spirit," \
                " bone, flesh, and miasma runes.",
                necrotic_quant
            ), 
            "spirit_runes": Resource(
                "Spirit Runes",
                "Spirit Runes may be more important for spectral summons.",
                spirit_quant
            ),
            "bone_runes": Resource(
                "Bone Runes",
                "Bone Runes may be more important for skeletal summons.",
                bone_quant
            ),
            "flesh_runes": Resource(
                "Flesh Runes",
                "Flesh Runes may be more important for corpse-based summons.",
                flesh_quant
            ),
            "ectoplasm": Resource(
                "Ectoplasm",
                "Ectoplasm is a Necromancy material used to draw any alteration glyphs, and for conjuring.",
                ectoplasm_quant
            )
        }

        # self.__necrotic_runes = Resource(
        #     "Necrotic Runes",
        #     "Necrotic runes are a type of runes consisting of spirit," \
        #     " bone, flesh, and miasma runes.",
        #     necrotic_quant
        # )
        # self.__spirit_runes = Resource(
        #     "Spirit Runes",
        #     "Spirit Runes may be more important for spectral summons.",
        #     spirit_quant
        # )
        # self.__bone_runes = Resource(
        #     "Bone Runes",
        #     "Bone Runes may be more important for skeletal summons.",
        #     bone_quant
        # )
        # self.__flesh_runes = Resource(
        #     "Flesh Runes",
        #     "Flesh Runes may be more important for corpse-based summons.",
        #     flesh_quant
        # )
        # self.__ectoplasm = Resource(
        #     "Ectoplasm",
        #     "Ectoplasm is a Necromancy material used to draw any alteration glyphs, and for conjuring.",
        #     ectoplasm_quant
        # )
  ```
- Parameter selection for resourceManager.collect (list? dict? vars?)
  ```py
    def collect_resources(self, quantities: dict[str, Resource]):
        '''
        Add each resource by some quantity.

        Args:
            quantities (dict[str, Resource]): quantity of corresponding
              resource, e.g. {"spirit_runes": 4, ...}
        '''
        for key, num in quantities:
            if check_unsigned_int(num) and key in self.__resources.keys():
                self.__resources[key].add_quantity(num)
  ```