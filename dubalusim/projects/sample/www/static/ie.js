!function(){(function(a,b){function l(a,b){var c=a.createElement("p"),d=a.getElementsByTagName("head")[0]||a.documentElement;return c.innerHTML="x<style>"+b+"</style>",d.insertBefore(c.lastChild,d.firstChild)}function m(){var a=t.elements;return typeof a=="string"?a.split(" "):a}function n(a,b){var c=t.elements;typeof c!="string"&&(c=c.join(" ")),typeof a!="string"&&(a=a.join(" ")),t.elements=c+" "+a,s(b)}function o(a){var b=j[a[h]];return b||(b={},i++,a[h]=i,j[i]=b),b}function p(a,c,d){c||(c=b);if(k)return c.createElement(a);d||(d=o(c));var g;return d.cache[a]?g=d.cache[a].cloneNode():f.test(a)?g=(d.cache[a]=d.createElem(a)).cloneNode():g=d.createElem(a),g.canHaveChildren&&!e.test(a)&&!g.tagUrn?d.frag.appendChild(g):g}function q(a,c){a||(a=b);if(k)return a.createDocumentFragment();c=c||o(a);var d=c.frag.cloneNode(),e=0,f=m(),g=f.length;for(;e<g;e++)d.createElement(f[e]);return d}function r(a,b){b.cache||(b.cache={},b.createElem=a.createElement,b.createFrag=a.createDocumentFragment,b.frag=b.createFrag()),a.createElement=function(c){return t.shivMethods?p(c,a,b):b.createElem(c)},a.createDocumentFragment=Function("h,f","return function(){var n=f.cloneNode(),c=n.createElement;h.shivMethods&&("+m().join().replace(/[\w\-:]+/g,function(a){return b.createElem(a),b.frag.createElement(a),'c("'+a+'")'})+");return n}")(t,b.frag)}function s(a){a||(a=b);var c=o(a);return t.shivCSS&&!g&&!c.hasCSS&&(c.hasCSS=!!l(a,"article,aside,dialog,figcaption,figure,footer,header,hgroup,main,nav,section{display:block}mark{background:#FF0;color:#000}template{display:none}")),k||r(a,c),a}var c="3.7.2",d=a.html5||{},e=/^<|^(?:button|map|select|textarea|object|iframe|option|optgroup)$/i,f=/^(?:a|b|code|div|fieldset|h1|h2|h3|h4|h5|h6|i|label|li|ol|p|q|span|strong|style|table|tbody|td|th|tr|ul)$/i,g,h="_html5shiv",i=0,j={},k;(function(){try{var a=b.createElement("a");a.innerHTML="<xyz></xyz>",g="hidden"in a,k=a.childNodes.length==1||function(){b.createElement("a");var a=b.createDocumentFragment();return typeof a.cloneNode=="undefined"||typeof a.createDocumentFragment=="undefined"||typeof a.createElement=="undefined"}()}catch(c){g=!0,k=!0}})();var t={elements:d.elements||"abbr article aside audio bdi canvas data datalist details dialog figcaption figure footer header hgroup main mark meter nav output picture progress section summary template time video",version:c,shivCSS:d.shivCSS!==!1,supportsUnknownElements:k,shivMethods:d.shivMethods!==!1,type:"default",shivDocument:s,createElement:p,createDocumentFragment:q,addElements:n};a.html5=t,s(b)})(this,document),function(a){function y(){u(!0)}"use strict";var b={};a.respond=b,b.update=function(){};var c=[],d=function(){var b=!1;try{b=new a.XMLHttpRequest}catch(c){b=new a.ActiveXObject("Microsoft.XMLHTTP")}return function(){return b}}(),e=function(a,b){var c=d();if(!c)return;c.open("GET",a,!0),c.onreadystatechange=function(){if(c.readyState!==4||c.status!==200&&c.status!==304)return;b(c.responseText)};if(c.readyState===4)return;c.send(null)},f=function(a){return a.replace(b.regex.minmaxwh,"").match(b.regex.other)};b.ajax=e,b.queue=c,b.unsupportedmq=f,b.regex={media:/@media[^\{]+\{([^\{\}]*\{[^\}\{]*\})+/gi,keyframes:/@(?:\-(?:o|moz|webkit)\-)?keyframes[^\{]+\{(?:[^\{\}]*\{[^\}\{]*\})+[^\}]*\}/gi,comments:/\/\*[^*]*\*+([^/][^*]*\*+)*\//gi,urls:/(url\()['"]?([^\/\)'"][^:\)'"]+)['"]?(\))/g,findStyles:/@media *([^\{]+)\{([\S\s]+?)$/,only:/(only\s+)?([a-zA-Z]+)\s?/,minw:/\(\s*min\-width\s*:\s*(\s*[0-9\.]+)(px|em)\s*\)/,maxw:/\(\s*max\-width\s*:\s*(\s*[0-9\.]+)(px|em)\s*\)/,minmaxwh:/\(\s*m(in|ax)\-(height|width)\s*:\s*(\s*[0-9\.]+)(px|em)\s*\)/gi,other:/\([^\)]*\)/g},b.mediaQueriesSupported=a.matchMedia&&a.matchMedia("only all")!==null&&a.matchMedia("only all").matches;if(b.mediaQueriesSupported)return;var g=a.document,h=g.documentElement,i=[],j=[],k=[],l={},m=30,n=g.getElementsByTagName("head")[0]||h,o=g.getElementsByTagName("base")[0],p=n.getElementsByTagName("link"),q,r,s,t=function(){var a,b=g.createElement("div"),c=g.body,d=h.style.fontSize,e=c&&c.style.fontSize,f=!1;return b.style.cssText="position:absolute;font-size:1em;width:1em",c||(c=f=g.createElement("body"),c.style.background="none"),h.style.fontSize="100%",c.style.fontSize="100%",c.appendChild(b),f&&h.insertBefore(c,h.firstChild),a=b.offsetWidth,f?h.removeChild(c):c.removeChild(b),h.style.fontSize=d,e&&(c.style.fontSize=e),a=s=parseFloat(a),a},u=function(b){var c="clientWidth",d=h[c],e=g.compatMode==="CSS1Compat"&&d||g.body[c]||d,f={},l=p[p.length-1],o=(new Date).getTime();if(b&&q&&o-q<m){a.clearTimeout(r),r=a.setTimeout(u,m);return}q=o;for(var v in i)if(i.hasOwnProperty(v)){var w=i[v],x=w.minw,y=w.maxw,z=x===null,A=y===null,B="em";!x||(x=parseFloat(x)*(x.indexOf(B)>-1?s||t():1)),!y||(y=parseFloat(y)*(y.indexOf(B)>-1?s||t():1));if(!w.hasquery||(!z||!A)&&(z||e>=x)&&(A||e<=y))f[w.media]||(f[w.media]=[]),f[w.media].push(j[w.rules])}for(var C in k)k.hasOwnProperty(C)&&k[C]&&k[C].parentNode===n&&n.removeChild(k[C]);k.length=0;for(var D in f)if(f.hasOwnProperty(D)){var E=g.createElement("style"),F=f[D].join("\n");E.type="text/css",E.media=D,n.insertBefore(E,l.nextSibling),E.styleSheet?E.styleSheet.cssText=F:E.appendChild(g.createTextNode(F)),k.push(E)}},v=function(a,c,d){var e=a.replace(b.regex.comments,"").replace(b.regex.keyframes,"").match(b.regex.media),g=e&&e.length||0;c=c.substring(0,c.lastIndexOf("/"));var h=function(a){return a.replace(b.regex.urls,"$1"+c+"$2$3")},k=!g&&d;c.length&&(c+="/"),k&&(g=1);for(var l=0;l<g;l++){var m,n,o,p;k?(m=d,j.push(h(a))):(m=e[l].match(b.regex.findStyles)&&RegExp.$1,j.push(RegExp.$2&&h(RegExp.$2))),o=m.split(","),p=o.length;for(var q=0;q<p;q++){n=o[q];if(f(n))continue;i.push({media:n.split("(")[0].match(b.regex.only)&&RegExp.$2||"all",rules:j.length-1,hasquery:n.indexOf("(")>-1,minw:n.match(b.regex.minw)&&parseFloat(RegExp.$1)+(RegExp.$2||""),maxw:n.match(b.regex.maxw)&&parseFloat(RegExp.$1)+(RegExp.$2||"")})}}u()},w=function(){if(c.length){var b=c.shift();e(b.href,function(c){v(c,b.href,b.media),l[b.href]=!0,a.setTimeout(function(){w()},0)})}},x=function(){for(var b=0;b<p.length;b++){var d=p[b],e=d.href,f=d.media,g=d.rel&&d.rel.toLowerCase()==="stylesheet";if(!!e&&g&&!l[e])if(d.styleSheet&&d.styleSheet.rawCssText)v(d.styleSheet.rawCssText,e,f),l[e]=!0;else if(!/^([a-zA-Z:]*\/\/)/.test(e)&&!o||e.replace(RegExp.$1,"").split("/")[0]===a.location.host)e.substring(0,2)==="//"&&(e=a.location.protocol+e),c.push({href:e,media:f})}w()};x(),b.update=x,b.getEmValue=t,a.addEventListener?a.addEventListener("resize",y,!1):a.attachEvent&&a.attachEvent("onresize",y)}(this),$(function(){$("[placeholder]").focus(function(){var a=$(this);a.val()==a.attr("placeholder")&&(a.val(""),a.removeClass("placeholder"))}).blur(function(){var a=$(this);if(a.val()==""||a.val()==a.attr("placeholder"))a.addClass("placeholder"),a.val(a.attr("placeholder"))}).blur(),$("[placeholder]").parents("form").submit(function(){$(this).find("[placeholder]").each(function(){var a=$(this);a.val()==a.attr("placeholder")&&a.val("")})})})}()