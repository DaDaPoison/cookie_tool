# Cookie tool
## Ultimate cookie tool for python+selenium, that's work everywhere(i hope so) 
### Description:
Sometimes basic selenium methods of working with cookies don't work. Because selenium can't use cookie, if it's domain is not similar with page, where cookies are used.
So you have to use JavaScript by webdriver.execute_script. Sometimes it is hard for newbies (like me) or just not very comfortable. So i made a script, that saves different cookies in different files
(1 cookie == 1 file). And than, using the 'use_cookie' method information from cookies get parsed as a dict and executes in webdriver.execute_script.
	You can used just like imported methods, but the best way to use it in POM. You just need to copy methods 'get_cookie' and 'use_cookie' and paste them into your base class and use it.
	
	
	I hope this script will help you, if you have troubles with 'unusual' cookies.
	Enjoy!!
