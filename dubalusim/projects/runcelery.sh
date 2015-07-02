#!/bin/sh
cd "`dirname "$0"`"
cd ..

name="celeryd"
loglevel=${celeryd_loglevel:-"INFO"}
pool_cls=${celeryd_pool_cls:-"threads"}

method="console"
# method="single"
mode="$1"
if [ $# -gt 0 ]; then
	case $mode in
		multiple|multi|m|c|C|3 )
			method="multiple"
			shift
		;;
		single|sing|s|b|B|2 )
			method="single"
			shift
		;;
		console|con|c|a|A|1 )
			method="console"
			shift
		;;
	esac
fi
if [ -n "${celeryd_profiles}" ]; then
	profiles="${celeryd_profiles}"
elif [ -n "$*" ]; then
	profiles="$*"
elif [ -n "${profiles_dir}" ]; then
	for I in ${profiles_dir}/*; do
		profile=`basename "$I"`
		profiles="${profile} ${profiles}"
	done
else
	if [ -z $PROJECT ] && [ -f "PROJECT" ]; then
		PROJECT=`cat PROJECT`
	fi
	if [ -z $PROJECT ]; then
		echo "You need to set up PROJECT_NAME environment variable or create a PROJECT file with the project name in it!" 1>&2
		exit
	fi
	IFS=. read -r PROJECT_NAME PROJECT_SUFFIX <<EOC
$PROJECT
EOC
	PROJECT_NAME=$(echo "$PROJECT_NAME" | sed 's/\-/_/g')
	if [ -z $PROJECT_SUFFIX ] && [ -f "PROJECT_SUFFIX" ]; then
		PROJECT_SUFFIX=`cat PROJECT_SUFFIX`
	fi
	PROJECT_SUFFIX=$(echo "$PROJECT_SUFFIX" | sed 's/\-/_/g')
	profiles="$PROJECT_NAME.$PROJECT_SUFFIX"
fi
echo "Projects to work on: ${profiles}"

celeryd_start() {
	for profile in ${profiles}; do
		echo "Starting ${profile}..."
		eval logfile=\${celeryd_logfile:-"${name}-${profile}-%n.log"}
		eval pidfile=\${celeryd_pidfile:-"${name}-${profile}-%n.pid"}
		PROJECT=${profile} python "$PWD/manage.py" celery multi start $nodes --interpreter=python --pidfile=$pidfile --logfile=$logfile --loglevel=$loglevel $flags
	done
}

celeryd_stop() {
	for profile in ${profiles}; do
		echo "Stopping ${profile}..."
		eval logfile=\${celeryd_logfile:-"${name}-${profile}-%n.log"}
		eval pidfile=\${celeryd_pidfile:-"${name}-${profile}-%n.pid"}
		PROJECT=${profile} python "$PWD/manage.py" celery multi stop $nodes --interpreter=python --pidfile=$pidfile --logfile=$logfile --loglevel=$loglevel
	done
}

method_console() {
	celeryd_flags="-P $pool_cls"
	flags=${celeryd_flags:-}
	for profile in ${profiles}; do
		echo "Starting ${profile}..."
		PROJECT=${profile} python "$PWD/manage.py" celery worker --loglevel=DEBUG $flags  # --autoreload
	done
}

method_single() {
	celeryd_nodes="1"
	celeryd_flags="-P $pool_cls"
	eval nodes=\${celeryd_nodes:-"1"}
	eval flags=\${celeryd_flags:-""}
	trap celeryd_stop 1 2 15 && celeryd_start && sleep 1 && tail -F ${name}*.log
}

method_multiple() {
	celeryd_nodes="2"
	celeryd_flags="-P $pool_cls"
	eval nodes=\${celeryd_nodes:-"1"}
	eval flags=\${celeryd_flags:-""}
	trap celeryd_stop 1 2 15 && celeryd_start && sleep 1 && tail -F ${name}*.log
}


rm -f ${name}*.log

case $method in
	multiple )
		echo "Running multiple running workers in $pool_cls mode as deamon..."
		method_multiple ;;
	single )
		echo "Running a single running worker with in $pool_cls mode as a deamon..."
		method_single ;;
	console )
		echo "Running in $pool_cls mode in the console..."
		method_console ;;
esac
