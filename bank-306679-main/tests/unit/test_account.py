from src.account import Account


def test_account_stores_first_name_last_name_and_pesel():
    account = Account("Jan", "Kowalski", "90010112345")

    assert account.first_name == "Jan"
    assert account.last_name == "Kowalski"
    assert account.pesel == "90010112345"

def test_pesel_too_short_is_invalid():
    # 10 cyfr zamiast 11
    account = Account("Jan", "Kowalski", "1234567890")
    assert account.pesel == "Invalid"
def test_pesel_too_long_is_invalid():
     # 12 cyfr zamiast 11
    account = Account("Jan", "Kowalski", "123456789012")
    assert account.pesel == "Invalid"
def test_pesel_with_letters_is_invalid():
     # 11 znaków, ale zawiera literę w środku
     account = Account("Jan", "Kowalski", "12345a78901")
     assert account.pesel == "Invalid"
def test_code_dodaje_50():
    account = Account("Jan", "Kowalski", "90010112345", promo_code="PROM_123")
    assert account.balance == 50
def test_no_promo_code():
    account = Account("Jan", "Kowalski", "90010112345", promo_code=None)
    assert account.balance == 0
def test_too_short_promo_code():
    account = Account("Jan", "Kowalski", "90010112345", promo_code="PROM_12")
    assert account.balance == 0
def test_too_long_promo_code():
    account = Account("Jan", "Kowalski", "90010112345", promo_code="PROM_1234")
    assert account.balance == 0
def test_wrong_prefix_promo_code():
    account = Account("Jan", "Kowalski", "90010112345", promo_code="DISC_123")
    assert account.balance == 0


    

   
