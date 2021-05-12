# Projet Crypto

                                                              Cryptanalyse

[Votre mission, si vous l'acceptez, est de déchiffrer 4 textes de difficulté croissante en vous aidant d'un programme python 
que vous allez écrire.
Les fichiers ont été cryptés avec des méthodes données en cours.
Les fichiers chiffrés contiennent des textes en ASCII. Une fois déchiffrés ils vous donneront des informations.
Vous devez vous baser sur les fréquences d'apparition des lettres en français (et des paires de lettres) pour casser les codes.
Faire une fonction de calcul pour vous aider.
Penser à réutliser le code du td de cryptographie comme base de travail.
Le code de votre programme doit être sur github et vous fournirez un lien vers votre projet github avec le code et le résultat
du décodage en le déposant sur Moodle avant le mercredi 12 mai.
Une soutenance sera organisée le 17 mai.]


   Le texte 1 est chiffré avec le code de César, c'est-à-dire que toutes les lettres du texte sont décalées dans l'alphabet modulo 26 par une même lettre.
Dans notre cas la clé est "b".
Ce qui nous permet de déchiffrer ceci : "le prochain fichier aura un code par substitution alphabétique: chaque lettre est remplacée par 
une autre. utiliser la fréquence des lettres pour décoder le message."
 

   Le texte 2 lui est chiffré par substitution de toutes ses lettres par une autre, et non pas la même pour toutes comme dans le texte 1.
Nous avons alors calculé la fréquence de chaque lettre, puis les avons substituer aux fréquences d'apparition des lettres en français.
(Par exemple, la lettre avec la plus grande fréquence dans un texte en français est e)
Si il y a des incohérences, on remplace par une autre lettre, jusqu'à avoir le texte déchiffré.
En effet, le texte étant très court, les fréquences d'apparition des lettres en français ne sont pas toujours correctes.

Déchiffrement du texte 2 : "le prochain fichier est codé par un mot de passe de taille inconnue et contient l'indice. 
Les lettres du mot de passe permettent de décaler les lettres du message original modulo 26. seules les lettres de a a z sont chiffrées."
 

   Le texte 3 lui est chiffré avec le chiffrement de Vigenère. C'est un système de chiffrement par substitution polyalphabétique; en effet une même lettre du message clair peut, suivant sa position, être remplacée par des lettres différentes, contrairement au système du
code de César.
Nous pouvons supposer que les lettres seules que l'on voit dans le texte qui sont des "c" sont des "a", car dans la langue française il n'y a que cela comme mot avec une seule lettre.
(De même, on suppose que les lettres précédant une apostrophe sont des "l", cela étant aussi la seule possibilité dans la langue française.)
Si cela devient alors cela veut dire que nous sommes passés de 3 dans l'alphabet à 1.
Formule : (3+x)modulo 26 = 1
x = 24
La 24ème lettre de l'alphabet est X.
Pour trouver la taille de la clé, on regarde la distance entre les répétitions, puis on cherche les facteurs pour chaque paire.
entre les 2 c : 20
entre les 2 uqfw : 129
entre les deux wy : 23
On trouve que la taille du mot clé est de 4.
Ainsi on remplace une lettre par la lettre + X)modulo 26 à chaque bloc de 4 lettres.
on obtient alors : 
               
               dceu|q e |n'eh|fp c|g p'|kyhh|ep u|qfw |cgiy| cit|udm |c gz|udiq| ni |ezhd| px |c jh|ptv |ep c|ggsh|t. k|g hd|tymd|t xd|zei |gdx |rzyq| wir| mvz|xpw,| cif|cchd|
               b    o    l    d    e    i    c    o    a         s    a    s         c         a    n    c    e    r.   e    r    r    x    e    p              v         a   
             
               b zn|wd c|cyw |wy l|kcsh|t, d|p is|gd u|qfw |wy ?|
               z    u    a    u    i    r    n    e    o    u       

on continue alors à deviner les mots, par exemple après un c dans un mot de deux lettres, il ne peut qu' y avoir un e pour donner "ce".
p devient alors un e
Formule : (16+x)modulo 26 = 5
x = 15
la 15ème lettre de l'alphabet est O.
On a alors : 
             
             dceu|q e |n'eh|fp c|g p'|kyhh|ep u|qfw |cgiy| cit|udm |c gz|udiq| ni |ezhd| px |c jh|ptv |ep c|ggsh|t. k|g hd|tymd|t xd|zei |gdx |rzyq| wir| mvz|xpw,| cif|cchd|
             br   o    l    de   e    in   c    ou   av        ss   a    ss        co        a    ni   ce   ev   r.   e    rn   r    xt   es   po             ve        ar   
             
             b zn|wd c|cyw |wy l|kcsh|t, d|p is|gd u|qfw |wy ?|
             z    us   an   un   ir   r    n    es   ou   un       
.....

On continue cela jusqu'à déchiffrer tout le texte, et on trouve le mot clé : xova.
Déchiffrement du texte 3 : "bravo à l'aide de l'indice vous avez réussi à casser le code et à finir ce devoir. 
le dernier texte est pour les braves, regardez vous dans un miroir, en êtes vous un?"
 
   Le texte 4 est donc vu comme dans un miroir, c'est-à -dire qu'on l'inverse.
Il est codé de la même manière que le texte 3, on fait donc la même chose que dans le texte 3.
Quand on l'inverse on obtient : "kv qsteiadw qrs gqfmem  zwrno c'rvjmq toirt  cen bizeiw ofimw el Miwjhuz  pvz ysqnvno rbes vdwvr  pdt sdrffj à bvc iy  evvjvdvis hd krjthrlen  kfj vvzjxnzir u'vvffet  et eiy sslfai ev wykmvs  if vjycsrin obj xvdwvr  wzoj neupzr wh ca ptov  nstt sjr grus zji yi uyuii  b ui bpke tnjetp  rj lz rpcedp fjt jqpzd  wh cen pvrtmi trinsmt  nz rpet zqbzmzrs huz pvrtmi  trnn zwfim dtjati  ev ksquvr ymf rjfd  jum kfj bvzous fnvceqeqej"
