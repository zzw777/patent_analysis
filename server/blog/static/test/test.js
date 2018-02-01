function gradeChange(){
            // alert("成功进入这个函数！");
            var select_obj = document.getElementById("select2");
            // alert("success achieve select_obj !");
            var select_value = select_obj.options[select_obj.selectedIndex].value;
            // alert(select_value);
            if(select_value == "Recall"){
                document.getElementById('picture').style.display = "none";
                document.getElementById("container_test").style.display="none";
                document.getElementById("Recall").style.display="block";
                document.getElementById("Precision").style.display="none";
                document.getElementById("Coverage").style.display="none";
                document.getElementById("Popularity").style.display="none";
            }else if(select_value == "result"){
                document.getElementById('picture').style.display = "none";
                document.getElementById("container_test").style.display="block";
                document.getElementById("Recall").style.display="none";
                document.getElementById("Precision").style.display="none";
                alert("进入了此函数:container_test的属性："+ shuxing1 +"  test的属性："+ shuxing2);
            }else if(select_value == "Precision"){
                document.getElementById('picture').style.display = "none";
                document.getElementById("container_test").style.display="none";
                document.getElementById("Recall").style.display="none";
                document.getElementById("Precision").style.display="block";
                document.getElementById("Coverage").style.display="none";
                document.getElementById("Popularity").style.display="none";
            }else if(select_value == "Coverage"){
                document.getElementById('picture').style.display = "none";
                document.getElementById("container_test").style.display="none";
                document.getElementById("Recall").style.display="none";
                document.getElementById("Precision").style.display="none";
                document.getElementById("Coverage").style.display="block";
                document.getElementById("Popularity").style.display="none";
            }else if(select_value == "Popularity"){
                document.getElementById('picture').style.display = "none";
                document.getElementById("container_test").style.display="none";
                document.getElementById("Recall").style.display="none";
                document.getElementById("Precision").style.display="none";
                document.getElementById("Coverage").style.display="none";
                document.getElementById("Popularity").style.display="block";
            }else{

            }
        }

