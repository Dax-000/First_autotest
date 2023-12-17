from PageSbisIndex import SbisIndex
from PageSbisContacts import SbisContacts
from PageTensorIndex import TensorIndex
from PageTensorAbout import TensorAbout


def test_go_to_contacts(browser, logger):
    sbis_index = SbisIndex(browser, logger)
    sbis_index.go_to_site("https://sbis.ru/")
    sbis_index.click_on_contacts()
    assert "https://sbis.ru/contacts" in sbis_index.get_url()


def test_go_to_tensor(browser, logger):
    sbis_contacts = SbisContacts(browser, logger)
    sbis_contacts.click_on_tensor()
    assert sbis_contacts.get_url() == "https://tensor.ru/"


def test_sila_section(browser, logger):
    tensor_index = TensorIndex(browser, logger)
    assert tensor_index.check_sila_section()
    tensor_index.click_on_about()
    assert tensor_index.get_url() == "https://tensor.ru/about"


def test_rabota_section(browser, logger):
    tensor_about = TensorAbout(browser, logger)
    assert tensor_about.check_size_equality()
