import treetaggerwrapper
"""
ABR	abbreviation
ADJ	adjective
ADV	adverb
CON	conjunction
DET:def	definite article
DET:indef	indefinite article
FW	foreign word
INT	interjection
LS	list symbol
NOM	noun
NPR	name
NUM	numeral
PON	punctuation
PRE	preposition
PRE:det	preposition+article
PRO	pronoun
PRO:demo	demonstrative pronoun
PRO:indef	indefinite pronoun
PRO:inter	interrogative pronoun
PRO:pers	personal pronoun
PRO:poss	possessive pronoun
PRO:refl	reflexive pronoun
PRO:rela	relative pronoun
SENT	sentence marker
SYM	symbol
VER:cimp	verb conjunctive imperfect
VER:cond	verb conditional
VER:cpre	verb conjunctive present
VER:futu	verb future tense
VER:geru	verb gerund
VER:impe	verb imperative
VER:impf	verb imperfect
VER:infi	verb infinitive
VER:pper	verb participle perfect
VER:ppre	verb participle present
VER:pres	verb present
VER:refl:infi	verb reflexive infinitive
VER:remo	verb simple past
"""
stnc='si tratta di un test'
tagger = treetaggerwrapper.TreeTagger(TAGLANG='it')
tags = tagger.tag_text("si tratta di un test")
tagset=[i.pos for i in treetaggerwrapper.make_tags(tags)]
print(tagset)
tagger = treetaggerwrapper.TreeTagger(TAGLANG='fr')
tags = tagger.tag_text("hey toi là-bas")
tagset=[i.pos for i in treetaggerwrapper.make_tags(tags)]
print(tagset)