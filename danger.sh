alias sudo="ls"
while [ 1 ]
do 
	history  | grep "sudo"
	if [ "$?" -ne 1 ] 
	then
		echo "yo"
		#read -p "[sudo] password for $USER: " -s d
		break
	fi
done
#echo $d
