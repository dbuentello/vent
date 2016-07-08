import os
import pytest

from ..service_urls import get_urls

def test_url():
    """ Tests get_urls """
    get_urls.url(get_url.PathDirs(), "elasticsearch", "head")
    get_urls.url(get_url.PathDirs(), "elasticsearch", "marvel")
    get_urls.url(get_url.PathDirs(), "aaa-rabbitmq", "")
    get_urls.url(get_url.PathDirs(), "rq-dashboard","")
    get_urls.url(get_url.PathDirs(), "aaa-syslog", "")
    path_dirs = get_urls.PathDirs(base_dir=os.getcwd()+"/")

    filedata = None
    with open(path_dirs.template_dir + 'core.template', 'r') as f:
        filedata = f.read()
    filedata = filedata.replace('off', 'on')
    with open(path_dirs.template_dir + 'core.template', 'w') as f:
        f.write(filedata)
    get_urls.url(path_dirs, "elasticsearch", "head")
    get_urls.url(path_dirs, "elasticsearch", "marvel")
    get_urls.url(path_dirs, "aaa-rabbitmq", "")
    get_urls.url(path_dirs, "rq-dashboard","")
    get_urls.url(path_dirs, "aaa-syslog", "")
