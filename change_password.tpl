<!DOCTYPE html>
<html>
<head>
	<title>Login</title>
	<link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
	<div id="site_content">
      <div id="login">
      	<form action="/change_password" method="post">
            nickname: <input name="nickname" type="text" />
            New password: <input name="new_password" type="password" />
            Old password: <input name="old_password" type="password" />
            <input value="Login" type="submit" />
        </form>
      </div>
     </div>
</body>
</html>