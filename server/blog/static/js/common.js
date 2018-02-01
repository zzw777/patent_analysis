

// Bind click function
// function initListListeners(ListID,List){    
//   $("#"+ListID+" tbody").unbind();

//   function tableClick() {
//     List.$('tr.selected').removeClass('selected');
//     $(this).addClass('selected');
//   }
//   function tableDBLClick() {
//     if (List.$('tr.selected').length != 0) {
//       var para = {
//         "id":"Modal",
//         "size":"modal-dialog modal-lg",
//         "title":List.rows('.selected').data()[0][2],
//         "parent":$("#PresentationsShell"),
//         "subject":[
//           creSupplementList($("<div>"),"SubList")
//         ],
//         "backdrop":true,
//         "buttonID":"Close",
//         "button":"Close",
//         "EVENT":
//           function Close(){
//             $("#closeSubModal").click();
//           }
//       };
//       initModal(para);
//       initModalList({"Supplement":List.rows('.selected').data()[0][2]},"SubList");
//     }
//     else {
//       alert("Please select a presentation!")
//     }
//   }
//   $("#"+ListID+" tbody").on( 'click', 'tr', tableClick);
//   $("#"+ListID+" tbody").on( 'dblclick', 'tr', tableDBLClick);
// }



function creSupplementList(Parent,id) {
  var table = $("<table>",{id:id||"List",class:"display",cellspacing:"0",width:"100%"});
  var thead = $("<thead>").append($("<tr>",{id:(id?"SubSearch":"Search")})
                                  .append($("<th>").append("No."))
                                  .append($("<th>").append("Type"))
                                  .append($("<th>").append("Title")));
  Parent.append(table.append(thead));
  return Parent;
}


function creAddPresentation(Parent,id){
  var label = $("<label>",{class:"col-sm-3",align:"right"}).append("Meeting Date: &nbsp;");
  var input = $("<input>",{class:"col-sm-2",type:"text",id:"MeetingDate",readonly:true});
  var DateDIV = $("<div>",{class:"col-sm-12"});
  DateDIV.append(label).append(input);
  var label = $("<label>",{class:"col-sm-3",align:"right",style:"float:none;vertical-align:middle;display:inline-block;margin-top:-10px"}).append("Speaker: &nbsp;");
  var combobox = $("<div>",{class:"col-sm-3",style:"display:inline-block;margin-left:-15px"}).append($("<div>",{id:"Speaker"}));
  var SpeakerDIV = $("<div>",{class:"col-sm-12",style:"white-space:nowrap;margin-bottom:5px"});
  SpeakerDIV.append(label).append(combobox);
  // var label = $("<label>",{class:"col-sm-3",align:"right",style:"float:none;vertical-align:middle;display:inline-block;margin-top:-10px"}).append("Category: &nbsp;");
  // var combobox = $("<div>",{class:"col-sm-3",style:"display:inline-block;margin-left:-15px"}).append($("<div>",{id:"Category"}));
  // var CategoryDIV = $("<div>",{class:"col-sm-12",style:"white-space:nowrap;margin-bottom:5px"});
  // CategoryDIV.append(label).append(combobox);
  var label = $("<label>",{class:"col-sm-3",align:"right"}).append("Title: &nbsp;");
  var input = $("<input>",{class:"col-sm-9 range",type:"text",id:"Title"});
  var TitleDIV = $("<div>",{class:"col-sm-12"});
  TitleDIV.append(label).append(input);
  var label = $("<label>",{class:"col-sm-3",align:"right"}).append("URL: &nbsp;");
  var input = $("<input>",{class:"col-sm-9 range",type:"text",id:"TitleURL"});
  var TitleURLDIV = $("<div>",{class:"col-sm-12"});
  TitleURLDIV.append(label).append(input);
  var label = $("<label>",{class:"col-sm-3",align:"right",style:"float:none;vertical-align:middle;display:inline-block;margin-top:-10px"}).append("Supplement: &nbsp;");
  var combobox = $("<div>",{class:"col-sm-3",style:"display:inline-block;margin-left:-15px"}).append($("<div>",{id:"SupplementCount"}));
  var CountDIV = $("<div>",{class:"col-sm-12",style:"white-space:nowrap"});
  CountDIV.append(label).append(combobox);
  var SupplementDIV = $("<div>",{class:"col-sm-12"});

  Parent.append(DateDIV).append(SpeakerDIV).append(TitleDIV).append(TitleURLDIV).append(CountDIV).append(SupplementDIV);
  return Parent;
}


