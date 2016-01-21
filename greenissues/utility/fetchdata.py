import os
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "greenissues.settings")
import django
django.setup()

from apps.bluefish.models import BranchInfo, ChangeInfo

# get test data path
data_path = os.path.join(os.path.dirname(
    os.path.abspath('__file__')), 'testdata')


def dril_data(full_file_path):
    word = full_file_path.split(' - ')[0]
    return(word[: word.index('#')])


def get_data(file_name):
    changelist = []
    (file_name_info, file_ext) = os.path.splitext(file_name)
    file_info = os.path.basename(file_name_info).split('-')
    if os.path.getsize(file_name) > 0:
        try:
            branch = BranchInfo.objects.get(branch_name=file_info[0], from_build=file_info[
                                            1], to_build=file_info[2])
        except:
            branch = BranchInfo.objects.create(
                branch_name=file_info[0],
                from_build=file_info[1],
                to_build=file_info[2])
        try:
            with open(file_name) as f:
                for line in f.readlines():
                    (file_path, file_name) = os.path.split(dril_data(line))
                    changelist.append(ChangeInfo(
                        branch=branch,
                        file_path=file_path,
                        file_name=file_name))
                ChangeInfo.objects.bulk_create(changelist)


        except IOError as ioError:
            print("File error" + str(ioError))
            return(None)

def getChange(data_path):
    files = os.listdir(data_path)
    for f in files:
        if(os.path.isfile(os.path.join(data_path, f))):
            get_data(os.path.join(data_path, f))
            os.remove(os.path.join(data_path, f))
        else:
            print("please provide a data file with name like DAX63HFSTAB-6.3.3000.101-6.3.3000.106.txt")
