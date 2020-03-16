import os

################################################################################
# Clean out files with certain suffixes
################################################################################

#suffixlist = ['aux','out','pdf','toc','lot','lof','log']
# But wait, keep the pdf!
suffixlist = ['aux','out','toc','lot','lof','log','bbl','blg']

files = []
for (dirpath, dirnames, filenames) in os.walk('.'):
  files.extend(os.path.join(dirpath, filename) for filename in filenames)
  for subdir in dirnames:
    for (subdirpath, subdirnames, subfilenames) in os.walk(subdir):
      files.extend(os.path.join(subdirpath, subfilename) for subfilename in subfilenames)
  break

print '\nPrinting all files...'
print files

found = []
for f in files:
  for s in suffixlist:
    if s in f:
      found.append(f)

print '\nPrinting matches for removal...'
print found

for f in found:
  os.remove(f)

