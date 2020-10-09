############
# Part 1   #
############

class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, name, is_seedless = 'True', is_bestseller = 'True'):
        """Initialize a melon."""
        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.name = name
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing) 

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code
        print(f"this is the new code {new_code})")

def make_melon_types():
    """Returns a list of current melon types."""
    all_melon_types = []

    musk = MelonType('musk', '1998', 'green', 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', '2003', 'orange', 'Casaba', False, False)
    cas.add_pairing('strawberies')
    cas.add_pairing('mint')
    all_melon_types.append(cas)

    cren = MelonType('cren', '1996', 'green', 'Crenshaw', False, False)
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', '2013', 'yellow', 'Yellow Watermelon', False, True)
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)
    
    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")
        print() 

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_id = {}

    for melon in melon_types:
        if melon.code not in melon_id:
            melon_id[melon.code] = melon
    
    return melon_id


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, type, shape_rating, color_rating, harvested_from, harvested_by):
        self.type = melon_type
        self.shape_rating = int(shape_rating)
        self.color_rating = int(color_rating)
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by

    def is_sellable(self):
        if (shape_rating > 5 and color_rating > 5) and harvested_from != "field 3":
            return True 

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_id = make_melon_type_lookup(melon_types)
    melons = []

    melon_1 = Melon(melon_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melon_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melon_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melon_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melon_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melon_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melon_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melon_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melon_id['yw'], 7, 10, 3, 'Sheila')

    melons.extend(melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        harvested_by = f'Harvested by {melon.harvested_by}'
        harvested_from = f'from Field {melon.harvested_from}'
        status = ('CAN BE SOLD') if melon.is_sellable() else ('NOT SELLABLE')
        print(f'{harvested_by} {harvested_from} {status}')
            





