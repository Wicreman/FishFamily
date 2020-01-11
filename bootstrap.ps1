Function Get-EnlistmentDrive 
{   
        $volumes = Get-Volume

        foreach ($volume in $volumes)
        {
            $driveLetter = $volume.DriveLetter

            $vhdInfo = "${driveLetter}:\DAX63HF\sd.ini"
            if (Test-Path $vhdInfo)
            {           
                return $driveLetter
            }
        }
    

    Throw "No DAX63HF enlistment drive found"
}

. { iwr -useb https://boxstarter.org/bootstrapper.ps1 } | iex; Get-Boxstarter -Force
choco install python -y
#choco install mysql -y
#choco install mysql.workbench -y
#choco install mysql-cli -y
#choco install mysql.utilities -y
choco install git -y

#Set python environment
[Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python38")

# Initialize variables
$enlistmentDrive = Get-EnlistmentDrive
$fishDir = "${enlistmentDrive}:\FishFamily\fishs"
$djangoIssuePath = "C:\Python38\lib\site-packages\django\db\backends\mysql"

# clone and install requirements
Push-Location "${enlistmentDrive}:\"
git clone https://github.com/Wicreman/FishFamily.git
python -m pip install -U pip
python -m pip install -r "${fishDir}\requirements.txt"

Copy-Item -Path "${fishDir}\replace\base.py" -Destination  $djangoIssuePath  -Force
Copy-Item -Path "${fishDir}\replace\operations.py" -Destination $djangoIssuePath  -Force
Pop-Location

Push-Location $fishDir
Write-Host "Migrate the database..."
python manage.py migrate

Write-Host "Start the server..."
python manage.py runserver 0.0.0.0:8000
Pop-Location
