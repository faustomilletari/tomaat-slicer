import slicer
# install requests
try:
  import requests
except:
  slicer.util.pip_install('requests')
  import requests
  pass

# install requests_toolbelt
try:
  from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
except:
  slicer.util.pip_install('requests_toolbelt')
  from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
  pass
