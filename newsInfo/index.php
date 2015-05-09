<?php
header('content-type:text/html;charset = utf-8');

function loadData(){
	$filePath = "newsInfo.json";
	
	$file = file($filePath);
	$file = array_unique($file);

	$myfile = fopen($filePath, "w");
	for($i=0; $i<count($file); $i++) {
		if(!empty($file[$i])){
			fwrite($myfile, $file[$i]);}
	}
	fclose($myfile);

	$data = implode(',', $file);
	$data = "[".$data."]";
	$dataArray = json_decode($data, true);
	//echo $data;
	//var_dump($dataArray);
	
	return $dataArray;
}
?>


<!DOCTYPE html>
<html>
<head>
<meta charset="gb2312">
<link rel="stylesheet" href="http://code.jquery.com/mobile/1.3.2/jquery.mobile-1.3.2.min.css">
<script src="http://code.jquery.com/jquery-1.8.3.min.js"></script>
<script src="http://code.jquery.com/mobile/1.3.2/jquery.mobile-1.3.2.min.js"></script>
</head>
<body>

<div data-role="page">
	<div data-role="header">
    	<h1>新闻抓取结果</h1>
  	</div>

  	<div data-role="content">
  	    <ul data-role="listview">
		<?php
		$msg = loadData();
		$i = 0;
		foreach($msg as $va) { $i++; ?>
			<li>
				<a href = <?php echo $va['detailLink'] ?> >
				<h2><?php echo '['.$i.']-'.$va['title'] ?></h2>
				<p><?php echo $va['content'] ?></p>
				<span><?php echo $va['publishTime'] ?></span>
				</a>				
			</li>
		<?php }?>	
		</ul>
  	</div>

  	<div data-role="footer" data-tap-toggle="false" data-position="fixed">
    	<h1>技术支持：&nbsp;<a href = "mailto:lzq.zheng@qq.com" style="text-decoration:none;">@Rf-sama</a></h1>
  	</div>
</div> 

</body>
</html>