//
// $.ajax({
//     url:'http://127.0.0.1:8000/ajax_dict',
//     type:'get',
//     datatype:"json",
//     success:function(data){
//         var name_ajax=data[0].name;
//         var data_ajax=data[0].data;
//         var count = data.length;
//         $(function(){
//         var chart=Highcharts.chart('container_test',{
//         title: {
//             text: '不同城市月平均气温',
//             x: -20
//         },
//         subtitle:{
//             text: '数据来源: MySQL',
//             x: -20
//         },
//         xAxis: {
//             categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
//              },
//         yAxis: {
//             title: {
//                 text: 'temperature:(°C)'
//             },
//             plotLines: [{
//                 value: 0,
//                 width: 1,
//                 color: '#808080'
//             }]
//         },
//         tooltip:{
//                 valueSuffix:'°C'
//             },
//         legend:{
//             layout: 'vertical',
//             align: 'right',
//             verticalAlign:'middle',
//             borderWidth: 0
//         },
//         series:[]
//     });
//     for(var i = 0; i<count; i++)
//     {
//         chart.addSeries({
//             name:data[i].name,
//             data:data[i].data
//         },redraw=true);
//     }
//     });
//
// }})
//
//
// //---------------------------------------------------
// $.ajax({
//     url:'http://127.0.0.1:8000/ajax_dict1',
//     type:'get',
//     datatype:"json",
//     success:function(data){
//         var name_ajax=data[0].name;
//         var data_ajax=data[0].data;
//         var count = data.length;
//         $(function(){
//         var chart=Highcharts.chart('Recall',{
//         title: {
//             text: 'Recommend System 召回率',
//             x: -20
//         },
//         subtitle:{
//             text: '数据来源: MySQL',
//             x: -20
//         },
//         xAxis: {
//             categories: ['K=5', 'K=10', 'K=15', 'K=20', 'K=30', 'K=40', 'K=80', 'K=160']
//              },
//         yAxis: {
//             title: {
//                 text: '数值:百分数%'
//             },
//             plotLines: [{
//                 value: 0,
//                 width: 1,
//                 color: '#808080'
//             }]
//         },
//         tooltip:{
//                 valueSuffix:'%'
//             },
//         legend:{
//             layout: 'vertical',
//             align: 'right',
//             verticalAlign:'middle',
//             borderWidth: 0
//         },
//         series:[]
//     });
//     for(var i = 0; i<count; i++)
//     {
//         chart.addSeries({
//             name:data[i].name,
//             data:data[i].data
//         },redraw=true);
//     }
//     });
// }})
//
// //-------------Precision-----------------
// $.ajax({
//     url:'http://127.0.0.1:8000/ajax_dict2',
//     type:'get',
//     datatype:"json",
//     success:function(data){
//         var name_ajax=data[0].name;
//         var data_ajax=data[0].data;
//         var count = data.length;
//         $(function(){
//         var chart=Highcharts.chart('Precision',{
//         title: {
//             text: 'Recommend System 准确率',
//             x: -20
//         },
//         subtitle:{
//             text: '数据来源: MySQL',
//             x: -20
//         },
//         xAxis: {
//             categories: ['K=5', 'K=10', 'K=15', 'K=20', 'K=30', 'K=40', 'K=80', 'K=160']
//              },
//         yAxis: {
//             title: {
//                 text: '数值:百分数%'
//             },
//             plotLines: [{
//                 value: 0,
//                 width: 1,
//                 color: '#9B30FF'
//             }]
//         },
//         tooltip:{
//                 valueSuffix:'%'
//             },
//         legend:{
//             layout: 'vertical',
//             align: 'right',
//             verticalAlign:'middle',
//             borderWidth: 0
//         },
//         series:[]
//     });
//     for(var i = 0; i<count; i++)
//     {
//         chart.addSeries({
//             name:data[i].name,
//             data:data[i].data
//         },redraw=true);
//     }
//     });
// }})
//
// //--------------Precision----------------
// $.ajax({
//     url:'http://127.0.0.1:8000/ajax_dict3',
//     type:'get',
//     datatype:"json",
//     success:function(data){
//         var name_ajax=data[0].name;
//         var data_ajax=data[0].data;
//         var count = data.length;
//         $(function(){
//         var chart=Highcharts.chart('Coverage',{
//         title: {
//             text: 'Recommend System 覆盖率',
//             x: -20
//         },
//         subtitle:{
//             text: '数据来源: MySQL',
//             x: -20
//         },
//         xAxis: {
//             categories: ['K=5', 'K=10', 'K=15', 'K=20', 'K=30', 'K=40', 'K=80', 'K=160']
//              },
//         yAxis: {
//             title: {
//                 text: '数值:百分数%'
//             },
//             plotLines: [{
//                 value: 0,
//                 width: 1,
//                 color: '#9B30FF'
//             }]
//         },
//         tooltip:{
//                 valueSuffix:'%'
//             },
//         legend:{
//             layout: 'vertical',
//             align: 'right',
//             verticalAlign:'middle',
//             borderWidth: 0
//         },
//         series:[]
//     });
//     for(var i = 0; i<count; i++)
//     {
//         chart.addSeries({
//             name:data[i].name,
//             data:data[i].data
//         },redraw=true);
//     }
//     });
// }})
//
// //------------------------流行度-----------------------
// $.ajax({
//     url:'http://127.0.0.1:8000/ajax_dict4',
//     type:'get',
//     datatype:"json",
//     success:function(data){
//         var name_ajax=data[0].name;
//         var data_ajax=data[0].data;
//         var count = data.length;
//         $(function(){
//         var chart=Highcharts.chart('Popularity',{
//         title: {
//             text: 'Recommend System 流行度',
//             x: -20
//         },
//         subtitle:{
//             text: '数据来源: MySQL',
//             x: -20
//         },
//         xAxis: {
//             categories: ['K=5', 'K=10', 'K=15', 'K=20', 'K=30', 'K=40', 'K=80', 'K=160']
//              },
//         yAxis: {
//             title: {
//                 text: '数值'
//             },
//             plotLines: [{
//                 value: 0,
//                 width: 1,
//                 color: '#9B30FF'
//             }]
//         },
//         tooltip:{
//                 valueSuffix:' '
//             },
//         legend:{
//             layout: 'vertical',
//             align: 'right',
//             verticalAlign:'middle',
//             borderWidth: 0
//         },
//         series:[]
//     });
//     for(var i = 0; i<count; i++)
//     {
//         chart.addSeries({
//             name:data[i].name,
//             data:data[i].data
//         },redraw=true);
//     }
//     });
// }})
