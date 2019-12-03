import glob
import zipfile

# with zipfile.ZipFile('test.zip', 'w') as z:
#     for f in glob.glob('test_dir/**', recursive=True):
#         print(f)
#         z.write(f)


with zipfile.ZipFile('test.zip', 'r') as z:
    z.extractall('zzz')