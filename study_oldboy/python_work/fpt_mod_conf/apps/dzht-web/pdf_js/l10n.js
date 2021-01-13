"use strict";document.webL10n=function(a,b){function k(){return b.querySelectorAll('link[type="application/l10n"]')}function l(){var a=b.querySelector('script[type="application/l10n"]');return a?JSON.parse(a.innerHTML):null}function m(a){return a?a.querySelectorAll("*[data-l10n-id]"):[]}function n(a){var b,c,d;if(!a)return{};if(b=a.getAttribute("data-l10n-id"),c=a.getAttribute("data-l10n-args"),d={},c)try{d=JSON.parse(c)}catch(e){console.warn("could not parse arguments for #"+b)}return{id:b,args:d}}function o(a){var c=b.createEvent("Event");c.initEvent("localized",!0,!1),c.language=a,b.dispatchEvent(c)}function p(a,b,c,d){b=b||function(){},c=c||function(){console.warn(a+" not found.")};var e=new XMLHttpRequest;e.open("GET",a,d),e.overrideMimeType&&e.overrideMimeType("text/plain; charset=utf-8"),e.onreadystatechange=function(){4==e.readyState&&(200==e.status||0===e.status?b(e.responseText):c())},e.onerror=c,e.ontimeout=c;try{e.send(null)}catch(f){c()}}function q(a,b,c,g){function i(a){return a.lastIndexOf("\\")<0?a:a.replace(/\\\\/g,"\\").replace(/\\n/g,"\n").replace(/\\r/g,"\r").replace(/\\t/g,"	").replace(/\\b/g,"\b").replace(/\\f/g,"\f").replace(/\\{/g,"{").replace(/\\}/g,"}").replace(/\\"/g,'"').replace(/\\'/g,"'")}function k(a){function k(a,k){var r,s,t,m=a.replace(d,"").split(/[\r\n]+/),n="*",o=b.replace(/-[a-z]+$/i,""),p=!1,q="";for(r=0;r<m.length;r++)if(s=m[r],!e.test(s)){if(k){if(f.test(s)){q=f.exec(s),n=q[1],p="*"!==n&&n!==b&&n!==o;continue}if(p)continue;g.test(s)&&(q=g.exec(s),l(h+q[1]))}t=s.match(j),t&&3==t.length&&(c[t[1]]=i(t[2]))}}function l(a){p(a,function(a){k(a,!1)},null,!1)}var c=[],d=/^\s*|\s*$/,e=/^\s*#|^\s*$/,f=/^\s*\[(.*)\]\s*$/,g=/^\s*@import\s+url\((.*)\)\s*$/i,j=/^([^=\s]*)\s*=\s*(.+)$/;return k(a,!0),c}var h=a.replace(/[^\/]*$/,"")||"./";p(a,function(a){var b,g,h,i,j;e+=a,b=k(a);for(g in b)j=g.lastIndexOf("."),j>0?(h=g.substring(0,j),i=g.substr(j+1)):(h=g,i=f),d[h]||(d[h]={}),d[h][i]=b[g];c&&c()},g,j)}function r(a,b){function m(a){var b=a.href;a.type,this.load=function(a,c){var d=a;return q(b,a,c,function(){console.warn(b+" not found."),d=""}),d}}var c,e,f,h,j,n,p,r;if(b=b||function(){},s(),g=a,c=k(),e=c.length,0===e)return f=l(),f&&f.locales&&f.default_locale?(console.log("using the embedded JSON directory, early way out"),d=f.locales[a]||f.locales[f.default_locale],b()):console.log("no resource to load, early way out"),o(a),i="complete",void 0;for(h=null,j=0,h=function(){j++,j>=e&&(b(),o(a),i="complete")},n=0;e>n;n++)p=new m(c[n]),r=p.load(a,h),r!=a&&(console.warn('"'+a+'" resource not found'),g="")}function s(){d={},e="",g=""}function t(a){function c(a,b){return-1!==b.indexOf(a)}function d(a,b,c){return a>=b&&c>=a}var b={af:3,ak:4,am:4,ar:1,asa:3,az:0,be:11,bem:3,bez:3,bg:3,bh:4,bm:0,bn:3,bo:0,br:20,brx:3,bs:11,ca:3,cgg:3,chr:3,cs:12,cy:17,da:3,de:3,dv:3,dz:0,ee:3,el:3,en:3,eo:3,es:3,et:3,eu:3,fa:0,ff:5,fi:3,fil:4,fo:3,fr:5,fur:3,fy:3,ga:8,gd:24,gl:3,gsw:3,gu:3,guw:4,gv:23,ha:3,haw:3,he:2,hi:4,hr:11,hu:0,id:0,ig:0,ii:0,is:3,it:3,iu:7,ja:0,jmc:3,jv:0,ka:0,kab:5,kaj:3,kcg:3,kde:0,kea:0,kk:3,kl:3,km:0,kn:0,ko:0,ksb:3,ksh:21,ku:3,kw:7,lag:18,lb:3,lg:3,ln:4,lo:0,lt:10,lv:6,mas:3,mg:4,mk:16,ml:3,mn:3,mo:9,mr:3,ms:0,mt:15,my:0,nah:3,naq:7,nb:3,nd:3,ne:3,nl:3,nn:3,no:3,nr:3,nso:4,ny:3,nyn:3,om:3,or:3,pa:3,pap:3,pl:13,ps:3,pt:3,rm:3,ro:9,rof:3,ru:11,rwk:3,sah:0,saq:3,se:7,seh:3,ses:0,sg:0,sh:11,shi:19,sk:12,sl:14,sma:7,smi:7,smj:7,smn:7,sms:7,sn:3,so:3,sq:3,sr:11,ss:3,ssy:3,st:3,sv:3,sw:3,syr:3,ta:3,te:3,teo:3,th:0,ti:4,tig:3,tk:3,tl:4,tn:3,to:0,tr:0,ts:3,tzm:22,uk:11,ur:3,ve:3,vi:0,vun:3,wa:4,wae:3,wo:0,xh:3,xog:3,yo:0,zh:0,zu:3},e={0:function(){return"other"},1:function(a){return d(a%100,3,10)?"few":0===a?"zero":d(a%100,11,99)?"many":2==a?"two":1==a?"one":"other"},2:function(a){return 0!==a&&0===a%10?"many":2==a?"two":1==a?"one":"other"},3:function(a){return 1==a?"one":"other"},4:function(a){return d(a,0,1)?"one":"other"},5:function(a){return d(a,0,2)&&2!=a?"one":"other"},6:function(a){return 0===a?"zero":1==a%10&&11!=a%100?"one":"other"},7:function(a){return 2==a?"two":1==a?"one":"other"},8:function(a){return d(a,3,6)?"few":d(a,7,10)?"many":2==a?"two":1==a?"one":"other"},9:function(a){return 0===a||1!=a&&d(a%100,1,19)?"few":1==a?"one":"other"},10:function(a){return d(a%10,2,9)&&!d(a%100,11,19)?"few":1!=a%10||d(a%100,11,19)?"other":"one"},11:function(a){return d(a%10,2,4)&&!d(a%100,12,14)?"few":0===a%10||d(a%10,5,9)||d(a%100,11,14)?"many":1==a%10&&11!=a%100?"one":"other"},12:function(a){return d(a,2,4)?"few":1==a?"one":"other"},13:function(a){return d(a%10,2,4)&&!d(a%100,12,14)?"few":1!=a&&d(a%10,0,1)||d(a%10,5,9)||d(a%100,12,14)?"many":1==a?"one":"other"},14:function(a){return d(a%100,3,4)?"few":2==a%100?"two":1==a%100?"one":"other"},15:function(a){return 0===a||d(a%100,2,10)?"few":d(a%100,11,19)?"many":1==a?"one":"other"},16:function(a){return 1==a%10&&11!=a?"one":"other"},17:function(a){return 3==a?"few":0===a?"zero":6==a?"many":2==a?"two":1==a?"one":"other"},18:function(a){return 0===a?"zero":d(a,0,2)&&0!==a&&2!=a?"one":"other"},19:function(a){return d(a,2,10)?"few":d(a,0,1)?"one":"other"},20:function(a){return!d(a%10,3,4)&&9!=a%10||d(a%100,10,19)||d(a%100,70,79)||d(a%100,90,99)?0===a%1e6&&0!==a?"many":2!=a%10||c(a%100,[12,72,92])?1!=a%10||c(a%100,[11,71,91])?"other":"one":"two":"few"},21:function(a){return 0===a?"zero":1==a?"one":"other"},22:function(a){return d(a,0,1)||d(a,11,99)?"one":"other"},23:function(a){return d(a%10,1,2)||0===a%20?"one":"other"},24:function(a){return d(a,3,10)||d(a,13,19)?"few":c(a,[2,12])?"two":c(a,[1,11])?"one":"other"}},f=b[a.replace(/-.*$/,"")];return f in e?e[f]:(console.warn("plural form unknown for ["+a+"]"),function(){return"other"})}function u(a,b,c){var f,g,h,e=d[a];if(!e){if(console.warn("#"+a+" is undefined."),!c)return null;e=c}f={};for(g in e)h=e[g],h=v(h,b,a,g),h=w(h,b,a),f[g]=h;return f}function v(a,b,c,e){var i,j,k,l,f=/\{\[\s*([a-zA-Z]+)\(([a-zA-Z]+)\)\s*\]\}/,g=f.exec(a);return g&&g.length?(i=g[1],j=g[2],b&&j in b?k=b[j]:j in d&&(k=d[j]),i in h&&(l=h[i],a=l(a,k,c,e)),a):a}function w(a,b,c){for(var h,i,e=/\{\{\s*(.+?)\s*\}\}/,g=e.exec(a);g;){if(!g||g.length<2)return a;if(h=g[1],i="",b&&h in b)i=b[h];else{if(!(h in d))return console.log("argument {{"+h+"}} for #"+c+" is undefined."),a;i=d[h][f]}a=a.substring(0,g.index)+i+a.substr(g.index+g[0].length),g=e.exec(a)}return a}function x(a){var d,e,g,h,i,j,k,c=n(a);if(c.id){if(d=u(c.id,c.args),!d)return console.warn("#"+c.id+" is undefined."),void 0;if(d[f]){if(0===y(a))a[f]=d[f];else{for(e=a.childNodes,g=!1,h=0,i=e.length;i>h;h++)3===e[h].nodeType&&/\S/.test(e[h].nodeValue)&&(g?e[h].nodeValue="":(e[h].nodeValue=d[f],g=!0));g||(j=b.createTextNode(d[f]),a.insertBefore(j,a.firstChild))}delete d[f]}for(k in d)a[k]=d[k]}}function y(a){var b,c;if(a.children)return a.children.length;if("undefined"!=typeof a.childElementCount)return a.childElementCount;for(b=0,c=0;c<a.childNodes.length;c++)b+=1===a.nodeType?1:0;return b}function z(a){var c,d,e;for(a=a||b.documentElement,c=m(a),d=c.length,e=0;d>e;e++)x(c[e]);x(a)}var d={},e="",f="textContent",g="",h={},i="loading",j=!0;return h.plural=function(a,b,c,e){var j,i=parseFloat(b);return isNaN(i)?a:e!=f?a:(h._pluralRules||(h._pluralRules=t(g)),j="["+h._pluralRules(i)+"]",0===i&&c+"[zero]"in d?a=d[c+"[zero]"][e]:1==i&&c+"[one]"in d?a=d[c+"[one]"][e]:2==i&&c+"[two]"in d?a=d[c+"[two]"][e]:c+j in d?a=d[c+j][e]:c+"[other]"in d&&(a=d[c+"[other]"][e]),a)},{get:function(a,b,c){var g,h,d=a.lastIndexOf("."),e=f;return d>0&&(e=a.substr(d+1),a=a.substring(0,d)),c&&(g={},g[e]=c),h=u(a,b,g),h&&e in h?h[e]:"{{"+a+"}}"},getData:function(){return d},getText:function(){return e},getLanguage:function(){return g},setLanguage:function(a){r(a,z)},getDirection:function(){var a=["ar","he","fa","ps","ur"];return a.indexOf(g)>=0?"rtl":"ltr"},translate:z,getReadyState:function(){return i},ready:function(c){c&&("complete"==i||"interactive"==i?a.setTimeout(c):b.addEventListener?b.addEventListener("localized",c):b.attachEvent&&b.documentElement.attachEvent("onpropertychange",function(a){"localized"===a.propertyName&&c()}))}}}(window,document);