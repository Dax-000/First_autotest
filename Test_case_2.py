from pages.PageSbisIndex import SbisIndex
from pages.PageSbisContacts import SbisContacts


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


def test_check_partners(browser, logger):
    sbis_contacts = SbisContacts(browser, logger)
    assert sbis_contacts.get_partners_item_keys(1)


def test_switch_region(browser, logger):
    new_region = "Камчатский край"
    sbis_contacts = SbisContacts(browser, logger)
    old_partners = sbis_contacts.get_partners_item_keys(5)
    region_code = sbis_contacts.change_region(new_region)
    assert sbis_contacts.get_region() == new_region
    assert sbis_contacts.get_partners_item_keys(5) != old_partners
    url_region = int(sbis_contacts.get_url().split("/")[-1][:2])
    assert url_region == region_code