// 初始化信息列表
function initList(List,para){
  if (List!=null) {
    List.destroy();
  }
  var List = $('#'+para.id).DataTable({
    "data": para.data,
    "columns": para.columns,
    "dom": 'flrtip',
    "order": [[ 0, "desc" ]],
  });

  return List;
}




// 初始化信息列表
function initLocalList(List,para){
  if (List!=null) {
      List.destroy();
  }

  var List = $('#'+para.id).DataTable({
      data: para.dataset,
      columns: para.columns,
      dom: 'lfrtip',
  })

  return List;
}


// http://spin.js.org/#v2.3.2
!function(a,b){"object"==typeof module&&module.exports?module.exports=b():"function"==typeof define&&define.amd?define(b):a.Spinner=b()}(this,function(){"use strict";function a(a,b){var c,d=document.createElement(a||"div");for(c in b)d[c]=b[c];return d}function b(a){for(var b=1,c=arguments.length;c>b;b++)a.appendChild(arguments[b]);return a}function c(a,b,c,d){var e=["opacity",b,~~(100*a),c,d].join("-"),f=.01+c/d*100,g=Math.max(1-(1-a)/b*(100-f),a),h=j.substring(0,j.indexOf("Animation")).toLowerCase(),i=h&&"-"+h+"-"||"";return m[e]||(k.insertRule("@"+i+"keyframes "+e+"{0%{opacity:"+g+"}"+f+"%{opacity:"+a+"}"+(f+.01)+"%{opacity:1}"+(f+b)%100+"%{opacity:"+a+"}100%{opacity:"+g+"}}",k.cssRules.length),m[e]=1),e}function d(a,b){var c,d,e=a.style;if(b=b.charAt(0).toUpperCase()+b.slice(1),void 0!==e[b])return b;for(d=0;d<l.length;d++)if(c=l[d]+b,void 0!==e[c])return c}function e(a,b){for(var c in b)a.style[d(a,c)||c]=b[c];return a}function f(a){for(var b=1;b<arguments.length;b++){var c=arguments[b];for(var d in c)void 0===a[d]&&(a[d]=c[d])}return a}function g(a,b){return"string"==typeof a?a:a[b%a.length]}function h(a){this.opts=f(a||{},h.defaults,n)}function i(){function c(b,c){return a("<"+b+' xmlns="urn:schemas-microsoft.com:vml" class="spin-vml">',c)}k.addRule(".spin-vml","behavior:url(#default#VML)"),h.prototype.lines=function(a,d){function f(){return e(c("group",{coordsize:k+" "+k,coordorigin:-j+" "+-j}),{width:k,height:k})}function h(a,h,i){b(m,b(e(f(),{rotation:360/d.lines*a+"deg",left:~~h}),b(e(c("roundrect",{arcsize:d.corners}),{width:j,height:d.scale*d.width,left:d.scale*d.radius,top:-d.scale*d.width>>1,filter:i}),c("fill",{color:g(d.color,a),opacity:d.opacity}),c("stroke",{opacity:0}))))}var i,j=d.scale*(d.length+d.width),k=2*d.scale*j,l=-(d.width+d.length)*d.scale*2+"px",m=e(f(),{position:"absolute",top:l,left:l});if(d.shadow)for(i=1;i<=d.lines;i++)h(i,-2,"progid:DXImageTransform.Microsoft.Blur(pixelradius=2,makeshadow=1,shadowopacity=.3)");for(i=1;i<=d.lines;i++)h(i);return b(a,m)},h.prototype.opacity=function(a,b,c,d){var e=a.firstChild;d=d.shadow&&d.lines||0,e&&b+d<e.childNodes.length&&(e=e.childNodes[b+d],e=e&&e.firstChild,e=e&&e.firstChild,e&&(e.opacity=c))}}var j,k,l=["webkit","Moz","ms","O"],m={},n={lines:12,length:7,width:5,radius:10,scale:1,corners:1,color:"#000",opacity:.25,rotate:0,direction:1,speed:1,trail:100,fps:20,zIndex:2e9,className:"spinner",top:"50%",left:"50%",shadow:!1,hwaccel:!1,position:"absolute"};if(h.defaults={},f(h.prototype,{spin:function(b){this.stop();var c=this,d=c.opts,f=c.el=a(null,{className:d.className});if(e(f,{position:d.position,width:0,zIndex:d.zIndex,left:d.left,top:d.top}),b&&b.insertBefore(f,b.firstChild||null),f.setAttribute("role","progressbar"),c.lines(f,c.opts),!j){var g,h=0,i=(d.lines-1)*(1-d.direction)/2,k=d.fps,l=k/d.speed,m=(1-d.opacity)/(l*d.trail/100),n=l/d.lines;!function o(){h++;for(var a=0;a<d.lines;a++)g=Math.max(1-(h+(d.lines-a)*n)%l*m,d.opacity),c.opacity(f,a*d.direction+i,g,d);c.timeout=c.el&&setTimeout(o,~~(1e3/k))}()}return c},stop:function(){var a=this.el;return a&&(clearTimeout(this.timeout),a.parentNode&&a.parentNode.removeChild(a),this.el=void 0),this},lines:function(d,f){function h(b,c){return e(a(),{position:"absolute",width:f.scale*(f.length+f.width)+"px",height:f.scale*f.width+"px",background:b,boxShadow:c,transformOrigin:"left",transform:"rotate("+~~(360/f.lines*k+f.rotate)+"deg) translate("+f.scale*f.radius+"px,0)",borderRadius:(f.corners*f.scale*f.width>>1)+"px"})}for(var i,k=0,l=(f.lines-1)*(1-f.direction)/2;k<f.lines;k++)i=e(a(),{position:"absolute",top:1+~(f.scale*f.width/2)+"px",transform:f.hwaccel?"translate3d(0,0,0)":"",opacity:f.opacity,animation:j&&c(f.opacity,f.trail,l+k*f.direction,f.lines)+" "+1/f.speed+"s linear infinite"}),f.shadow&&b(i,e(h("#000","0 0 4px #000"),{top:"2px"})),b(d,b(i,h(g(f.color,k),"0 0 1px rgba(0,0,0,.1)")));return d},opacity:function(a,b,c){b<a.childNodes.length&&(a.childNodes[b].style.opacity=c)}}),"undefined"!=typeof document){k=function(){var c=a("style",{type:"text/css"});return b(document.getElementsByTagName("head")[0],c),c.sheet||c.styleSheet}();var o=e(a("group"),{behavior:"url(#default#VML)"});!d(o,"transform")&&o.adj?i():j=d(o,"animation")}return h});

