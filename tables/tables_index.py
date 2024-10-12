# Locations
from .locations.wizards_chamber import wizard_chamber_items
from .locations.alchemists_lab import alchemists_lab_items
from .locations.cottage import cottage_items
from .locations.bandit_hideout import bandit_hideout_items
from .locations.office import office_items
from .locations.warehouse import warehouse_items
from .locations.royal_tomb import royal_tomb_items
from .locations.nobles_bedchamber import nobles_bechamber_items
from .locations.port_masters_office import port_masters_office_items
from .locations.hunters_camp import hunters_camp_items
from .locations.ship_captains_quarters import ship_captains_quarters_items
from .locations.fantasy_desk import fantasy_desk_items
from .locations.inns_kitchen import inns_kitchen_items

# Items
from .items.adventurers_dead_body import adventurers_dead_body_items
from .items.dead_goblin import dead_goblin_items
from .items.weapons_armor_and_equipment import weapons_armor_and_equipment_items
from .items.gemstones_1 import gemstones_1_list
from .items.gemstones_2 import gemstones_2_list
from .items.gemstones_3 import gemstones_3_list
from .items.trinkets_phb import trinkets_phb_items
from .items.food import food_list

# Effects
from .effects.minor_curses import minor_curses_list
from .effects.major_curses import major_curses_list
from .effects.deadly_curses import deadly_curses_list
from .effects.fatal_curses import fatal_curses_list
from .effects.blessings import blessings_list
from .effects.remarkable_blessings import remarkable_blessings_list
from .effects.wild_magic_surge import wild_magic_surge_list
from .effects.wild_magic_pact import wild_magic_pact_list

# Experiences
from .experiences.nightmares import nightmares_list

# Names
from .names.book_titles import book_titles_list
from .names.male_names_1 import male_names_1_list
from .names.male_names_2 import male_names_2_list
from .names.male_names_3 import male_names_3_list

# Crafting items
from .crafting.potion_ingredients import potion_ingredients_list
from .crafting.medicinal_herbs import medicinal_herbs_list
from .crafting.culinary_herbs_and_spices import culinary_herbs_and_spices_list

# Encounters
from .encounters.forest import forest_encounters_list
from .encounters.mountain import mountain_encounters_list
from .encounters.swamp import swamp_encounters_list
from .encounters.seafaring import seafaring_encounters_list

# Events
from .events.catastrophes import catastrophes_list

# Quests
from .quests.rumors_and_odd_jobs import rumors_and_odd_jobs_list

item_tables = {
    "Adventurer's Dead Body": adventurers_dead_body_items,
    "Dead Goblin": dead_goblin_items,
    "Weapons, Armor and Equipment": weapons_armor_and_equipment_items,
    "Gemstones (10 gp)": gemstones_1_list,
    "Gemstones (50 gp)": gemstones_2_list,
    "Gemstones (100 gp)": gemstones_3_list,
    "Trinkets (PHB)": trinkets_phb_items,
    "Food": food_list,
}

location_tables = {
    "Wizard's Chamber": wizard_chamber_items,
    "Alchemist's Lab": alchemists_lab_items,
    "Cottage": cottage_items,
    "Bandit Hideout": bandit_hideout_items,
    "Office": office_items,
    "Warehouse": warehouse_items,
    "Royal Tomb": royal_tomb_items,
    "Noble's Bedchamber": nobles_bechamber_items,
    "Port Master's Office": port_masters_office_items,
    "Hunter's Camp": hunters_camp_items,
    "Ship Captain's Quarters": ship_captains_quarters_items,
    "Fantasy Desk": fantasy_desk_items,
    "Inn's Kitchen": inns_kitchen_items,
}

effects_tables = {
    "Curses, Minor": minor_curses_list,
    "Curses, Major": major_curses_list,
    "Curses, Deadly": deadly_curses_list,
    "Curses, Fatal": fatal_curses_list,
    "Blessings": blessings_list,
    "Blessings, Remarkable": remarkable_blessings_list,
    "Wild Magic Surge": wild_magic_surge_list,
    "Wild Magic Pact (Barbarian)": wild_magic_pact_list,
}

experiences_tables = {
    "Nightmares": nightmares_list
}

encounter_tables = {
    "Forest Encounters": forest_encounters_list,
    "Mountain Encounters": mountain_encounters_list,
    "Swamp Encounters": swamp_encounters_list,
    "Seafaring Encounters": seafaring_encounters_list
}

name_tables = {
    "Book Titles": book_titles_list,
    "Male Names #1": male_names_1_list,
    "Male Names #2": male_names_2_list,
    "Male Names #3": male_names_3_list,
}

crafting_tables = {
    "Potion Ingredients": potion_ingredients_list,
    "Medicinal Herbs": medicinal_herbs_list,
    "Culinary Herbs & Spices": culinary_herbs_and_spices_list
}

events_tables = {
    "Catastrophes": catastrophes_list,
}

quests_tables = {
    "Rumors & Odd Jobs": rumors_and_odd_jobs_list,
}

# Index for all tables
tables = item_tables | effects_tables | experiences_tables | encounter_tables | name_tables | crafting_tables | location_tables | events_tables | quests_tables
