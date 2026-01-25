# The Last Haven: Idle Refuge
- Still need's a name
- More heavy notes/learning material is put into a Notion dock with explanation's of how things work

# Overview
This is an idle game inspired by Melvor Idle, it is my first main project. Coded with python through Pygame. There are 3 active skills. Foraging, Hunting, and Scavenging which the player needs to actively sink their time into. They can only do one of these at a time. Then 6 passive skills. Cooking, Engineering, Legacy, Medicine, Fortification, Community. These are skills the player spends reasources in, waits an amount of time, and then get a reward out of.

# Features
-Menu Select
-Customizable Button's
-Temp Inventory
-Scavenging resource gathering
-Hunting reasource gathering
-Foraging reasource gathering
-Fortification background change
-Engineering to reduce starting time of scavenging, foraging, and hunting

# Project Structure
The Project is organized into these main folders
    -Entities
        Button
        Foraging
        Fortification
        GameState
        Hunting
        Player
        Scavenging
    -Menus
        -Core
           DefaultMenu
           InventoryMenu
           ShopMenu 
        -Skills
            CommunityMenu
            CookingMenu
            EngineeringMenu
            ForagingMenu
            FortificationMenu
            HuntingMenu
            LegacyMenu
            MedicineMenu
            ScavengingMenu
        -Services
           Mutator
           SaveFunction 
    .gitnore
    Main
    README