// 遮盖罩相关参数与函数
var opts = {
      lines: 9                      // The number of lines to draw
    , length: 28                    // The length of each line
    , width: 23                     // The line thickness
    , radius: 37                    // The radius of the inner circle
    , scale: 0.5                    // Scales overall size of the spinner
    , corners: 1                    // Corner roundness (0..1)
    , color: '#000'                 // #rgb or #rrggbb or array of colors
    , opacity: 0.25                 // Opacity of the lines
    , rotate: 0                     // The rotation offset
    , direction: 1                  // 1: clockwise, -1: counterclockwise
    , speed: 1                      // Rounds per second
    , trail: 60                     // Afterglow percentage
    , fps: 20                       // Frames per second when using setTimeout() as a fallback for CSS
    , zIndex: 2e9                   // The z-index (defaults to 2000000000)
    , className: 'spinner'          // The CSS class to assign to the spinner
    , top: '20%'                    // Top position relative to parent
    , left: '50%'                   // Left position relative to parent
    , shadow: true                  // Whether to render a shadow
    , hwaccel: false                // Whether to use hardware acceleration
    , position: 'absolute'          // Element positioning
};

function loadingSign(panelName){
    var target = document.getElementById(panelName);
    spinner = new Spinner(opts).spin(target);
    $("#"+panelName+" *").prop('disabled',true);
}

function loadingSignStop(panelName){
    $("#"+panelName+" *").prop('disabled',false);
    if (typeof spinner != 'undefined') {
        spinner.stop();
    };
}