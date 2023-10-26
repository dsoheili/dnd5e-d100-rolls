# Items
from .items.wizards_chamber import wizard_chamber_items
from .items.alchemists_lab import alchemists_lab_items
from .items.cottage import cottage_items
from .items.bandit_hideout import bandit_hideout_items
from .items.office import office_items
from .items.warehouse import warehouse_items
from .items.royal_tomb import royal_tomb_items
from .items.nobles_bedchamber import nobles_bechamber_items
from .items.port_masters_office import port_masters_office_items
from .items.adventurers_dead_body import adventurers_dead_body_items
from .items.hunters_camp import hunters_camp_items
from .items.ship_captains_quarters import ship_captains_quarters_items
from .items.dead_goblin import dead_goblin_items
from .items.fantasy_desk import fantasy_desk_items
from .items.inns_kitchen import inns_kitchen_items
from .items.weapons_armor_and_equipment import weapons_armor_and_equipment_items

# Effects
from .effects.minor_curses import minor_curses_list
from .effects.major_curses import major_curses_list
from .effects.deadly_curses import deadly_curses_list
from .effects.fatal_curses import fatal_curses_list
from .effects.blessings import blessings_list
from .effects.remarkable_blessings import remarkable_blessings_list

# Experiences
from .experiences.nightmares import nightmares_list

item_tables = {
    "Wizard's Chamber": wizard_chamber_items,
    "Alchemist's Lab": alchemists_lab_items,
    "Cottage": cottage_items,
    "Bandit Hideout": bandit_hideout_items,
    "Office": office_items,
    "Warehouse": warehouse_items,
    "Royal Tomb": royal_tomb_items,
    "Noble's Bedchamber": nobles_bechamber_items,
    "Port Master's Office": port_masters_office_items,
    "Adventurer's Dead Body": adventurers_dead_body_items,
    "Hunter's Camp": hunters_camp_items,
    "Ship Captain's Quarters": ship_captains_quarters_items,
    "Dead Goblin": dead_goblin_items,
    "Fantasy Desk": fantasy_desk_items,
    "Inn's Kitchen": inns_kitchen_items,
    "Weapons, Armor and Equipment": weapons_armor_and_equipment_items,
}

effects_tables = {
    "Curses, Minor": minor_curses_list,
    "Curses, Major": major_curses_list,
    "Curses, Deadly": deadly_curses_list,
    "Curses, Fatal": fatal_curses_list,
    "Blessings": blessings_list,
    "Blessings, Remarkable": remarkable_blessings_list,
}

experiences_tables = {
    "Nightmares": nightmares_list
}

encounter_tables = {}

name_tables = {}


# Index for all tables
tables = item_tables | effects_tables | experiences_tables | encounter_tables | name_tables
