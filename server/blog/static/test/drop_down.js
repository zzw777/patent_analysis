var DatabaseName = ["first","LBSMining","DataBase_1","DataBase_2"];

var Database_1 = ["result","Recall","Precision","Coverage","Popularity"];

var Database_2 = ["CheckInNyc","lxp","zmz"];

var Database_3 = ["test1","test2"];

var Database_4 = ["test3","test4"];

function DataBase()
{
	var s1 = document.getElementById("select1");

	for(var i=0;i<DatabaseName.length;i++)
	{
		s1.options.add(new Option(DatabaseName[i],DatabaseName[i]));
	}

}

function loadTables(n)
{
	var s2 = document.getElementById("select2");
	// alert(s2.options.length);
	for(var i=s2.options.length; i>0; i--)
	{
		s2.remove(i);
	}
	// alert("清空原始数据成功");
	if(n==0) return ;

	var a = eval("Database_"+ n);
	for(var i =0; i<a.length; i++)
	{
		s2.options.add(new Option(a[i],a[i]));
	}
	// alert("添加了新数据成功");
}

function loadDatabase()
{
	DataBase();
}