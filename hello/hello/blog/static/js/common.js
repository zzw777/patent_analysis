

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


