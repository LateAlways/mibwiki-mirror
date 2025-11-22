echo "displaying ${1}"

export LIBIMG_CFGFILE=/etc/imgprocessing.cfg
LD_LIBRARY_PATH=/eso/lib:/armle/lib:/root/lib-target:/armle/lib/dll /eso/bin/apps/loadandshowimage ${1}&

#try to figure out if the broker is running as a signal that the framework is available
if pidin | grep -v grep | grep broker > /dev/null
then
	LD_LIBRARY_PATH=/eso/lib:/armle/lib:/root/lib-target IPL_CONFIG_DIR=/etc/eso/production /eso/bin/apps/dmdt sc 0 -9
	echo "press any key to continue..."
	read ASD
	LD_LIBRARY_PATH=/eso/lib:/armle/lib:/root/lib-target /eso/bin/apps/loadandshowimage 1 2 3 4 5 

	LD_LIBRARY_PATH=/eso/lib:/armle/lib:/root/lib-target IPL_CONFIG_DIR=/etc/eso/production /eso/bin/apps/dmdt sb 0
else
	echo "press any key to continue..."
	read ASD
	LD_LIBRARY_PATH=/eso/lib:/armle/lib:/root/lib-target /eso/bin/apps/loadandshowimage 1 2 3 4 5 
fi


