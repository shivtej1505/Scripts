read -p "Enter Icon Name: " name

# Icon finder
read -p "Enter name of icon image: " icon
echo $icon
result=`find ~ -iname $icon`

num=1
for Icon in $result
do
	echo "Showing Image No. $num"
	eog $Icon
	names[$num-1]=$Icon
	echo ${names[$num-1]}
	let num=$num+1
done

read -p "Which image do you choose?:" ans
echo $ans
let ans=$ans-1

echo ${names[$ans]}
path=${names[$ans]}

# Executable finder
read -p "Enter executable filename: " exe
echo $icon
result=`find ~ -iname $exe`

num=1
for Exe in $result
do
	echo "Showing file no. $num"
	names[$num-1]=$Exe
	echo ${names[$num-1]}
	let num=$num+1
done

read -p "Which file would you choose?: " ans

echo $ans
let ans=$ans-1
chmod 774 ${names[$ans]}
echo ${names[$ans]}

read -p "Any extra arguments: " args
cute=${names[$ans]} $args
echo $cute | sed 's/)/\\)/g' | sed 's/(/\\(/g' | sed 's/:/\\:/g'

#Cute=`echo $cute | sed 's/)/\\)/g' | sed 's/(/\\(/g' | sed 's/:/\\:/g'`
Cute=`printf '%q' $cute`
echo "Cute: $Cute"

read -p "Enter categories: " app
Name=`echo "$name"".desktop"`
echo "$Name"
cat << _EOF_ > $Name
[Desktop Entry]
Name=$name
Icon=$path
Exec=$Cute
Terminal=false
Type=Application
Categories=$app
_EOF_

sudo desktop-file-install $Name
echo "Success"
