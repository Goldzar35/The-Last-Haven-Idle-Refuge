# The Last Haven: Idle Refuge

An idle/incremental game inspired by Melvor Idle. Built with Python and Pygame. First major project.

## Overview

The player manages a survival camp in a post-apocalyptic world. There are 3 active skills — Scavenging, Foraging, and Hunting — which gather resources over time. Only one can run at a time. Passive skills like Engineering, Fortification, Cooking, Medicine, Community, and Legacy let the player spend resources to upgrade and improve the camp.

## Features

- Sidebar navigation with 12 menu pages
- Scavenging, Foraging, and Hunting — active resource gathering with pending start delays
- Shop — purchase tick speed upgrades for all 3 active skills (scaling costs)
- Engineering — reduce start delays for all 3 active skills (scaling costs, visual MAXED state)
- Fortification — visual base progression across 6 levels
- Inventory — live display of all 30 resource types

## Project Structure

```
Main.py
Entities/
    Button.py
    Foraging.py
    Fortification.py
    GameState.py
    Hunting.py
    Player.py
    Scavenging.py
Menus/
    Core/
        DefaultMenu.py
        InventoryMenu.py
        ShopMenu.py
    Skills/
        CommunityMenu.py
        CookingMenu.py
        EngineeringMenu.py
        ForagingMenu.py
        FortificationMenu.py
        HuntingMenu.py
        LegacyMenu.py
        MedicineMenu.py
        ScavengingMenu.py
Services/
    Mutator.py
    SaveFunction.py
Assets/
    Base_lvl_1.png … Base_lvl_6.png
```

## Coming Soon

- Medicine, Cooking, Community, Legacy skill menus
- Save / load system
- Shop box 4
