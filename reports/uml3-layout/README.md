# UML3 layout repair

The previous row-major grid separated parent and child classes across
unrelated rows, producing long relations through the model. Its saved
zoom level was 1 (10%).

The corrected UMLet diagram groups resources and summoning above the
inheritance tree. WarriorUndead and CursedUndead share the same level;
DeathKnight sits between them below, showing both inheritance branches.
PutridZombie remains directly connected to Undead. Orthogonal relation
routes avoid unrelated class interiors.

- 12 classes and all existing class-member text preserved.
- 14 relationships retained, including both DeathKnight parent edges.
- No overlapping class rectangles.
- No relation segment crosses an unrelated class rectangle.
- Saved zoom level: 6 (60%).
- Project2/current.uxf matches Project2/UML3.uxf.

UML3-before.uxf is the original backup. UML3-preview.png is the detailed
preview; UML3-overview.png is the reduced overview. Both previews use the
same class geometry and relation points as the saved XML. They are layout
previews, not screenshots of UMLet; its font metrics and label placement
may differ slightly.
