## Scripts for USB XD-USBTIME4-V2 relay

Product to find on Alibaba, under the name "4 channel relay intelligent control module computer controller /pc controller relay module with USB" :

http://www.aliexpress.com/item/4-channel-relay-intelligent-control-module-computer-controller-pc-controller-relay-module-with-USB/1315261952.html

http://item.taobao.com/item.htm?spm=2013.1.20141001.2.jzkBS5&id=12824159130&scm=1007.10115.1443.0&pvid=528a5bcb-4081-4286-963a-14aec070cf2d


### Commands to control the relays

* Enable relay n°1 : `55 01 11 00 00 00 01 68`
* Enable relay n°2 : `55 01 11 00 00 00 02 69`
* Enable relay n°3 : `55 01 11 00 00 00 03 6A`
* Enable relay n°4 : `55 01 11 00 00 00 04 6B`

* Disable relay n°1 : `55 01 12 00 00 00 01 69`
* Disable relay n°2 : `55 01 12 00 00 00 02 6A`
* Disable relay n°3 : `55 01 12 00 00 00 03 6B`
* Disable relay n°4 : `55 01 12 00 00 00 04 6C`

* To enable / disable all relays :
   * `55 01 13 00 00 FF FF 67`
   * `55 01 13 00 00 00 00 69`
