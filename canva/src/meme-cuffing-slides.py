T='Cuffing season'
S=[]
S.append(('Alliance','Horde',[
  tip('Hearthstone','w','Bound to: Goldshire','obviously',-3),
  img(C+'02-human-hunter.png',300),
  t('Dances on the mailbox in Stormwind',28,2),
  t('Gnome named Sparklebolt',28,-2),
  img(C+'08-gnome-murlocs.png',230),
  chat('w','Cuddlebunz','hey wanna duel',1),
  t('Roleplays a little too hard',27,0),
  img(C+'09-dwarf-tips.png',240),
  t('Date night at the Lion’s Pride Inn',27,-2),
],[
  t('Still looking for Mankrik’s wife',28,-2),
  img(C+'03-orc-warrior.png',290),
  chat('1','Grukk','anyone know where mankrik wife is',-1),
  t('Fell off the Undercity elevator (twice)',27,2),
  img(C+'05-tauren-mount-price.png',250),
  tip('Kodo Hide Bag','g','Holds 6 items','and every Barrens chat argument',2),
  t('Says lok’tar unironically',27,-1),
  img(C+'07-troll-battleground.png',240),
]))
S.append(('Tanks','Healers',[
  t('Pulls the whole room. Types “np”',28,-2),
  img(C+'03-orc-warrior.png',260,0,True),
  tip('Shield Wall','b','Emotionally unavailable for 10 sec','works on feelings too',2),
  t('Marks skull. Hits something else',27,1),
  img(C+'17-gnome-warrior-acronyms.png',230),
  chat('s','Tankyboi','gogogo',-1),
  t('Never once read chat',27,-2),
  t('“gogogo” is their love language',27,2),
],[
  t('Silently judging your gear',28,2),
  img(K+'priest.png',250),
  chat('s','Moonpriest','mana',-1),
  chat('s','Moonpriest','MANA',1),
  tip('Renew','g','Heals you over time','unlike your ex',-2),
  img(C+'10-druid-raid.png',270),
  t('Let the hunter die. On purpose.',28,1),
  t('Drinks mid-conversation',27,-1),
]))
S.append(('Hunters','Rogues',[
  t('Pet has a better name than you',28,-2),
  img(C+'02-human-hunter.png',270,0,True),
  t('Rolled need on the dagger',28,2),
  tip('Quiver','g','Holds arrows','and grudges',-2),
  img(C+'06-rambleon-pet.png',230),
  t('Feigns Death during arguments',27,1),
  chat('r','Legolasss','sry pet was on aggressive',0),
  t('Asks how the pet is doing before asking how you’re doing',24,-1),
],[
  t('Sapped you at the mailbox',28,2),
  img(K+'rogue.png',290),
  t('Vanishes when you say “we need to talk”',27,-2),
  tip('Thistle Tea','w','Restores 100 energy','does not restore trust',2),
  t('“I’m not a ganker”',28,-1),
  img(C+'07-troll-battleground.png',230,0,True),
  chat('w','Stabbyx','gg',1),
  t('Corpse camps with intent',27,0),
]))
S.append(('Mages','Warlocks',[
  t('Water vendor with benefits',28,-2),
  img(C+'15-orc-mage-travel.png',270),
  tip('Conjured Water','w','Restores mana','free, like their attention',2),
  t('Charges you for a portal on the first date',26,1),
  chat('2','Frostyy','WTS portals 5g',-1),
  img(C+'40-high-order-skyborne-mage.png',250),
  t('Sheeps their problems',27,-2),
  t('Blinks into the next pack',27,2),
],[
  t('Summons you whether you want it or not',27,2),
  img(K+'warlock.png',280),
  chat('g','Shadowdad','click the portal pls',-1),
  tip('Soul Shard','p','Unique (x28)','keeps one from every ex',-2),
  img(K+'mage.png',230),
  t('Healthstone is their love language',27,1),
  t('The imp has seen things',27,-2),
  t('Life Taps when stressed',27,1),
]))
S.append(('Raiders','Casuals',[
  t('Calendar invites as flirting',28,-2),
  img(C+'10-druid-raid.png',250,0,True),
  chat('r','Raidlead','no one is missing raid for a birthday',1),
  t('Asks your DKP before your name',27,2),
  tip('Flask of Commitment','b','Required for raid','you are not',-2),
  img(C+'11-dwarf-shaman-dungeon.png',250),
  t('Lives in Discord voice',27,-1),
  t('Talks only in acronyms',27,1),
],[
  t('Level 23 since launch',28,2),
  img(C+'12-rambleon-bags.png',260),
  t('Fishing as therapy',28,-2),
  tip('Fishing Pole','w','+1 Fishing','+10 inner peace',2),
  t('9 alts, none past 30',27,-1),
  img(C+'05-tauren-mount-price.png',230,0,True),
  t('Spent the whole night sorting bags',26,1),
  chat('1','Cozyhorns','is it bad if i just pick flowers',-1),
]))
S.append(('Paladins','Druids',[
  t('Bubbles and hearths when it gets hard',27,-2),
  img(K+'paladin.png',280),
  tip('Divine Shield','p','Immune to all damage','and all accountability',2),
  t('Specced Ret. Heals anyway',27,1),
  chat('s','Lightbringr','/kneel',-1),
  img(C+'04-undead-paladin.png',240),
  t('Gives you Kings, never Might',27,-2),
  t('Thinks /kneel is a proposal',27,2),
],[
  t('Turns into a cat when things get serious',27,2),
  img(C+'42-skyborne-druid-intro.png',270),
  tip('Innervate','b','Restores your mana','never gives you closure',-2),
  t('Can’t commit to one role',27,-1),
  img(C+'44-night-elf-elf-tree.png',240),
  chat('w','Moonleaf','brb, travel form',1),
  t('Herbalism walks as a date',27,1),
  t('Bear form is their “comfort fit”',26,-2),
]))
out=['<!doctype html><meta charset="utf-8"><title>meme: cuffing season</title><style>'+CSS+'</style>']
for i,(a,b,L,R) in enumerate(S): out.append(slide(i+1,7,T,L,R,a,b))
def at(x,y,html_): return f'<div style="position:absolute;left:{x}px;top:{y}px">{html_}</div>'
pieces=[
 at(330,250,f'<img class="cut" src="{C}16-rambleon-cheer.png" style="height:1000px">'),
 at(40,300,render(t('Married to the Auction House',34,-3))),
 at(730,290,render(tip('Ring of Commitment','o','Unique. Soulbound.','not equipped',4))),
 at(40,530,render(t('“one more dungeon” at 1am',34,2))),
 at(770,560,render(t('Hearthed out of the conversation',32,-2))),
 at(40,760,render(chat('w','Someone','hey are u up',-2))),
 at(40,870,render(tip('Hearthstone','w','Bound to: my own company','cooldown: 0',-3))),
 at(760,800,render(t('Only long-term relationship is my mount',32,2))),
 at(760,1040,render(t('/sit in Ironforge waiting to be inspected',30,-1))),
 at(40,1140,render(t('Left on read since 2019',32,1))),
]
out.append(f'<section class="me"><h1>{T}</h1><div class="pill">7/7</div><h2 style="position:absolute;top:168px;left:0;right:0;text-align:center;margin:0;font:900 72px Inter">me</h2>{"".join(pieces)}<div class="handle">@wowforeverguide</div></section>')
open('/home/user/wowforeverguide/canva/meme-cuffing-season.html','w').write('\\n'.join(out))
