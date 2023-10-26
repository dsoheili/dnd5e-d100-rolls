# Import all external variables
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

# Index for all tables
tables = {
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
    "Weapons, Armor and Equipment": weapons_armor_and_equipment_items
}