#! /usr/bin/env python

import cgi, cgitb

print """
<html>
	<link rel="icon" href="graphics/pyramid.ico">

	<head>
		<title>Current Work</title>

	<style>
	body {
		font-family: helvetica;
	}

	a img {
		border: 0px none transparent;
	}

	.img-link {
		text-decoration: none;
	}

	#main {
		width: 500px;
		background-color:#ebebeb;
		color:black;

		border: 2px solid #CCCCCC;
		border-radius: 25px;

		text-align:center;
		padding:5px;

		margin: 0;
		position: absolute;
		top: 50%;
		left: 50%;
		margin-right: -50%;
		transform: translate(-50%, -50%);
	}

	#nav {
		width:200px;
		background-color: #ebebeb;
		color:black;

		border: 1px solid #CCCCCC;
		border-radius: 10px;

		text-align:center;
		margin: 0 auto;
		position: absolute;
		bottom: -40px;
		left: 150px;
	}	

	#txtgen {
		width:450px;
		background-color: #ebebeb;
		color:black;

		border: 1px solid #CCCCCC;
		border-radius: 25px;

		text-align:center;
		margin: 0 auto;
		position: absolute;
		top: -40px;
		left: 50px;
	}	

	</style>
	</head>

	<body>
		<div id="main">
			<h1 style="font-family:helvetica">Current Work</h1>

			<p style="font-familty:helvetica;margin-left:30px;" align="left">

			<a href="https://github.com/jvasilakes/nltk/tree/develop/nltk/sem_parse" class="img-link" target="_blank">
			  <img src="graphics/github-logo.gif" alt="github" style="width:20px;height:20px">
			</a>
			Thesis: adding a semantic parser to the NLTK Python library.<br><br>
			
			<a href="https://github.com/jvasilakes/txtgen" class="img-link" target="_blank">
			  <img src="graphics/github-logo.gif" alt="github" style="width:20px;height:20px">
			</a>
			TXTGEN: n-gram model based text generator.<br><br>

			<a href="https://github.com/jvasilakes/txtsh" class="img-link" target="_blank">
			  <img src="graphics/github-logo.gif" alt="github" style="width:20px;height:20px">
			</a>
			TXTSH: cli application for basic text analysis.

			<p>

			<div id="nav">
				<a href="homepage.html" style="text-decoration: none; color: #000000;">Home</a> &nbsp; 
				<a href="cv.html" style="text-decoration: none; color: #000000;">CV</a> &nbsp; 
				<a href="about.html" style="text-decoration: none; color: #000000;">About</a> &nbsp;
			</div>

		</div>


	</body>

</html>
"""
