from PageSbisIndex import SbisIndex
from PageSbisContacts import SbisContacts


def get_my_region():
    return "г. Москва"


def test_go_to_contacts(browser, logger):
    sbis_index = SbisIndex(browser, logger)
    sbis_index.go_to_site("https://sbis.ru/")
    sbis_index.click_on_contacts()
    assert "https://sbis.ru/contacts" in sbis_index.get_url()


def test_check_region_url(browser, logger):
    sbis_contacts = SbisContacts(browser, logger)
    region = sbis_contacts.get_region()
    assert region == get_my_region()


# def test_check_region_