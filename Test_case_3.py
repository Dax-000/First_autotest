from PageSbisDownloads import SbisDownloads
from PageSbisIndex import SbisIndex
from urllib.error import URLError
import wget
from os.path import getsize, join
from os import remove, listdir


def download_file(url, path, logger):
    file, error = None, None
    try:
        file = wget.download(url, path)
        logger.info(f"Downloaded file {file}")
    except URLError as err:
        logger.error(f"Download error", exc_info=True)
        error = err
    finally:
        return file, error


def clear_directory(dir):
    for f in listdir(dir):
        remove(join(dir, f))


def test_go_to_downloads(browser, logger):
    sbis_index = SbisIndex(browser, logger)
    sbis_index.go_to_site("https://sbis.ru/")
    sbis_index.click_on_download_page()
    assert "https://sbis.ru/download" in sbis_index.get_url()


def test_download_plugin(browser, logger):
    path = "downloads/"
    clear_directory(path)
    sbis_download = SbisDownloads(browser, logger)
    sbis_download.click_on_tab_plugin()
    url, MBs = sbis_download.get_plugin_download_data()
    file, err = download_file(url, path, logger)
    assert not err, err
    file_size = round(getsize(file)/1048576, 2)
    assert file_size == MBs
