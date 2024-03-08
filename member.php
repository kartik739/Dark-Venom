<html>
<head>
<title>{$mybb->settings['bbname']} - {$lang->profile}</title>
{$headerinclude}
<script type="text/javascript" src="{$mybb->asset_url}/jscripts/report.js?ver=1820"></script>
</head>
<body>
{$header}
<div class="profile-container">
	<div class="p-user fullwidth">
		<div class="p-top">
			<div class="user-details ud-img p-top-bg" style="background-image: url(https://sinfulcdn.b-cdn.net/uploads/profilepics/profilepic_1.jpg)"></div>
		</div>
	</div>
</div>
<div class="profile-container">
	<div class="p-sidebar tborder border-top-none">
		<div class="avatar text-center">{$avatar}</div>
		<br>
		<div class="text-center">
		<span class="x-largetext">{$formattedname}</span>
		<br>
		<span class="smalltext">{$usertitle}</span>
		<br>
		<div class="text-center">{$groupimage}</div>
		<br>
		<div class="p-stats">
			<div class="trow1 d-flex">UID: <span class="ml-auto p-uid">{$memprofile['uid']}</span></div>
			<div class="trow2 d-flex">{$lang->postbit_status}<span class="ml-auto">{$online_status}</span></div>
			<div class="trow1 d-flex">{$lang->registration_date}<span class="ml-auto">{$memregdate}</span></div>
			<div class="trow2 d-flex">{$lang->date_of_birth}<span class="ml-auto">{$membday} {$membdayage}</span></div>
			{$warning_level}
			{$contact_details}
		</div>
		</div>
	</div>
	<div class="p-content">
		<br>
		<div class="section">
			<div class="thead">
				<strong>Information about {$memprofile['username']}</strong>
			</div>
			<div class="row d-flex">
				<div class="row-inner d-flex">
					<div class="trow1 d-flex align-items-center fullwidth"><i class="fa fa-eye"></i>&nbsp;{$lang->lastvisit}</div>
					<div class="trow1 d-flex align-items-center fullwidth"><span class="ml-auto">{$memlastvisitdate}</span></div>
				</div>
				<div class="row-inner d-flex">
					<div class="trow1 d-flex align-items-center fullwidth"><i class="far fa-clock"></i>&nbsp;{$lang->timeonline}</div>
					<div class="trow1 d-flex align-items-center fullwidth"><span class="ml-auto">{$timeonline}</span></div>
				</div>
			</div>
			<div class="row d-flex">
				{$reputation}
				{$referrals}
			</div>
			<div class="row d-flex">
				<div class="row-inner d-flex">
					<div class="trow1 d-flex align-items-center fullwidth"><i class="fa fa-heart"></i>&nbsp;Likes Received:</div>
					<div class="trow1 d-flex align-items-center fullwidth"><span class="ml-auto">N/A</span></div>
				</div>
				<div class="row-inner d-flex">
					<div class="trow1 d-flex align-items-center fullwidth"><i class="fas fa-thumbs-up"></i>&nbsp;Likes Given:</div>
					<div class="trow1 d-flex align-items-center fullwidth"><span class="ml-auto">N/A</span></div>
				</div>
			</div>
			<div class="row d-flex">
				<div class="row-inner d-flex">
					<div class="trow1 d-flex align-items-center fullwidth"><i class="fa fa-book"></i>&nbsp; Total Threads:</div>
					<div class="trow1 d-flex align-items-center fullwidth"><span class="ml-auto"><a href="search.php?action=finduserthreads&amp;uid={$memprofile['uid']}">{$memprofile['threadnum']}</a></span></div>
				</div>
				<div class="row-inner d-flex">
					<div class="trow1 d-flex align-items-center fullwidth"><i class="fa fa-comments"></i>&nbsp; Total Posts:</div>
					<div class="trow1 d-flex align-items-center fullwidth"><span class="ml-auto"><a href="search.php?action=finduser&amp;uid={$memprofile['uid']}">{$memprofile['postnum']}</a></span></div>
				</div>
			</div>
		</div>
		<br>
		{$profilefields}
		{$signature}
		{$modoptions}
		{$adminoptions}
	</div>
	<div class="p-sidebar">
		<br>
		<table border="0" cellspacing="0" cellpadding="5" class="tborder tfixed">
			<tr>
				<td class="thead"><strong>Credits</strong></td>
			</tr>
			<tr>
				<td class="trow1" align="center">Ripped by YASAKA<br>Owner of Sinful Site</td>
			</tr>
		</table>
		<br>
		<table border="0" cellspacing="0" cellpadding="5" class="tborder tfixed">
			<tr>
				<td class="thead"><strong>About Us</strong></td>
			</tr>
			<tr>
				<td class="trow1">Sinful Site is a forum based on general discussion and sharing of related resources. You can also find lots of leaks, tools, software, tutorials, and more. Learn many things here, new friends and have fun with our special features. We will not disappoint you!</td>
			</tr>
			<tr>
				<td class="trow1" align="center"><a href="https://sinfulsite.com/" target="_blank">www.sinfulsite.com</a></td>
			</tr>
		</table>
	</div>
</div>
{$footer}
</body>
</html>