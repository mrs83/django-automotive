import os
import shutil
import zipfile
import tempfile
import urlparse
import requests
import progressbar


def download_file(url, chunk_size=1024 * 1024):
    name = os.path.basename(urlparse.urlparse(url).path)
    suffix = os.path.splitext(name)[1]
    r = requests.get(url, stream=True)
    total_size = int(r.headers['content-length'])
    pbar = progressbar.ProgressBar(maxval=total_size).start()
    output = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
    counter = 0
    for chunk in r.iter_content(chunk_size=chunk_size):
        output.write(chunk)
        counter += chunk_size
        try:
            pbar.update(counter)
        except ValueError:
            pass
    pbar.update(total_size)
    return output


def extract_zipfile(file_obj, root_path=None, extraction_dir=None):
    temp_dir = tempfile.mkdtemp()
    with zipfile.ZipFile(file_obj) as zip_file:
    	files = zip_file.namelist()
        if root_path:
    	    files = [f for f in files if f.startswith(root_path)]
    	zip_file.extractall(temp_dir, files)
        if root_path:
            temp_dir = os.path.join(temp_dir, root_path)
        if extraction_dir:
            shutil.move(temp_dir, extraction_dir)
            return extraction_dir
        return temp_dir
