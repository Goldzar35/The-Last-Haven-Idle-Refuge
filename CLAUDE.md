# The Last Haven: Idle Refuge — CLAUDE.md

## Project Overview
Python idle/incremental game built with Pygame (inspired by Melvor Idle). First major project.
- **Language**: Python 3.13
- **Engine**: Pygame
- **Current Version**: ~4.6

## File Structure
```
Main.py                          # Entry point, game loop, sidebar nav, event routing
Entities/
  Button.py                      # Generic UI button (x, y, w, h, text, action_id)
  GameState.py                   # Central state manager; enforces mutually exclusive skills
  Player.py                      # Player data, inventory (30 item types), tick rates, upgrade counts
  Scavenging.py                  # Active skill entity
  Foraging.py                    # Active skill entity
  Hunting.py                     # Active skill entity
  Fortification.py               # Base defense level tracker (6 levels, visual only)
Menus/
  Core/
    DefaultMenu.py               # Main landing page (clickable box with "Coming Soon" label)
    InventoryMenu.py             # Read-only inventory display
    ShopMenu.py                  # Tick speed upgrades for all 3 active skills (4 boxes)
  Skills/
    ScavengingMenu.py            # Start/stop + pending state UI
    ForagingMenu.py              # Start/stop + pending state UI
    HuntingMenu.py               # Start/stop + pending state UI
    EngineeringMenu.py           # Reduces start delays (3 subsystems, scaling costs)
    FortificationMenu.py         # Background progression UI (6 levels, scaling costs, MAXED state)
    MedicineMenu.py              # Placeholder (coming soon)
    CookingMenu.py               # Placeholder (coming soon)
    CommunityMenu.py             # Placeholder (coming soon)
    LegacyMenu.py                # Placeholder (coming soon)
Services/
  Mutator.py                     # Empty (planned)
  SaveFunction.py                # Empty (planned)
Assets/
  Base_lvl_1.png … Base_lvl_6.png  # Fortification backgrounds
```

## Core Architecture

### Game State Flow
1. `Player` holds all persistent data (inventory, tick rates, upgrade counts)
2. `GameState` wraps the three active skill objects and enforces mutual exclusivity
3. Menus render UI and route events; they do NOT hold game data
4. `Main.py` owns the game loop, sidebar, and dispatches events to the active menu

### Active Skills Pattern (Scavenging / Foraging / Hunting)
All three follow identical structure:
- Tick rate stored on `Player` (`scavenge_tick`, `forage_tick`, `hunting_tick`), default 2.0s
- Timing via `time.time()` for loot generation
- Pending start state with delay (default 3000ms), tracked with `pygame.time.get_ticks()`
- Probability-based loot tables (each item has a 1-100 chance value)
- Start/stop controlled through `GameState` (starting one stops others)
- Upgrade count tracked on `Player` (`scavenge_upgrade_count`, `forage_upgrade_count`, `hunting_upgrade_count`)

### Event Routing (Main.py)
- Uses `hasattr(current_menu, 'handle_X_event')` to dispatch events
- Each menu declares handler methods it supports
- Menu-specific `update()` called each frame for pending state logic

### Shop/Upgrade Pattern
- Affordability check before purchase using `can_afford(cost_dict)`
- Deduct resources via `player.remove_inventory_bulk()`
- Reduce tick rate on `Player`; minimum cap 0.1s
- Scaling costs: `cost = 1 + upgrade_count` (all three skills implemented)
- Button text updates after each purchase to show new cost; shows MAXED when capped

### Engineering Pattern
- Reduces start delay per skill; minimum cap 500ms
- Scaling costs derived from current delay: `cost = 1 + (3000 - delay) // 500`
- Resources: Cement (Scavenging), Seeds (Foraging), Bones (Hunting)
- Boxes dim visually and text changes to MAXED when fully upgraded

### Sidebar
- 1600×900 window, 320px sidebar (20%), 1280px main area
- 12 nav buttons (indices 0–11), scrollable with mouse wheel
- Button action IDs map directly to menu index

## Key Items / Resources
**Urban loot (Scavenging)**: Gasoline, People, Canned Food, Electronics, Spare Parts, Nails, Metal Scrap, Rope, Fabric Scrap, Cement, Wood Planks
**Nature loot (Foraging)**: Mirabelle Fruit, Magic Artifact, Medical Herbs, Honey Comb, Fresh Water, Berries, Seeds, Wild Vegetables, Fish, Dirty Water
**Animal loot (Hunting)**: Intact Infected Organ, Boar Tusk, Blood Sample, Eggs, Zombie Flesh, Animal Fat, Hide, Bones, Meat

## Known Bugs / Tech Debt
- **ShopMenu box 4**: Not yet implemented (placeholder "Coming Soon")

## Conventions
- Class names: `[Feature]Menu` for menus, skill/entity names for Entities
- Handler methods: `handle_[action]_event`
- Box/rect vars: `[action]_box`
- Button text helper methods prefixed with `_` (e.g. `_scavenge_button_text()`)
- Fonts created once in `__init__`, never inside `draw()`
- Specific imports only — no wildcard `import *`
- Docstrings on all classes and methods
- No save/load yet — game state resets on restart

## Development Status
**Working**: Scavenging, Foraging, Hunting (active skills), Shop (all 3 tick upgrades with scaling costs), Engineering (delay upgrades with scaling costs + visual MAXED state), Fortification (6 levels, scaling costs, MAXED state), Inventory display, DefaultMenu ("Coming Soon" label)
**Placeholder**: Medicine, Cooking, Community, Legacy menus; save/load system; Shop box 4
