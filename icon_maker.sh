read -p "Enter Icon Name: " name
read -p "Enter absoulte path of icon image: " path
read -p "Enter executable filepath: " exe
read -p "Enter categories: " app
Name=`echo "$name"".desktop"`
echo "$Name"
cat << _EOF_ > $Name
[Desktop Entry]
Name=$name
Icon=$path
Exec=$exe
Terminal=false
Type=Application
Categories=$app
_EOF_

sudo desktop-file-install $Name
echo "Success"
