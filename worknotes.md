#####################################################################
NOTES:
setting PYTHONPATH:
	windows:
		$env:PYTHONPATH = "path/to/BatchManager"
		$env:PYTHONPATH = "C:\Users\sy000661\Documents\Dev\"
		Get-ChildItem Env:PYTHONPATH

	unix like:
		PYTHONPATH=${PYTHONPATH}:path/to/BatchManager


to install external packages:
	add packages to requirements.txt
	pip install --trusted-host pypi.python.org -r requirements.txt


