Setup:
$pip install requests


Input:
api=RiotAPI(API_KEY)
champion_list = api.get_champion_list()
Spell(api,'Tryndamere','q').print_spell()

Sample Output:
Bloodlust
Tryndamere thrives on the thrills of combat, increasing his Attack Damage as he is more and more wounded. He can cast Bloodlust to consume his Fury and heal himself.
Range: self
Cooldown: [12.0, 12.0, 12.0, 12.0, 12.0]