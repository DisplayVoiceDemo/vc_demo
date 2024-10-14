
one_audio_block_temple = """
                                {name}
                                <audio controls preload="none">
                                    <source src={path}>
                                </audio>
"""

one_table_line = """
                            <tr>
                                {src_audio}
                                {tar_audio}
                                {conversion_audio}
                            </tr>
"""
table_temple = """
                    <!-- one table -->
                    <table class="table">
                        <thead>
                            <tr>
                                <th scope="col">Source</th>
                                <th scope="col">Target</th>
                                <th scope="col">Conversion</th>
                            </tr>
                        </thead>
                        <tbody>
                            {lines}
                            <h3 class="post-meta" id="s2s">
                                {test_tag}
                            </h3>
                        </tbody>
                    </table>
"""

experiment_temple = """
                <!-- one experience -->
                <div class="post-preview">
                    <h2 class="post-title">
                        {experiment_name}
                    </h2>
                    {tables}
                </div>
"""

page_temple = """
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="anonymous">

    <title>{title}</title>

    <!-- Bootstrap core CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.1/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom fonts for this template -->
    <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
    <link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet'
        type='text/css'>
    <link
        href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800'
        rel='stylesheet' type='text/css'>

    <!-- Custom styles for this template -->
    <link href="css/clean-blog.css" rel="stylesheet">

    <link rel="stylesheet" href="./css/fontawesome.all.min.css">

    <script defer src="./js/fontawesome.all.min.js"></script>
    <!-- Bootstrap core JavaScript -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
        integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx"
        crossorigin="anonymous"></script>

    <!-- Custom scripts for this template -->
    <script src="js/clean-blog.js"></script>
    <script src="js/interp.js"></script>

</head>

<body id="page-top">

    <!-- <nav class="navbar navbar-expand-lg fixed-top" id="mainNav">
		<div class="container">
			<a class="navbar-brand js-scroll-trigger" href="#page-top">LDM-SVC</a>
			<button class="navbar-toggler navbar-toggler-right font-weight-bold text-white rounded" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">Menu <i class="fas fa-bars"></i></button>
            <div class="collapse navbar-collapse" id="navbarResponsive">
				<ul class="navbar-nav ml-auto">
					<li class="nav-item mx-0 mx-lg-1"><a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#abstract">Abstract</a>
					<li class="nav-item mx-0 mx-lg-1"><a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#s2s">Seen-to-Seen</a></li>
					<li class="nav-item mx-0 mx-lg-1"><a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#u2s">Zero-shot Unseen-to-Unseen</a></li>
				</ul>
			</div>
		</div>
	</nav> -->

    <!-- Page Header -->
    <header class="masthead" style="background-image: url('img/home-bg.jpg')">
        <div class="container" style="padding-bottom:10px">
            <div class="row">
                <div class="col-lg-10 col-md-10 mx-auto">
                    <div class="site-heading">
                        <h1>{big_header}</h1>
                        <span class="subheading">
                            {sub_header}
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <div class="container">
        <div class="row">
            <div class="col-lg-14 col-md-12 mx-auto">
                <div class="post-preview" id="abstract">
                    <h2 class="post-title">
                        Abstract
                    </h2>
                    <p>
                        {abstract}
                    </p>
                </div>
                <!-- ![arch](images/pic1.png) -->
                <!-- <img src="images/pic1.png" alt="ldm-svc" width="1200"> -->
                <!-- experience start -->
                {experimental_results}
                <!-- experience end -->
            </div>
        </div>
</body>

</html>
"""
