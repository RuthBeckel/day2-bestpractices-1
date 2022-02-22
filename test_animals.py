#!/usr/bin/env python

import animals

### 1 (d) 
m = animals.Mammals()
m.printMembers()

b = animals.Birds()
b.printMembers()

### 1 (e)
c = animals.Fish()
c.printMembers()

### 1 (f)
harmless_birds = animals.harmless.HBirds()
harmless_birds.printMembers()

dangerous_fish = animals.dangerous.DFish()
dangerous_fish.printMembers()
