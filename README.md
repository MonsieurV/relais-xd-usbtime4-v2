## Scripts de test pour le relais USB XD-USBTIME4-V2

Produit à retrouver sur Alibaba, sous le libellé "4 channel relay intelligent control module computer controller /pc controller relay module with USB" :

http://www.aliexpress.com/item/4-channel-relay-intelligent-control-module-computer-controller-pc-controller-relay-module-with-USB/1315261952.html

http://item.taobao.com/item.htm?spm=2013.1.20141001.2.jzkBS5&id=12824159130&scm=1007.10115.1443.0&pvid=528a5bcb-4081-4286-963a-14aec070cf2d


### Les commandes du relais

* Activer le relais n°1 : `55 01 11 00 00 00 01 68`
* Activer le relais n°2 : `55 01 11 00 00 00 02 69`
* Activer le relais n°3 : `55 01 11 00 00 00 03 6A`
* Activer le relais n°4 : `55 01 11 00 00 00 04 6B`

* Désactiver le relais n°1 : `55 01 12 00 00 00 01 69`
* Désactiver le relais n°2 : `55 01 12 00 00 00 02 6A`
* Désactiver le relais n°3 : `55 01 12 00 00 00 03 6B`
* Désactiver le relais n°4 : `55 01 12 00 00 00 04 6C`

* Pour activer / désactiver tous les relais :
   * `55 01 13 00 00 FF FF 67`
   * `55 01 13 00 00 00 00 69`
